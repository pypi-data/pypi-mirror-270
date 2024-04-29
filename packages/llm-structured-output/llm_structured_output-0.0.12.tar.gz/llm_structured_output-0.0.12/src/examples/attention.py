# pylint: disable=missing-function-docstring,missing-class-docstring
"""
Example server to visualize the generation mechanism.
"""
import json
from operator import itemgetter
import os
from typing import Optional

from fastapi import FastAPI, Request, status
from fastapi.responses import FileResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import mlx.core as mx
import mlx.nn as nn
from mlx_lm.utils import load
from llm_structured_output import (
    JsonSchemaAcceptorDriver,
    HuggingfaceTokenizerHelper,
)
from llm_structured_output.util.output import info, debug, warning


class ObservedLLM:
    def __init__(self, model_path: str):
        self.model, self.tokenizer = load(model_path)
        self.tokenizer_helper = HuggingfaceTokenizerHelper(self.tokenizer)
        self.vocabulary, self.eos_id = self.tokenizer_helper.extract_vocabulary()
        self.token_acceptor_factory = JsonSchemaAcceptorDriver.driver_factory_for_model(
            self.vocabulary, self.eos_id
        )
        self.cache = None
        self.tokens = []
        self.fragments = []
        self.layer_attention_scores = []
        self.token_acceptor = None
        self.layer_attention_scores = []

        # Replace the attention dot product function to be able to look into it.
        def mock_fast_scaled_dot_product_attention(
            queries, keys, values, *, scale, mask=None, stream=None
        ):
            """
            O = softmax(Q @ K.T, dim=-1) @ V
            """
            B, n_kv_heads, L, _ = keys.shape
            _, n_heads, _, _ = queries.shape
            repeats = n_heads // n_kv_heads

            def repeat(a):
                a = mx.concatenate([mx.expand_dims(a, 2)] * repeats, axis=2)
                return a.reshape([B, n_heads, L, -1])

            keys, values = map(repeat, (keys, values))

            scores = (queries * scale) @ keys.transpose(0, 1, 3, 2)
            if mask is not None:
                scores += mask
            scores = mx.softmax(scores.astype(mx.float32), axis=-1).astype(scores.dtype)
            result = scores @ values
            self.layer_attention_scores.append(scores[0, :, -1, :].tolist())
            return result

        mx.fast.scaled_dot_product_attention = mock_fast_scaled_dot_product_attention

    def start(self, prompt: str, schema: dict):
        if schema:
            self.token_acceptor = self.token_acceptor_factory(schema)

        prior_tokens = self.tokens
        self.tokens = self.tokenizer_helper.encode_prompt(prompt)
        self.fragments = [
            self.tokenizer_helper.no_strip_decode([token]) for token in self.tokens
        ]

        # If we had started a generation before, try to reuse as much of the cache as possible.
        i = 0
        for i, t in enumerate(prior_tokens):
            if len(self.tokens) <= i or self.tokens[i] != t:
                break
        if i:
            self.cache = [
                (
                    layer_key_cache[:, :, :i, :],
                    layer_value_cache[:, :, :i, :],
                )
                for layer_key_cache, layer_value_cache in self.cache
            ]
            new_tokens = self.tokens[i:]
        else:
            self.cache = None
            new_tokens = self.tokens

        print(f"{new_tokens}")
        return self._generate(new_tokens)

    def add_token(self, token):
        self.tokens.append(token)
        self.fragments.append(self.tokenizer_helper.no_strip_decode([token]))
        if self.token_acceptor:
            self.token_acceptor.advance_token(token)
        return self._generate([token])

    def _generate(self, new_input_tokens: list[int]):
        self.layer_attention_scores = []
        logits, self.cache = self._run_model(
            mx.array(new_input_tokens)[None], self.cache
        )
