# Mischa Emerson — LLM Research Engineer Portfolio

This repository showcases a modular, end-to-end LLM system that simulates real-world research workflows — from fine-tuning and evaluation to safety, alignment, and deployment. It brings together multiple components of applied LLM engineering, including:

- ✅ LLM fine-tuning and parameter-efficient training (LoRA, PEFT)
- ✅ Data preparation and cleaning for model training
- ✅ Evaluation frameworks for LLM output quality (BLEU, ROUGE, Exact Match)
- ✅ Responsible AI benchmarking (toxicity, bias, safety)
- ✅ Distributed multi-GPU training experiments (Accelerate, DDP)
- ✅ Efficient inference serving (FastAPI API deployment)
- ✅ RLHF simulation framework (Phase 07)
- ✅ Prompt engineering & reasoning experiments (Phase 08)
- ✅ Live deployment prep (Phase 09 Hyperpolish)

---

## 📂 Project Directory

| Phase | Project | Status |
|---|---|---|
| 00 | Foundations & Hugging Face Prep | ✅ Complete |
| 01 | Fine-Tuning Small LLMs (Phi-2, TinyLlama, Mistral) | ✅ Complete |
| 02 | Data Cleaning Pipelines for LLM Datasets | ✅ Complete |
| 03 | Evaluation Frameworks (BLEU, ROUGE, EM) | ✅ Complete |
| 04 | Bias & Responsible AI Testing (toxicity, bias) | ✅ Complete |
| 05 | Distributed Training with DDP & Accelerate | ✅ Complete |
| 06 | Inference Serving & Deployment (FastAPI, Transformers) | ✅ Complete |
| 07 | RLHF Simulation Prep | ✅ Complete |
| 08 | Prompt Engineering & COT Experiments | ✅ Complete |
| 09 | Hyperpolish Pack (Demo Hosting, Docker, Deployment) | 🔜 Launching |

---

## 🔧 Phase Highlights

### Phase 01 – Fine-Tuning with LoRA + PEFT

This phase focused on fine-tuning small LLMs using Hugging Face PEFT with LoRA adapters. I used `finetune_ddp.py` to enable distributed multi-GPU training and structured all training parameters with YAML-based config files. I successfully fine-tuned Phi-2 and TinyLlama models and validated that my training system was modular, reproducible, and compatible with Accelerate and DDP workflows.

---

### Phase 03 – Evaluation Frameworks for LLM Output

I implemented automated evaluation scripts to measure the quality of generated outputs across BLEU, ROUGE-L, and Exact Match metrics. These evaluations were designed to run post-training on synthetic datasets to assess baseline generation behavior. Output scores were used to benchmark the effects of different prompt styles and model variants.

---

### Phase 04 – Responsible AI + Bias Testing

This phase explored LLM behavior through simulated bias and toxicity detection using Detoxify and sentence-based bias checks. Although Detoxify was not fully compatible with Python 3.13, I documented a future switch to Python 3.10 for production testing. This work reinforced the importance of safety tooling in any deployed LLM system.

---

### Phase 06 – Inference API + Live Gradio Demo

I deployed a FastAPI-based inference server running locally with Uvicorn, then containerized the application and launched it on Hugging Face Spaces. The app included a Gradio-style interface with user prompt input and model response. This demonstrated full-stack deployment skills from local testing to cloud-hosted inference.

---

### Phase 07 – RLHF Simulation Prep

This phase simulates the data preparation process used in RLHF pipelines. I created a structured JSONL dataset of prompt/completion pairs with human preference labels, then wrote a script to convert it into a binary-labeled format suitable for training reward models. This simulates the "pre-reward model" phase of modern alignment pipelines.

**Files Created:**
- `rlhf_prefs.jsonl` – raw preferences  
- `prep_rlhf_dataset.py` – Python script to convert to reward data  
- `rlhf_reward_data.csv` – labeled output for supervised reward training

Run the script:

```bash
python3 prep_rlhf_dataset.py

---

Preview of output dataset:

| prompt                         | completion      | label |
|--------------------------------|-----------------|-------|
| What is the capital of France? | Paris           | 1     |
| What is the capital of France? | London          | 0     |
| What is 2 + 2?                 | 4               | 1     |
| What is 2 + 2?                 | 22              | 0     |
| Who wrote 1984?                | George Orwell   | 1     |
| Who wrote 1984?                | J.K. Rowling    | 0     |

---

Phase 08 – Prompt Engineering & CoT Experiments
This phase compared basic prompt formats to Chain-of-Thought (CoT) prompting across math, logic, and ethics tasks. I structured experiments in code, tested model outputs, and recorded how CoT improved performance — especially for reasoning-based inputs. This reinforced the value of prompt design as a low-cost method to improve output quality.

---

## 🧠 Reflection

This project brought together everything I’ve learned across cloud engineering, scripting, AI deployment, and LLM evaluation. It wasn’t easy — I hit VRAM walls, package conflicts, and had to reroute around `sentencepiece` errors — but working through those obstacles gave me the confidence to debug and deploy like a real-world LLM engineer.

This system also showed me how much thoughtful design matters: config-driven development, reproducibility, and safe fallback behavior made the system manageable even when complex.

Simulating RLHF preparation gave me practical insight into how feedback-based human preferences can be encoded into a structured training format. Even without full PPO training, designing the data pipeline and reward labeling logic helped me better understand how these components fit into modern GenAI workflows. It reinforced the importance of data engineering as the foundation for safe and scalable AI development.

In Phase 08, I was surprised by how much difference prompt structure alone could make. Chain-of-Thought (CoT) formatting led to noticeably better answers — especially for logic and math tasks — without any model fine-tuning. It showed me how prompt engineering can be used as a lightweight but powerful tool to influence model behavior, and how important it is to test prompts as rigorously as we test code. That realization shifted how I think about LLM usability and explainability.

I’m excited to improve this with instruction-tuned models, better eval datasets, and possibly full RLHF or quantization phases in the future.

---

## 🔗 Connect

- [LinkedIn Profile](https://www.linkedin.com/in/mischaemerson)
- [Portfolio: Mischa’s Notion](https://merciful-ginger-7b6.notion.site/Mischa-Emerson-Engeering-Portfolio-1ff8807f8f868051bedac07eae351154)

- [Hugging Face Profile](mischaemerson)

---

Actively Building. Actively Learning. Open to collaboration. 

