# MTG Ruling Assistant

A fine-tuned language model for providing Magic: The Gathering comprehensive rule explanations and rulings.

## Overview

This project fine-tunes a GPT-2 model using LoRA (Low-Rank Adaptation) to specialize in Magic: The Gathering comprehensive rules. The model can answer questions about MTG rules, provide detailed explanations, and help players understand complex game mechanics.

## Features

- ✅ **CPU-Compatible**: Runs on CPU-only systems (no GPU required)
- ✅ **Parameter-Efficient**: Uses LoRA for efficient fine-tuning
- ✅ **Cross-Platform**: Works on Windows, macOS, and Linux
- ✅ **Easy Setup**: Simple installation and training process
- ✅ **Specialized Knowledge**: Focused on MTG comprehensive rules

## Requirements

- Python 3.8+
- Windows, macOS, or Linux
- At least 4GB RAM (8GB recommended for training)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd mtg-ruling-assistant
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Dataset

The project uses a custom dataset (`mtg_comprehensive_rules_qwen_finetune.jsonl`) containing:
- **1,162 training examples**
- Instruction-response pairs for MTG rules
- Comprehensive rule explanations
- Example rulings and scenarios

### Dataset Format
Each line in the JSONL file contains:
```json
{
  "instruction": "Explain Magic: The Gathering Comprehensive Rule 100.1.",
  "response": "100.1. These Magic rules apply to any Magic game with two or more players..."
}
```

## Training

### Quick Start
```bash
python main.py
```

### Training Configuration
- **Base Model**: GPT-2 (124M parameters)
- **Fine-tuning Method**: LoRA with rank 16
- **Target Modules**: `c_attn` (attention layers)
- **Training Epochs**: 3
- **Batch Size**: 4
- **Learning Rate**: 2e-4

### Training Output
The training process will:
1. Load and format the dataset
2. Configure LoRA adapters
3. Train the model for 3 epochs
4. Save the fine-tuned model to `./models/fine-tuned-model/`

## Model Architecture

### Base Model: GPT-2
- **Parameters**: 124M
- **Architecture**: Transformer decoder
- **Context Length**: 1024 tokens
- **CPU-Compatible**: Yes

### LoRA Configuration
- **Rank (r)**: 16
- **Alpha**: 32
- **Dropout**: 0.05
- **Target Modules**: `["c_attn"]`

## Usage

After training, the fine-tuned model will be saved in the `./models/fine-tuned-model/` directory. You can load and use it for inference:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("./models/fine-tuned-model")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Generate text
input_text = "### Instruction:\nExplain Magic: The Gathering Comprehensive Rule 100.1.\n\n### Response:\n"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs, max_length=500, do_sample=True)
print(tokenizer.decode(outputs[0]))
```

## Project Structure

```
mtg-ruling-assistant/
├── main.py                    # Training script
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── datasets/                  # Training data
│   └── mtg_comprehensive_rules_qwen_finetune.jsonl
├── models/                    # Saved models (created during training)
│   └── fine-tuned-model/
└── results/                   # Training logs (created during training)
```

## Troubleshooting

### Common Issues

1. **FileNotFoundError**
   - Ensure you're running from the project directory
   - Check that `datasets/mtg_comprehensive_rules_qwen_finetune.jsonl` exists

2. **Memory Issues**
   - Close other applications to free up RAM
   - Consider reducing batch size in `TrainingArguments`

3. **Import Errors**
   - Ensure virtual environment is activated
   - Reinstall dependencies: `pip install -r requirements.txt`

### Performance Tips

- **Faster Training**: Use a smaller model or reduce epochs
- **Better Results**: Increase training epochs or adjust LoRA parameters
- **Memory Efficiency**: Use gradient accumulation if needed

## Dependencies

- `transformers`: Hugging Face transformer models
- `peft`: Parameter-efficient fine-tuning
- `trl`: Transformer reinforcement learning
- `datasets`: Hugging Face datasets library
- `torch`: PyTorch deep learning framework

## License

This project is for educational and personal use. The Magic: The Gathering rules content is based on official comprehensive rules.


## Support

If you encounter issues or have questions:
1. Check the troubleshooting section above
2. Review the training logs in the `results/` directory
3. Open an issue on GitHub

## Future Enhancements

- [ ] Implement web interface for rule queries
- [ ] Expand dataset with card database
- [ ] Experiment with larger base models
- [ ] Add evaluation metrics and validation

## Acknowledgments

- **Hugging Face**: For providing excellent transformer and dataset libraries
- **Magic: The Gathering**: For being an amazing game :) 
- **OpenAI**: For the original GPT-2 model