#        layer_attention_totals = [sum(layer) for layer in self.layer_attention_scores]
#        token_attention_scores = [
#            sum(
#                layer_scores[token_index] / layer_total
#                for layer_scores, layer_total in zip(
#                    self.layer_attention_scores, layer_attention_totals
#                )
#            )
#            / len(self.layer_attention_scores)
#            for token_index in range(len(self.fragments))
#        ]
#        print("LAYER", self.layer_attention_scores)
#        print("TOTALS", layer_attention_totals)
#        print("FINAL", token_attention_scores)
#        fragment_attention_scores = [*zip(self.fragments, token_attention_scores)]


        TOP_TOKEN_COUNT = 25
        probs = mx.softmax(logits[0, -1, :])
        top_token_partition = mx.argpartition(probs, -TOP_TOKEN_COUNT)[
            -TOP_TOKEN_COUNT:
        ]
        top_token_probs = sorted(
            [*zip(top_token_partition.tolist(), probs[top_token_partition].tolist())],
            key=itemgetter(1),
            reverse=True,
        )

        if self.token_acceptor:
            accepted_token_bitmap = self.token_acceptor.select_valid_tokens()
            rejected_top_tokens = set(
                token
                for token, _ in top_token_probs
                if not (accepted_token_bitmap & (1 << token))
            )
        else:
            rejected_top_tokens = set()

        top_tokens = [
            (
                token,
                self.tokenizer_helper.no_strip_decode([token]),
                p,
                token in rejected_top_tokens,
            )
            for token, p in top_token_probs
        ]

        return {
            #"attention_scores": fragment_attention_scores,
            "attention_scores": self.layer_attention_scores,
            "fragments": self.fragments,
            "top_tokens": top_tokens,
        }

    def _run_model(self, inputs: mx.array, cache=None):
        """
        This is like the model's __call__() method as implemented in
        `mlx-examples/llms/mlx_lm/models/*.py`, except it is also able
        to apply a causal mask once a cache is in place.
        """
        model = self.model.model
        h = model.embed_tokens(inputs)

        mask = None
        T = h.shape[1]  # pylint: disable=invalid-name
        if T > 1:
            if cache is None:
                S = 0  # pylint: disable=invalid-name
            else:
                S = cache[0][0].shape[2]  # pylint: disable=invalid-name
            mask = nn.MultiHeadAttention.create_additive_causal_mask(S + T)
            mask = mask.split([S])[1].astype(h.dtype)

        if cache is None:
            cache = [None] * len(model.layers)

        for e, layer in enumerate(model.layers):
            h, cache[e] = layer(h, mask, cache[e])

        out = model.norm(h)
        return self.model.lm_head(out), cache


try:
    MODEL_PATH = os.environ["MODEL_PATH"]
except KeyError:
    MODEL_PATH = "mlx-community/Meta-Llama-3-8B-Instruct-4bit"
    info("No MODEL_PATH environment variable, using default model.")

info(f"Loading model {MODEL_PATH}...")
llm = ObservedLLM(MODEL_PATH)


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_request: Request, exc: RequestValidationError):
    exc_str = f"{exc}"
    warning(f"RequestValidationError: {exc_str}")
    content = {"status_code": 10422, "message": exc_str, "data": None}
    return JSONResponse(
        content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )


@app.get("/")
def get_root():
    return FileResponse(
        f"{os.path.dirname(os.path.realpath(__file__))}/static/attention.html"
    )


@app.get("/status")
def get_status():
    return {"status": "OK"}


class GenerationStartRequest(BaseModel):
    prompt: str
    schema: Optional[str] = None


@app.post("/generation/start")
async def post_generation_start(request: GenerationStartRequest):
    debug("REQUEST", request)
    if request.schema:
        schema = json.loads(request.schema)
    else:
        schema = None
    response = llm.start(request.prompt, schema)
    # debug("RESPONSE", response)
    return response


class GenerationTokenRequest(BaseModel):
    token: int


@app.post("/generation/token")
async def post_generation_token(request: GenerationTokenRequest):
    debug("REQUEST", request)
    response = llm.add_token(request.token)
    debug("RESPONSE", response)
    return response
