import pandas as pd
from detoxify import Detoxify

# Load sample data
df = pd.read_csv("toxicity-benchmarks/test_data.csv")

# Run Detoxify model
model = Detoxify('original')
df['toxicity'] = df['text'].apply(lambda x: model.predict(x)['toxicity'])

# Save results
df.to_csv("toxicity-benchmarks/toxicity_scores.csv", index=False)

print("Toxicity evaluation complete!")

