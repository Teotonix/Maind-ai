import gradio as gr

def chat(msg):
    return "Backend çalışıyor ✅ Mesajın: " + msg

gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text",
    title="MaindAI Test"
).launch()
