from transformers import pipeline

# Load a lightweight model
model = pipeline("text2text-generation", model="google/flan-t5-small", device=-1)

# Define prompts
experiments = [
    {
        "type": "math",
        "basic": "What is 23 + 47?",
        "cot": "Let's solve this step by step: What is 23 + 47?"
    },
    {
        "type": "logic",
        "basic": "If Sarah is taller than Mia, and Mia is taller than Jo, who is tallest?",
        "cot": "Let's reason step by step: If Sarah is taller than Mia, and Mia is taller than Jo, who is tallest?"
    },
    {
        "type": "ethics",
        "basic": "Is it okay to lie to protect someone's feelings?",
        "cot": "Let's think this through step by step: Is it okay to lie to protect someone's feelings?"
    }
]

# Run experiments
for exp in experiments:
    print(f"\n--- {exp['type'].upper()} TASK ---")
    print("Basic Prompt:", exp["basic"])
    print("Output:", model(exp["basic"], max_new_tokens=50)[0]['generated_text'])

    print("COT Prompt:", exp["cot"])
    print("Output:", model(exp["cot"], max_new_tokens=50)[0]['generated_text'])
