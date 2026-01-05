import gradio as gr

def chat(msg):
    return f"AI cevapladı: {msg}"

demo = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(placeholder="Bir şey yaz..."),
    outputs="text",
    title="MaindAI"
)

demo.launch()
