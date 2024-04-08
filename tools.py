# tools.py

from llama_index.core.tools import FunctionTool
from . import handle_vision_request, handle_audio_response

def create_vision_tool():
    """
    Create a function tool for vision-related tasks.
    """
    # Define the function tool using Llama Index
    vision_tool = FunctionTool(
        name="Vision Tool",
        description="A tool for vision-related tasks.",
        func_dict={
            "handle_vision_request": handle_vision_request,
            "handle_audio_response": handle_audio_response
        }
    )
    
    return vision_tool
