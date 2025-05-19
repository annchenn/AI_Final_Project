import os 
from PIL import Image
import cv2
from transformers import BlipProcessor, BlipForQuestionAnswering

processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base").to("cuda")

image_folder = 'images'

with open('questions.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    filename, question = line.strip().split('|')
    image_path = os.path.join(image_folder, filename)

    image = Image.open(image_path).convert('RGB')

    inputs = processor(image, question, return_tensors='pt').to("cuda")
    out = model.generate(**inputs)
    answer = processor.decode(out[0], skip_special_tokens = True)


    print(f"ans: {answer}\n")
