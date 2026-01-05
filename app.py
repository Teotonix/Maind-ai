import gradio as gr

def hello(name):
    return "ÇALIŞIYOR: " + name

gr.Interface(
    fn=hello,
    inputs="text",
    outputs="text",
).launch()
