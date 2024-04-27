from dotenv import load_dotenv
from jinja2 import Template
from llama_index.core.tools import FunctionTool

from agent_path.llm import LLM

load_dotenv()
llm = LLM.from_default_demo()


def task_solve(task: str) -> str:
    """
    This function can be used to solve a task.
    """
    TEMPLATE = """
There is a task that needs to be solved. The task is: 
```
{{ text }}
```

First, you should check if the task can be solved on your own without tools.
If yes, you should solve the task directly without tools as possible.
Otherwise you can transform the task into a simpler task. Then you should use the tool to solve the simpler task.
However, you are forbided to use the tool to solve the original task directly. It can only be used to solve the simpler task.
After solving the simpler task by the tool, you can now solve the original task with the result of the simpler task.
Use language the same as the original task.
"""
    prompt = Template(TEMPLATE).render(text=task)
    ans = llm.generate_with_tools_react(
        prompt, [FunctionTool.from_defaults(task_solve)]
    )
    return ans
