import pandas as pd
import numpy as np
import rouge_score

from rouge_score import rouge_scorer

scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)

with open("reference_outputs/references.txt") as ref_file, open("generated_outputs/generations.txt") as gen_file:
    references = [line.strip() for line in ref_file]
    generations = [line.strip() for line in gen_file]

scores = [scorer.score(r, g)['rougeL'].fmeasure for r, g in zip(references, generations)]
print(f"Average ROUGE-L: {np.mean(scores):.4f}")

