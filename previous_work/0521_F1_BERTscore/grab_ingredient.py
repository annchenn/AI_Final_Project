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