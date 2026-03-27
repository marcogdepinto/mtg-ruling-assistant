# 📚 Specialization of LLMs for Magic: The Gathering Rules QA

## 🧠 Overview
This project investigates the domain adaptation of Large Language Models (LLMs) for question answering in structured rule-based environments, using Magic: The Gathering as a case study.

## 🎯 Objectives
- Evaluate LLM specialization in formal domains  
- Compare baseline vs fine-tuned performance  
- Analyze hallucinations and rule correctness  

## 🏗️ Project Structure
- LLama_Mtg_model_baseline.ipynb  
- LLama_MtgModel_fine_tuning.ipynb  
- thesis.pdf  

## ⚙️ Methodology
- Model: LLaMA 3.1  
- Fine-tuning: LoRA  
- Dataset: MTG QA dataset  

## 📊 Results
BLEU: 0.312 → 0.358  
ROUGE-L: 0.421 → 0.487  
BERTScore: 0.842 → 0.879  

## ⚠️ Key Insight
Metric improvements do not guarantee correctness. The model still hallucinates rule references.

## 👤 Author
Marco Giuseppe De Pinto
