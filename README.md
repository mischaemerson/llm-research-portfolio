# Mischa Emerson — LLM Research Engineer Portfolio

Welcome to my applied AI research engineering portfolio. This repository contains my growing body of hands-on work focused on Large Language Model (LLM) systems, covering:

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
| 08 | Prompt Engineering & COT Experiments | 🔨 In Progress |
| 09 | Hyperpolish Pack (Demo Hosting, Docker, Deployment) | 🔜 Launching |

---

## 🔧 Phase 07 Highlight – RLHF Simulation Prep

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

This step taught me how feedback data is encoded into usable labels and how reward modeling fits into real-world GenAI workflows.

---

## 🚀 Summary

This portfolio was designed to demonstrate full-stack LLM research engineering capabilities in preparation for roles including:

- Research Engineer @ Meta AI (FAIR)
- Applied LLM Engineer @ OpenAI / Anthropic / Google DeepMind / Hugging Face
- Responsible AI Engineer
- Applied AI Researcher

All projects are fully reproducible and documented with real-world industry pipelines.

---

## 🔗 Connect

- [LinkedIn Profile](https://www.linkedin.com/in/mischaemerson)
- [Portfolio: Mischa’s Notion](https://merciful-ginger-7b6.notion.site/Mischa-Emerson-Engeering-Portfolio-1ff8807f8f868051bedac07eae351154)

- [Hugging Face Profile](mischaemerson)

---

Actively Building. Actively Learning. Open to collaboration. 🚀

