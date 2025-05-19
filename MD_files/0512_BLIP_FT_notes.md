# Beforehand
## BLIP
Bootstrapping Language-Image Pretraining
bootstrap是指引導程式
是由 Salesforce Research 所開發的多模態預訓練模型
{%preview https://github.com/salesforce/BLIP %}

## CLIP
Contrastive Language-Image Pre-Training
是由 OpenAI 開發的模型
{%preview https://github.com/openai/CLIP %}


CLIP 在 2021 年由 OpenAI 發表，開啟了多模態 AI 模型的新方向，之後也促使許多研究團隊（如 Salesforce、Meta、Google）相繼開發類似的跨模態模型（如 BLIP、Flamingo、PaLI 等）
:::success
剛剛查到的是，CLIP2021、BLIP2022、BLIP2 2023
:::

## 關於BLIP更詳細的資訊
目前看起來他是最符合我們final project要做的事情，也就根據圖像+指令生成任務，適合描述圖像、生成食譜等。

### Hugging face 上和BLIP有關的模型
{%preview https://huggingface.co/collections/Salesforce/blip-models-65242f40f1491fbf6a9e9472 %}

上次跟璽安跑的是 Salesforce/blip-vqa-base，也就是目前我們github repository上的，但是我們測試的結果發現他蠻笨的，問了chatGPT後，覺得可能要放棄他，改用blip二代好了。
![image](https://hackmd.io/_uploads/B1tf-SJbxl.png)
![image](https://hackmd.io/_uploads/HJ_IZHkbll.png)

#### 改用BLIP二代遇到的問題
電腦做不到，不同等級的模型會需要不同的參數量，有些模型的參數量會直接寫在模型名稱，像是==blip2-opt-2.7b==
| 模型               | 參數量    | 推論建議 GPU RAM（float32） |
| ---------------- | ------ | --------------------- |
| `bert-base`      | \~110M | 1–2 GB                |
| `blip-base`      | \~220M | 2–3 GB                |
| `blip2-opt-2.7b` | 2.7B   | 8–12 GB               |
| `opt-6.7b`       | 6.7B   | 16–24 GB              |
| `flan-t5-xl`     | 3B     | 10–12 GB              |
| `gpt2`           | 124M   | <1 GB                 |

看看這個表! 想用flan-t5-xl根本不可能挖。

# 回到 BLIP 的 Fine-tuning

