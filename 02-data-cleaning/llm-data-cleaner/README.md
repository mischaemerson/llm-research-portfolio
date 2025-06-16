# LLM Data Cleaning Pipeline

This project prepares raw text datasets for LLM pre-training and fine-tuning by cleaning, normalizing, deduplicating, and exporting in JSONL format.

## Pipeline Steps

1. Text normalization & cleaning
2. Deduplication
3. Filtering (length, language, offensive content)
4. Export to train-ready JSONL format

## Usage

- Place raw text files into `data/raw/`
- Run each script in order:
  - `clean_text.py`
  - `deduplicate.py`
  - `build_dataset.py`
- Cleaned datasets saved to `data/cleaned/`

## Dependencies

- Python 3.10+
- tqdm
- pandas
- numpy
- unidecode
- langdetect

## Future Work

- Add profanity filtering
- Add language detection filters
- Add parallel processing for large datasets

