# Llama Index Tool Specification Example Usage

## Tool Specifications
Example tools to show capabilities of increasing context windows

from llama_index.core.tools.tool_spec.base import BaseToolSpec

class CVToolSpec(BaseToolSpec):
    spec_functions = ['handle_vision_question']

    def __init__(self):
        pass

    def handle_vision_question(request):
        return handle_vision_question(request)

class LocationToolSpec(BaseToolSpec):
    spec_functions = ['handle_location_question']

    def __init__(self):
        pass

    def handle_location_question(request):
        return handle_location_question(request)
        
The CVToolSpec and LocationToolSpec classes inherit from BaseToolSpec and specify functions that handle vision and location questions, respectively.

## Integration with Llama Index
Create an OpenAI language model agent and bind it with the specified tools:

from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI

cv_tool = CVToolSpec()
loc_tool = LocationToolSpec()
full_tool_list = cv_tool.to_tool_list() + loc_tool.to_tool_list()

llm = OpenAI(model="gpt-4")
agent = OpenAIAgent.from_tools(full_tool_list, verbose=True)
This setup initializes an OpenAI LLM with a custom agent that incorporates both vision and location handling tools.

## Execution
The agent can now handle complex queries that require integration of different functionalities:

# response = agent.handle(request)







