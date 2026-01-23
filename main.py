from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer
from datasets import Dataset
from pathlib import Path
import json

print("Initializing..")
current_dir = Path(__file__).parent
dataset_path = current_dir / "datasets" / "mtg_comprehensive_rules_qwen_finetune.jsonl"

# Load JSONL file manually
print("Loading dataset from JSONL file...")
with open(dataset_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Parse JSONL data
data_list = []
for line in lines:
    data_list.append(json.loads(line.strip()))

# Convert to Hugging Face Dataset
dataset = Dataset.from_list(data_list)
print(f"Dataset loaded successfully! Found {len(data_list)} examples")

# Format dataset for training - combine instruction and response into text field
def format_dataset(example):
    text = f"### Instruction:\n{example['instruction']}\n\n### Response:\n{example['response']}"
    return {"text": text}

print("Formatting dataset for training...")
dataset = dataset.map(format_dataset)
print("Dataset formatted successfully!")

# 1. Load base model
print("Loading base model..")
model_name = "gpt2"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 2. Configure LoRA
print("Configuring LoRA..")
lora_config = LoraConfig(
    r=16,  # Rank of the update matrices
    lora_alpha=32,
    target_modules=["c_attn"],  # Which layers to adapt
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)

# 3. Prepare your dataset
print("Preparing your dataset..")
# Dataset is already loaded from step 1

# 4. Set training parameters
print("Setting train parameters..")
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    logging_steps=10,
    save_steps=100,
    warmup_steps=100
)

# 5. Train
print("Training the model...")
trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

trainer.train()

# 6. Save the fine-tuned model
print("Saving the new model..")
model_save_path = current_dir / "models" / "fine-tuned-model"
model.save_pretrained(str(model_save_path))
print(f"Model saved in {model_save_path}")
