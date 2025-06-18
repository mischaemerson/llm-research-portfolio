import json
import pandas as pd

with open("rlhf_prefs.jsonl", "r") as f:
    data = [json.loads(line) for line in f]

rows = []
for entry in data:
    for i in [1, 2]:
        label = 1 if entry["preferred"] == i else 0
        rows.append({
            "prompt": entry["prompt"],
            "completion": entry[f"completion_{i}"],
            "label": label
        })

df = pd.DataFrame(rows)
df.to_csv("rlhf_reward_data.csv", index=False)
print("Saved rlhf_reward_data.csv with", len(df), "rows")
