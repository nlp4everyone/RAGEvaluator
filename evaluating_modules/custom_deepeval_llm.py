from deepeval.models.base_model import DeepEvalBaseLLM
from llama_index.core.llms import LLM

class CustomDeepEvalLLM(DeepEvalBaseLLM):
    def __init__(self, model):
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

    async def a_generate(self, prompt: str) -> str:
        # Return model
        chat_model = self.load_model()
        # Check model type
        if isinstance(chat_model, LLM):
            res = await chat_model.acomplete(prompt=prompt)
            return res.text

    def get_model_name(self):
        return "Custom Azure OpenAI Model"