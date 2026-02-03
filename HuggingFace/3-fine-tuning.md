### Processesing the Data

```python
import torch
from torch.optim import AdamW
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Same as before
checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
sequences = [
    "I've been waiting for a HuggingFace course my whole life.",
    "This course is amazing!",
]
batch = tokenizer(sequences, padding=True, truncation=True, return_tensors="pt")

# This is new
batch["labels"] = torch.tensor([1, 1])

optimizer = AdamW(model.parameters())
loss = model(**batch).loss
loss.backward()
optimizer.step()
```

### Preprocessing

Let's tokenize the two sentences as we have before

```python
checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
inputs = tokenizer("This is the first sentence.", "This is the second one.")
```

You'll get output like the following

```
{ 
  'input_ids': [101, 2023, 2003, 1996, 2034, 6251, 1012, 102, 2023, 2003, 1996, 2117, 2028, 1012, 102],
  'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
  'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}
```

The **token_type_ids** tells the model which is the first sentence and which is the second. As a reminder, we sometimes need to have the sentences be the same length and so we add padding. The **attention mask** will tell the model what's actual content vs what's padding.

So if we have 

```python
inputs = tokenizer(
    ["Short sentence.", "This is a much longer sentence."],
    padding=True
)
print(inputs)
```

We'll get 

```
[[101, 2460, 6251, 1012, 102, 0, 0, 0, 0], [101, 2023, 2003, 1037, 2172, 2936, 6251, 1012, 102]], 'token_type_ids': [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], 'attention_mask': [[1, 1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1]]}
```

The number of tokens is also different that the number of words because the model will add special tokens, BERT uses **wordpiece tokenization** to break into smaller words, and punctuation will have its own token.

```
[CLS] Short sentence . [SEP]
 101  2460   6251  1012  102
```
