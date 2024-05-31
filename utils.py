from deepeval.models.base_model import DeepEvalBaseLLM
from llama_index.core.llms import LLM
from typing import List, Optional


class StandardlizedDeepEvalLLM(DeepEvalBaseLLM):
    def __init__(self, model :LLM):
        self.model = model

    def load_model(self):
        return self.model

    def generate(self, prompt: str) -> str:
        # Return model
        chat_model = self.load_model()
        # Check model type
        if isinstance(chat_model,LLM):
            res = chat_model.complete(prompt=prompt)
            return res.text
        else:
            raise Exception("Doesn't support")

    async def a_generate(self, prompt: str) -> str:
        # Return model
        chat_model = self.load_model()
        # Check model type
        if isinstance(chat_model, LLM):
            res = await chat_model.acomplete(prompt=prompt)
            return res.text
        else:
            raise Exception("Doesn't support")

    def get_model_name(self) -> str:
        # Return model
        chat_model = self.load_model()
        # Check model type
        if isinstance(chat_model, LLM):
            return chat_model.class_name()