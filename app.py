import gradio as gr

def hello(name):
    return "Çalışıyor: " + name

demo = gr.Interface(
    fn=hello,
    inputs="text",
    outputs="text"
)

demo.launch()
