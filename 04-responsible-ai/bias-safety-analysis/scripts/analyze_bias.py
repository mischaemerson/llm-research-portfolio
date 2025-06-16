import pandas as pd
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

df = pd.read_csv("bias-benchmarks/bias_test_data.csv")

# Compare pairwise bias test prompts
similarities = []
for i, row in df.iterrows():
    emb1 = model.encode(row['prompt_a'], convert_to_tensor=True)
    emb2 = model.encode(row['prompt_b'], convert_to_tensor=True)
    sim = util.cos_sim(emb1, emb2).item()
    similarities.append(sim)

df['similarity'] = similarities
df.to_csv("bias-benchmarks/bias_scores.csv", index=False)

print("Bias evaluation complete!")

