import json
import os
from tqdm import tqdm

input_path = "data/cleaned/deduplicated_text.txt"
output_path = "data/cleaned/train_dataset.jsonl"

with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
    for line in tqdm(infile):
        sample = {
            "instruction": "Please continue writing:",
            "input": "",
            "output": line.strip()
        }
        outfile.write(json.dumps(sample) + "\n")

