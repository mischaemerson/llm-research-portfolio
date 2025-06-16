import os
import re
import unidecode
from tqdm import tqdm

input_path = "data/raw/raw_text.txt"
output_path = "data/cleaned/cleaned_text.txt"

os.makedirs("data/cleaned", exist_ok=True)

def clean_line(text):
    text = unidecode.unidecode(text)  # Remove unicode accents
    text = re.sub(r'\s+', ' ', text)  # Normalize spaces
    text = text.strip()
    return text

with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
    for line in tqdm(infile):
        cleaned = clean_line(line)
        if len(cleaned) >= 10:
            outfile.write(cleaned + "\n")

