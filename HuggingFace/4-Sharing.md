## Why HuggingFace Models

HuggingFace models are good to use for tasks that need the transformer architecture. For example, for my crossfit dataset predictions are better done with scikit-learn as it's tabular data of integers. HuggingFace would be useful if I want to understand relationships between text like The athlete who lifted the most also ran the fastest

## Sharing a pretrained model

```python
from huggingface_hub import notebook_login

notebook_login()
```

If you execute this in a notebook, you will be prompted to login

In the following example, we'll use the TrainingArguments class that we've created previously using BERT and we'll use the `push_to_hub` param. This will ONLY be uploaded when you call trainer.train()

```python
from transformers import TrainingArguments

training_args = TrainingArguments(
    "bert-finetuned-mrpc", save_strategy="epoch", push_to_hub=True
)
```

You can also call `trainer.push_to_hub()` directly. This will also generate a model card which'll have a summary 

<img width="1553" height="1702" alt="image" src="https://github.com/user-attachments/assets/781ef6b6-db85-423e-9933-349d32df6224" />
