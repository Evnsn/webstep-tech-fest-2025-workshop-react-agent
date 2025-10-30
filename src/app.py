import gradio as gr
from .agent import Agent, MODELS
from .tools import tools_description

TOOLS_OPTIONS = [(tool["name"], tool["description"]) for tool in tools_description]


def chat_with_agent(
    model,
    system_prompt,
    temperature,
    max_iterations,
    tool_call_mode,
    history,
    user_message,
    *tools_selected,
):
    enabled_tools = [
        name for (name, _), selected in zip(TOOLS_OPTIONS, tools_selected) if selected
    ]
    """Handle chat interaction with the agent."""
    if not user_message.strip():
        return history, ""

    # Add user user_message to chat history
    history.append([user_message, None])

    # Get Agent
    agent = Agent(
        model=model,
        system_prompt=system_prompt,
        temperature=temperature,
        max_iterations=max_iterations,
        tool_call_mode=tool_call_mode,
        tools=enabled_tools,
    )

    # Query agent and get response
    try:
        for reply in agent.run(user_message):
            history.append(["", reply])
            yield history, ""
    except Exception as e:
        print(f"Error: {str(e)}")
        history[-1][1] = f"Error: {str(e)}"

    return history, ""


def create_interface():
    """Create the Gradio interface."""

    with gr.Blocks(title="TechFest Chat", theme=gr.themes.Base()) as demo:
        gr.Markdown("# 💬 TechFest Chat")

        with gr.Row():
            # Tab: Settings
            with gr.Tab("Settings"):

                # Model selection
                gr.Markdown("### Model")
                gr_model_dropdown = gr.Dropdown(
                    choices=MODELS,
                    value=MODELS[0],
                )

                # System prompt
                gr.Markdown("### System Prompt")
                gr_system_prompt = gr.Textbox(
                    placeholder="Agent instructions...",
                    lines=6,
                    show_label=False,
                )
                # Sliding window control (number of recent messages to consider)
                gr.Markdown("### Temperature")
                gr_temperature = gr.Slider(
                    minimum=0,
                    maximum=1,
                    value=1,
                    step=0.1,
                )

                # Max iterations control
                gr.Markdown("### Max Iterations")
                gr_max_iterations = gr.Slider(
                    minimum=1,
                    maximum=30,
                    value=1,
                    step=1,
                )

            # Tab: Tools
            with gr.Tab("Tools"):
                # Tool call mode control
                gr.Markdown("### Agent Mode")
                gr_tool_call_mode = gr.Radio(
                    choices=["reason|act", "auto"],
                    value="reason|act",
                )

                # Tools selection
                gr.Markdown("### Tools")
                gr_tools_checkboxes = []
                for name, description in TOOLS_OPTIONS:
                    checkbox = gr.Checkbox(
                        label=name, value=False, info=f"{description}"
                    )
                    gr_tools_checkboxes.append(checkbox)

            with gr.Column(scale=2):
                gr_chatbot = gr.Chatbot(
                    label="Chat",
                    height=500,
                    show_label=False,
                    container=True,
                    render_markdown=True,
                )

                with gr.Row():
                    gr_user_input = gr.Textbox(
                        placeholder="Type your message here...",
                        scale=6,
                        show_label=False,
                    )
                    with gr.Column(scale=1):
                        gr_send_btn = gr.Button("Send", scale=1, variant="primary")
                        gr_clear_btn = gr.Button("Clear Chat", variant="secondary")

        def clear_chat():
            return [], ""

        gr_user_input.submit(
            chat_with_agent,
            inputs=[
                gr_model_dropdown,
                gr_system_prompt,
                gr_temperature,
                gr_max_iterations,
                gr_tool_call_mode,
                gr_chatbot,
                gr_user_input,
            ]
            + gr_tools_checkboxes,
            outputs=[gr_chatbot, gr_user_input],
        )

        gr_send_btn.click(
            chat_with_agent,
            inputs=[
                gr_model_dropdown,
                gr_system_prompt,
                gr_temperature,
                gr_max_iterations,
                gr_tool_call_mode,
                gr_chatbot,
                gr_user_input,
            ]
            + gr_tools_checkboxes,
            outputs=[gr_chatbot, gr_user_input],
        )

        gr_clear_btn.click(clear_chat, outputs=[gr_chatbot, gr_user_input])

    return demo


def main():
    """Main function to launch the Gradio app."""
    demo = create_interface()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        auth=("webstep", "wtf2025"),  # set APP_PASSWORD in env
        auth_message="Enter workshop password",
    )


if __name__ == "__main__":
    main()
