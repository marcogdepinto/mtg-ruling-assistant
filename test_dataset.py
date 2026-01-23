from pathlib import Path
import json

print("Testing dataset loading...")

# Get current directory
current_dir = Path('.')
dataset_path = current_dir / 'datasets' / 'mtg_comprehensive_rules_qwen_finetune.jsonl'

print(f"Looking for file at: {dataset_path}")
print(f"File exists: {dataset_path.exists()}")

if dataset_path.exists():
    try:
        with open(dataset_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print(f"Dataset loaded successfully! Found {len(lines)} lines")
        
        if lines:
            # Parse first line to check JSONL format
            first_line = lines[0].strip()
            try:
                data = json.loads(first_line)
                print("First line preview:", data)
            except json.JSONDecodeError:
                print("First line (raw):", first_line[:200])
        else:
            print("File is empty")
    except Exception as e:
        print(f"Error reading file: {e}")
else:
    print("File not found!")