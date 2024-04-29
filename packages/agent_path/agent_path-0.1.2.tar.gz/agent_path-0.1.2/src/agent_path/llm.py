import json
from typing import Any, Dict, List, Literal, Optional

from dotenv import load_dotenv
from jinja2 import Template
from llama_index.core.llms import LLM as LlamaIndexLLM
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI
from openai.types.chat import ChatCompletionMessageToolCall
from pydantic import BaseModel, ValidationError

from agent_path.utils import fancy_print, get_json_object, get_xml_tags


class LLM:
    client: LlamaIndexLLM
    verbose: bool

    def __init__(self, client: LlamaIndexLLM, verbose: bool = False) -> None:
        self.client = client
        self.verbose = verbose

    @classmethod
    def from_default_demo(
        cls, model: str = "gpt-4", temperature: float = 0.5, verbose=True
    ) -> "LLM":
        return cls(OpenAI(model, temperature=temperature, timeout=180), verbose=verbose)

    def generate(self, text: str) -> str:
        return self.client.chat([ChatMessage(content=text)]).message.content

    def generate_with_tools_react(self, text: str, tools: List[FunctionTool]):
        TEMPLATE = """
You are working on a task:
```
{{ text }}
```

Previous thoughts, tools usage, and observations:
```jsonl
{{ history}}
```

First, you should check it the task can be answered directly, following the previous thoughts, tools usage, and observations.
If the task can be solved now, give me the answer.
Otherwise, follow the tools' instructions to use them to solve the task. A tool's input is a JSON object described by a JSON schema. 
When using tools, output must contain "<ACTION> a JSON object containing tool's name and arguments </ACTION>"
When give answer, output must contain "<ANSWER_OUTPUT> The answer output </ANSWER_OUTPUT>"
No ANSWER_OUTPUT when using tools. No ACTION when giving answer.

Tools' instructions:
```json
{{ tools }}
```

Output format:
```
<THOUGHT>
your thought this time
</THOUGNT>
<ACTION>
{
    "tool_name": string, "The tool's name",
    "arguments": object, "The JSON object described by the JSON schema of the tool's instruction"
}
</ACTION>
<ANSWER_OUTPUT>
The answer output
</ANSWER_OUTPUT>
```
"""

        tools_dict = [
            {
                "name": tool.metadata.name,
                "description": tool.metadata.description,
                "parameters": tool.metadata.get_parameters_dict(),
            }
            for tool in tools
        ]

        class Reason(BaseModel):
            class Action(BaseModel):
                tool_name: str
                arguments: Dict[str, Any]

            thought: Optional[str] = None
            action: Optional[Action] = None
            observation: Optional[str] = None

        # Start tool calling loop
        history: List[Reason] = []
        while True:
            # Prepare prompt
            prompt = Template(TEMPLATE).render(
                text=text,
                tools=json.dumps(tools_dict, indent=4),
                history="\n".join(
                    [r.model_dump_json(exclude_none=True) for r in history]
                ),
            )

            # Generate response until contains valid answer or action
            while True:
                res = self.generate(prompt)
                tags = get_xml_tags(res)

                def fail(ans: str):
                    if self.verbose:
                        fancy_print("====== Error in response ======", color="red")
                        fancy_print(ans, color="red")
                        fancy_print("retrying...", color="red")

                thought_str = tags.get("THOUGHT", None)
                ans_output = tags.get("ANSWER_OUTPUT", None)
                action_str = tags.get("ACTION", None)
                try:
                    action = (
                        Reason.Action.model_validate_json(get_json_object(action_str))
                        if action_str
                        else None
                    )
                except ValidationError:
                    fail(res)
                    continue

                if ans_output or action:
                    break
                else:
                    fail(res)

            if self.verbose:
                fancy_print("========================")
                fancy_print("THOUGHT:\n" + thought_str) if thought_str else None
                fancy_print("ACTION:") if action else None
                fancy_print(action.model_dump()) if action else None
                fancy_print("ANSWER_OUTPUT:\n" + ans_output) if ans_output else None

            # Return answer if no action
            if ans_output and not action:
                return ans_output

            # Call tool and get observation
            name_to_tool = {tool.metadata.name: tool for tool in tools}
            failed = False
            try:
                tool = name_to_tool[action.tool_name]
            except KeyError:
                observation = f"Tool name {action.tool_name} not found."
                failed = True
            else:
                observation = tool.call(**action.arguments).content

            if self.verbose:
                fancy_print(
                    "OBERVATION:\n" + observation,
                    color="red" if failed else None,
                )

            # Append to history, continue loop
            history.append(
                Reason(thought=thought_str, action=action, observation=observation)
            )

    def generate_with_tools_api(self, text: str, tools: List[FunctionTool]) -> str:
        if not isinstance(self.client, OpenAI):
            raise ValueError("Only OpenAI client is supported")

        name_to_tool = {tool.metadata.name: tool for tool in tools}
        chat_his: List[ChatMessage] = [ChatMessage(content=text)]
        while True:
            res = self.client.chat_with_tools(
                tools=tools,
                chat_history=chat_his,
            )
            tool_calls = res.message.additional_kwargs.get("tool_calls", [])
            if res.message.content:
                if self.verbose:
                    fancy_print("======= Output: ========")
                    fancy_print(str(res.message.content))
                if len(tool_calls) == 0:
                    return str(res.message.content)

            chat_his.append(res.message)
            for tool_call in tool_calls:
                tool_call_model = ChatCompletionMessageToolCall.model_validate(
                    tool_call, from_attributes=True
                )
                tool = name_to_tool[tool_call_model.function.name]
                args_model = tool.metadata.fn_schema.validate(
                    json.loads(tool_call_model.function.arguments)
                )
                if self.verbose:
                    fancy_print("========================")
                    fancy_print(
                        f"Tool Calling: {tool_call_model.function.name}",
                    )
                    fancy_print(args_model.dict())
                output = tool.call(**args_model.dict())
                content = output.content
                if self.verbose:
                    fancy_print("===== Tool Output: =====")
                    fancy_print(str(content))
                chat_his.append(
                    ChatMessage(
                        role=MessageRole.TOOL,
                        content=content,
                        additional_kwargs={"tool_call_id": tool_call_model.id},
                    )
                )

    def generate_with_tools(
        self,
        text: str,
        tools: List[FunctionTool],
        mode: Literal["react", "api"] = "react",
    ) -> str:
        if mode == "react":
            return self.generate_with_tools_react(text, tools)
        elif mode == "api":
            return self.generate_with_tools_api(text, tools)
        else:
            raise ValueError("Invalid mode")


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    def get_location() -> str:
        return "Shanghai"

    def get_weather(location: str, unit: Literal["C", "F"] = "C") -> float:
        return 15

    llm = LLM.from_default_demo()

    task = "Using a haiku poem to describe the weather today. It must be accurate and not use any information not provided."
    fancy_print(llm.generate(task))
    fancy_print(
        llm.generate_with_tools_api(
            task,
            [
                FunctionTool.from_defaults(get_weather),
                FunctionTool.from_defaults(get_location),
            ],
        )
    )
    fancy_print(
        llm.generate_with_tools_react(
            task,
            [
                FunctionTool.from_defaults(get_weather),
                FunctionTool.from_defaults(get_location),
            ],
        )
    )
