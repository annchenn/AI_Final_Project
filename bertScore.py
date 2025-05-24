#請問這道料理的名稱？這道料理需要的原了與烹飪步驟。
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

# 載入中文 BERT 模型和 tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
model = AutoModel.from_pretrained("bert-base-chinese")

# 兩段你要比對的中文句子
sentence1 = "五花肉2000克 洋蔥2顆 紅蔥頭末50克 蒜末50克 五香粉1小匙 醬油1杯 油膏0.5杯 紹興酒4大匙 冰糖50克"
sentence2 = "油膏0.5杯 五香粉1小匙 醬油1杯 五花肉2000克 紅蔥頭末50克 洋蔥2顆 蒜末50克 紹興酒4大匙 冰糖50克 "

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
