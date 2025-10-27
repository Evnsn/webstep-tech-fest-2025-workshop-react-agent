from .tools import LOOPING_TOOLS, tools_description, tools_available
import json
import os
from openai import OpenAI
import time
from typing import List, Literal, Optional

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODELS = [
    "gpt-4.1-nano",
    "gpt-4.1-mini",
    "gpt-4.1",
    "gpt-4o-mini",
    "gpt-4o",
]


class Agent:
    def __init__(
        self,
        model: Literal[
            "gpt-4.1-nano", "gpt-4.1-mini", "gpt-4.1", "gpt-4o-mini", "gpt-4o"
        ],
        system_prompt: str,
        temperature: float,
        max_iterations: int,
        tool_call_mode: Literal["auto", "reason|act"],
        tools: List[dict],
    ):
        self.model = model
        self.system_prompt = system_prompt
        self.temperature = temperature
        self.max_iterations = max_iterations
        self.tool_call_mode = tool_call_mode
        self.tools = tools
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def run(
        self,
        user_prompt: str,
    ) -> str:
        avaliable_tools = [
            tool for tool in tools_description if tool["name"] in self.tools
        ]
        avaliable_tools += LOOPING_TOOLS

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        tool_choice_selected = "auto" if self.tool_call_mode == "auto" else "none"
        task_solved = False

        for _ in range(self.max_iterations):
            # 0. Call LLM API
            response = self.client.responses.create(
                model=self.model,
                temperature=self.temperature,
                input=messages,
                tools=avaliable_tools,
                tool_choice=tool_choice_selected,
                parallel_tool_calls=False,
            )

            # Toggle tool-choice for next iteration
            tool_choice_selected = self._toggle_tool_choice(
                tool_choice_selected, self.tool_call_mode
            )

            # Agent loop logic
            output = response.output[0]
            # 1. Reasoning step / Final answer
            if output.type == "message":
                agent_message = {"role": "assistant", "content": output.content[0].text}
                messages.append(agent_message)
                yield response.output[0].content[0].text
            # 2. Tool call and 3. Task finished
            elif output.type == "function_call":
                function_name = output.name
                function_args = output.arguments

                # 3 Task finished => Loop finished
                if function_name == "done":
                    if json.loads(function_args).get("done", False) == True:
                        yield "`...done`"
                        task_solved = True
                        break
                    else:
                        yield "`...`"
                        continue
                # 2 Tool call
                if function_name in tools_available:
                    func = tools_available[function_name]
                    args = json.loads(function_args)
                    result = func(**args)

                    messages.append(
                        {
                            "role": "assistant",
                            "content": f"**OBSERVE:** {function_name}({args}) => {result}",
                        }
                    )
                    yield messages[-1]["content"]

                else:
                    return f"Function name: {function_name}, Function args: {function_args}"

            time.sleep(0.1)

        # If task not solved within max iterations
        if not task_solved and self.max_iterations > 1:
            yield f"`Surpassed max iterations ({self.max_iterations}) without completing the task...`"

    def _toggle_tool_choice(self, current_choice: str, tool_call_mode: str) -> str:
        """Toggle tool choice based on the toggle_mode setting."""
        if tool_call_mode == "auto":
            return "auto"
        elif tool_call_mode == "reason|act":
            tool_choices = {"required": "none", "none": "required"}
            return tool_choices[current_choice]
