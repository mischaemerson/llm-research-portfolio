# LLM Evaluation Lab

This project evaluates fine-tuned LLM models using common NLP metrics:

- BLEU (accuracy of token match)
- ROUGE (overlap of longer phrases)
- Exact Match (strict full-match)
- Human-readable examples

## Workflow

1. Place ground-truth reference outputs in `reference_outputs/`
2. Place model-generated outputs in `generated_outputs/`
3. Run evaluation scripts

## Dependencies

- sacrebleu
- rouge-score
- pandas
- numpy
- tqdm

