# Towards Better Evaluation: A Multidimensional Framework for Assessing LLM-Generated Recipes
## Introduction
This repository documents our journey for the AI final project.
While our final research direction focuses on evaluating LLM-generated recipes beyond traditional text metrics, the entire process included multiple explorations, trial and errors -- all of which are preserved here as part of our learning record.

## Project Overview
In this project, we collected recipes for three popular Taiwanese dishes: braised pork rice, Taiwanese fried chicken, and stinky tofu from the iCook website. For each dish, we curated five recipe samples, and extracted their representative images.<br><br>
These images were then send to three large language models: ChatGPT, Gemini, and Claude with the prompts "根據圖片，請問這道料理的名稱？請列出這道料理需要的原料與烹飪步驟。" to generate full recipes (ingredients + instructions).<br><br>
To evaluate the accuracy and quality of the generated recipes, we applied both traditional and custom-designed evaluation methods:<br>
- **Text similarity metrics:** ROUGE, bert-base-chinese, and BERTScore.

- **Our proposed metric — Recipe-F1:** Inspired by the F1-score, this metric measures the overlap between generated and reference recipe content, considering both precision and recall.

- **User Study:** We designed a form-based survey to gather user feedback with the LLM-generated recipes.

This multidimensional evaluation approach helps us better understand the real-world applicability and limitations of recipe generation by LLMs.

## Early Exploration

