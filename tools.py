import base64
from typing import Dict
import openai
from llama_index.core.tools.tool_spec.base import BaseToolSpec
import gpt4vision

# Define your location and vision functions
def handle_location_question(request):
    # Implement your logic here
    pass

def handle_vision_question(request):
    Vision.register(GPT4Vision)

# Register the tools with their respective tool specs
class CVToolSpec(BaseToolSpec):
    spec_functions = ['handle_vision_question']

    def __init__(self, client: openai.OpenAI, model: str = "gpt-4-vision-preview"):
        self._client = client
        self._model = model

    @staticmethod
    def handle_vision_question(system_message: str, query: str, image_bytes: bytes | None, token_usage_by_model: Dict[str, TokenUsage]) -> str:
        return GPT4Vision.query_image(system_message, query, image_bytes, token_usage_by_model)

class LocationToolSpec(BaseToolSpec):
    spec_functions = ['handle_location_question']

    def __init__(self):
        pass

    @staticmethod
    def handle_location_question(request): 
        return handle_location_question(request)
