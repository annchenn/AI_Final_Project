from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

# 載入中文 BERT 模型和 tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
model = AutoModel.from_pretrained("bert-base-chinese")

# 兩段你要比對的中文句子
sentence1 = "準備材料：\n雞蛋打入碗中，加入一點鹽打散。\n番茄洗淨後切成小塊或月牙片狀。\n炒蛋：\n熱鍋倒入適量油，油熱後倒入蛋液，用中火快速翻炒至蛋剛剛凝固（不需炒太老），盛出備用。\n炒番茄：\n再倒一點油（如鍋中已乾），加入番茄翻炒 1~2 分鐘，炒到番茄略為出汁。\n加入少許鹽和糖提味，視情況加一點水讓番茄出汁更順滑。\n合炒：\n將炒好的蛋倒回鍋中，與番茄一起翻炒均勻約 30 秒即可起鍋。"
sentence2 = "先把番茄洗凈，切大塊。\n把雞蛋發打成蛋汁，加入少量清水（約2至3茶匙，視乎蛋的大小而定）拌勻。\n燒熱油鑊，下蛋汁，以大火快炒把蛋煮至約七成熟，備用。\n下番茄炒片刻，加入鹽、水和糖同煮。\n番茄煮到稍稔，加入茄膏和適量生粉水，再將已炒的雞蛋回鑊，快炒至熟透，即成。"

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
