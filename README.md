## 要做的事
使用 BLIP 視覺語言模型，透過 fine-tuning 使其能夠識別台灣食物並生成相應的食譜。

## 規劃
自創dataset, 裡面的結構為
```json
{
  "image": "path/to/food_image_1.jpg",
  "questions": [
    {
      "question": "這是什麼食物？",
      "answer": "這是台灣傳統的牛肉麵。"
    },
    {
      "question": "這道菜的食譜是什麼？",
      "answer": "牛肉麵食譜：\n材料：牛腱500g、老薑30g、蔥段50g、辣豆瓣醬20g、番茄1顆、八角1個、花椒10g、紅蔥頭4顆、麵條適量\n步驟：\n1. 牛腱切塊汆燙去血水\n2. 鍋中熱油爆香紅蔥頭、薑、蔥\n3. 加入辣豆瓣醬炒出香氣\n4. 加入牛肉塊拌炒\n5. 加入八角、花椒、番茄\n6. 加入熱水燉煮2小時\n7. 煮麵條，放入碗中，淋上湯和牛肉即可"
    }
  ]
}
```
用這個dataset去fine-tune BLIP讓他可以根據使用者傳入的圖片回答「這是什麼食物」和「這道菜的食譜是什麼」這兩個問題。

## contents in files: 
- dataset.json(): dataset
- FT Example.ipynb: fine-tune method
- BLIP.py: BLIP

接下來可能會試著學爬蟲，去爬網站搜集台灣食物的食譜。

## 小分工：
- 陳璽安、李尹瑄：fine-tune and dataset
- 劉維凡、陳ej：研究評估模型好壞的指標，可以先從李尹瑄傳在群組的paper的指標研究