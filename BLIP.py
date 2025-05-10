from transformers import BlipProcessor, BlipForQuestionAnswering
from PIL import Image
import requests

# 載入視覺問答模型
processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

# 下載圖片
url = "https://www.green-n-safe.com/uploads/images/thumbs/0007144_%E5%86%B7%E5%87%8D%E7%83%8F%E9%BE%8D%E9%BA%B5-1000.jpeg"
image = Image.open(requests.get(url, stream=True).raw)

# 視覺問答
question = "How many shrimps are there? And list all ingredients in the image"
inputs = processor(image, question, return_tensors="pt")
outputs = model.generate(**inputs)
print(processor.decode(outputs[0], skip_special_tokens=True))