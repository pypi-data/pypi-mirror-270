
import gradio as gr
from gradio_molecule2d import molecule2d


example = molecule2d().example_value()

demo = gr.Interface(
    lambda x:x,
    molecule2d(),  # interactive version of your component
    molecule2d(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()
