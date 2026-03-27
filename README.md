# 📚 Specialization of Large Language Models for Magic: The Gathering Rules QA

## 🧠 Overview
This repository contains the implementation and experiments for a Master's thesis project focused on adapting Large Language Models (LLMs) to highly structured, rule-based domains. 

We use *Magic: The Gathering* (MTG) as a challenging benchmark due to its:
- Extremely complex rules system
- Large combinatorial state space
- Frequent edge cases and exceptions

The goal is to evaluate whether fine-tuning can improve factual correctness and reasoning in such domains.

---

## 🎯 Objectives
- Evaluate baseline LLM performance on MTG rules QA
- Apply parameter-efficient fine-tuning (LoRA)
- Measure improvements using standard NLP metrics
- Analyze hallucination patterns
- Assess whether metric gains correlate with true correctness

---

## 🏗️ Project Structure
```
├── LLama_Mtg_model_baseline.ipynb     # Baseline model evaluation
├── LLama_MtgModel_fine_tuning.ipynb   # Fine-tuning pipeline
├── thesis.pdf                         # Final thesis document
└── README.md
```

---

## ⚙️ Methodology

### Model
- Base Model: LLaMA 3.1

### Fine-tuning Approach
- Technique: LoRA (Low-Rank Adaptation)
- Framework: HuggingFace Transformers
- Training Type: Supervised fine-tuning

### Dataset
- Domain: Magic: The Gathering rules Q&A
- Format: Question → Answer pairs
- Focus: Rule interpretation and edge cases

---

## 📊 Evaluation Metrics

We evaluate model performance using:

### BLEU
Measures exact n-gram overlap between generated and reference answers.

### ROUGE-L
Measures longest common subsequence similarity.

### BERTScore
Measures semantic similarity using contextual embeddings.

---

## 📈 Results

| Metric      | Baseline | Fine-tuned |
|------------|----------|-----------|
| BLEU       | 0.312    | 0.358     |
| ROUGE-L    | 0.421    | 0.487     |
| BERTScore  | 0.842    | 0.879     |

---

## ⚠️ Key Findings

- Fine-tuning improves all automatic metrics
- Semantic similarity (BERTScore) shows strongest gains
- However, **hallucinations still occur**
- Metric improvements ≠ guaranteed correctness

### Example Issue
The model may produce:
- Plausible but incorrect rule citations
- Confidently wrong reasoning chains

---

## 🧩 Discussion

This highlights a key limitation of current evaluation approaches:

- Metrics reward similarity, not correctness
- Rule-based domains require **logical validity**, not just fluency

This aligns with broader concerns in LLM evaluation:
- Over-reliance on surface-level metrics
- Lack of grounding in formal systems

---

## 🚀 Future Work
- Introduce rule-based verification systems
- Combine symbolic reasoning with LLMs
- Explore retrieval-augmented generation (RAG)
- Use human expert evaluation

---

## 📜 License
This project is for academic purposes.

---

## Cite this work
@mastersthesis{depinto2026mtgllm,
  author       = {Marco Giuseppe De Pinto},
  title        = {Specialization of Large Language Models for Magic: The Gathering Rules Question Answering},
  school       = {University of Bari},
  year         = {2026},
  type         = {Master's Thesis},
  note         = {Project on domain adaptation and evaluation of LLMs in rule-based environments}
}
