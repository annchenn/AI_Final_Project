from bert_score import score
import torch

sentence1 = "我喜歡貓咪"
sentence2 = "我也很喜歡貓咪"
candidate_sentences = [sentence2] 
reference_sentences = [sentence1] 

# lang='zh' 指定中文语言，会自动选择适合中文的预训练模型（如bert-base-chinese）
# 你也可以明确指定 model_type="bert-base-chinese"
P, R, F1 = score(candidate_sentences, reference_sentences, lang='zh', verbose=True)

print(f"Precision: {P.item():.4f}")
print(f"Recall: {R.item():.4f}")
print(f"F1 Score: {F1.item():.4f}")

# P, R, F1 = score(candidate_sentences, reference_sentences, lang='zh', verbose=True)
# print(f"Precision: {P}")
# print(f"Recall: {R}")
# print(f"F1 Score: {F1}")