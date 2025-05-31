import requests
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering

processor = BlipProcessor.from_pretrained("riteshkr/blip_base_vqa_finetuned")
model = BlipForQuestionAnswering.from_pretrained("riteshkr/blip_base_vqa_finetuned").to("cuda")

img_url = 'https://mrbug.tw/wp-content/uploads/2024/08/IMG_20240814_141221.jpg' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

question = "Describe the name of the dish in the photo."
inputs = processor(raw_image, question, return_tensors="pt").to("cuda")

out = model.generate(**inputs)
print(processor.decode(out[0], skip_special_tokens=True))

