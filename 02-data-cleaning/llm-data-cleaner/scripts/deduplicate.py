import os
from tqdm import tqdm

input_path = "data/cleaned/cleaned_text.txt"
output_path = "data/cleaned/deduplicated_text.txt"

seen = set()
deduped = []

with open(input_path, "r", encoding="utf-8") as infile:
    for line in infile:
        line = line.strip()
        if line not in seen:
            seen.add(line)
            deduped.append(line)

with open(output_path, "w", encoding="utf-8") as outfile:
    for line in tqdm(deduped):
        outfile.write(line + "\n")

