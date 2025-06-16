import yaml
import os
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, TaskType

# Load config
with open("configs/training_config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Load dataset
dataset = load_dataset(config['train_dataset'], split=config['train_subset'])

# Load tokenizer & model
model_name = config['model_name']
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(model_name)

# Apply LoRA
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=config['lora_r'],
    lora_alpha=config['lora_alpha'],
    lora_dropout=config['lora_dropout'],
    bias="none"
)
model = get_peft_model(model, lora_config)

# Tokenize
def tokenize(batch):
    return tokenizer(batch["instruction"], padding="max_length", truncation=True, max_length=512)

tokenized_dataset = dataset.map(tokenize, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir=config['save_dir'],
    per_device_train_batch_size=config['batch_size'],
    num_train_epochs=config['epochs'],
    logging_steps=10,
    save_steps=50,
    save_total_limit=1,
    fp16=False,
    report_to="none"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset
)

# Train
trainer.train()

# Save final model
trainer.save_model(config['save_dir'])

