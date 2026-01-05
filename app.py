import gradio as gr

def chat(message, history):
    return "Çalışıyor ✅"

demo = gr.ChatInterface(chat)
demo.launch()
