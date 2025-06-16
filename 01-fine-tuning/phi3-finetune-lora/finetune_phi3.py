import os
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, TaskType

# Load dataset
dataset = load_dataset("tatsu-lab/alpaca", split="train[:1000]")

# Load tokenizer and model
model_name = "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Pad token fix for causal models
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(model_name)

# Apply LoRA configuration
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,
    lora_alpha=32,
    lora_dropout=0.1,
    bias="none"
)

model = get_peft_model(model, lora_config)

# Tokenize dataset
def tokenize(batch):
    return tokenizer(batch["instruction"], padding="max_length", truncation=True, max_length=512)

tokenized_dataset = dataset.map(tokenize, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=2,
    num_train_epochs=1,
    logging_steps=10,
    save_steps=50,
    save_total_limit=1,
    fp16=False,
    report_to="none"
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset
)

# Train model
trainer.train()

# Save model (final fix added here)
save_path = os.path.join(os.getcwd(), "results", "final_model")
os.makedirs(save_path, exist_ok=True)
trainer.save_model(save_path)

