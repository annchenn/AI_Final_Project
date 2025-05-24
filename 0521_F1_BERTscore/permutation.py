import json
# Load data
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return {item['cuisine_id']: item for item in json.load(f)}  #回傳一個dictionary，key是id，內容是料理的dictionary
    
gt_file = 'GroundTruth_BraisedPorkRice.json'
pred_file = 'ModelPrediction_BraisedPorkRice.json'
gt_data = load_json(gt_file)
pred_data = load_json(pred_file)
# print(gt_data)

all_sentence = []

for item in gt_data:
    my_sentence = []
    for ingredient_list in gt_data[item]['ingredients']:
        my_sentence.append(ingredient_list['ingredient'])
                           
    all_sentence.append(my_sentence)

print(all_sentence)

import itertools
different_permu = list(itertools.permutations(all_sentence[0]))
print(different_permu)

my_sentence = []
for line in different_permu:
    str = ""
    for item in line:
        str = str + item
        str = str + " "
    my_sentence.append(str)

print(my_sentence)


#請問這道料理的名稱？這道料理需要的原了與烹飪步驟。
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

# 載入中文 BERT 模型和 tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
model = AutoModel.from_pretrained("bert-base-chinese")

# 兩段你要比對的中文句子
sentence1 = my_sentence[0]
for sentence in my_sentence:
    sentence2 = sentence

    # 將句子轉成 BERT 的輸入格式
    def get_cls_embedding(sentence):
        inputs = tokenizer(sentence, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
        # 抓出 [CLS] 的向量（batch_size=1, seq_len, hidden_size）
        cls_embedding = outputs.last_hidden_state[:, 0, :]  # shape: [1, hidden_size]
        return cls_embedding

    # 分別取得兩句話的 CLS 向量
    embedding1 = get_cls_embedding(sentence1)
    embedding2 = get_cls_embedding(sentence2)

    # 計算餘弦相似度（值域 -1 到 1，越接近 1 越相似）
    similarity = F.cosine_similarity(embedding1, embedding2)
    print(f"相似度: {similarity.item():.4f}")
