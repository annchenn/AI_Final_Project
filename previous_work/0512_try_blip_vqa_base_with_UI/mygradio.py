import os
from PIL import Image
import gradio as gr
from transformers import BlipProcessor, BlipForQuestionAnswering


processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base").to("cuda")


image_folder = 'images'
question_file = 'questions.txt'


question_map = {}
with open(question_file, 'r') as f:
    for line in f:
        filename, question = line.strip().split('|')
        question_map[filename] = question


image_files = sorted(os.listdir(image_folder))

def update_question(selected_image):
    return question_map.get(selected_image, "")

def answer_question(selected_image, question):
    image_path = os.path.join(image_folder, selected_image)
    image = Image.open(image_path).convert("RGB")
    inputs = processor(image, question, return_tensors="pt").to("cuda")
    out = model.generate(**inputs)
    answer = processor.decode(out[0], skip_special_tokens=True)
    return image, answer

with gr.Blocks() as demo:
    
    with gr.Row():
        image_dropdown = gr.Dropdown(choices=image_files, label="choose a file")
        question_box = gr.Textbox(label="question", placeholder="")
    
    submit_btn = gr.Button("GO！")

    image_output = gr.Image(label="selected image")
    answer_output = gr.Textbox(label="answer")


    image_dropdown.change(fn=update_question, inputs=image_dropdown, outputs=question_box)
    submit_btn.click(fn=answer_question, inputs=[image_dropdown, question_box], outputs=[image_output, answer_output])


if __name__ == "__main__":
    demo.launch()
