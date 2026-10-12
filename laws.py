import pandas as pd
from datasets import load_dataset
import json
print("downloading dataset...")

ds = load_dataset("irlspbru/RusLawOD", split="train", streaming=True)

dataset_rows = []
counter = 0

print("🔍 Фильтрую кодексы...")
for row in ds:
    title = row.get('headingIPS', '')
    text_content = row.get('textIPS', '')
    
    if not title or not text_content:
        continue
        
    keywords = ["конституция", "конституции"]
    if any(kw in title.lower() for kw in keywords):
        counter += 1
        
        if counter % 50 == 0:
            print(f" Найдено кодексов: {counter}/1500...")
            
        dialog = {
            "messages": [
                {"role": "user", "content": f"Разъясни положения документа: '{title}'"},
                {"role": "assistant", "content": f"Официальный текст акта:\n\n{text_content[:4000]}"}
            ]
        }
        dataset_rows.append(dialog)
        
        if counter >= 1500:
            break

with open("train_laws.jsonl", "a", encoding="utf-8") as f:
    for row in dataset_rows:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

print(f"Все готово! Создан файл 'train_laws.jsonl'. Найдено статей: {counter}")