import json
import csv
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return {item['cuisine_id']: item for item in json.load(f)}

gt_file = 'ground_truth.json'
gpt_file = 'response_gpt.json'
gemini_file = 'response_gemini.json'
claude_file = 'response_claude.json'

gt_data = load_json(gt_file)
gpt_data = load_json(gpt_file)
gemini_data = load_json(gemini_file)
claude_data = load_json(claude_file)

print(gt_data)
print(gpt_data)
print(gemini_data)

def json_csv(name, data):

    with open (f'{name}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for item in gt_data:
            writer.writerow([data[item]['cuisine_id']])
            writer.writerow([data[item]['cuisine_name']])
            for ingredient_list in data[item]['ingredients']:
                writer.writerow([ingredient_list['ingredient']])
            writer.writerow([' '])

json_csv('gt', gt_data)
json_csv('gpt', gpt_data)
json_csv('gemini', gemini_data)
json_csv('claude', claude_data)

