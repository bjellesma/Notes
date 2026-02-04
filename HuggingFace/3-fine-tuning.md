### Processesing the Data

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

This can be checked by converting the inputs back

```python
tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
```

```
['[CLS]',
 'short',
 'sentence',
 '.',
 '[SEP]',
 '[PAD]',
 '[PAD]',
 '[PAD]',
 '[PAD]']
```

### Dynamic Padding

Dynamic Padding is used when processing batches of sentences by only padding to the max length in each batch. This reduces computational overhead.

```python
def tokenize_function(example):
    return tokenizer(example["sentence1"], example["sentence2"], truncation=True)


tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
```

## Trainer API

<img width="3482" height="2022" alt="image" src="https://github.com/user-attachments/assets/b798e9f8-b394-4af7-8d6b-e1115a98c709" />

The first step is to make a TrainingArguments class to contain all of the hyperparams. We'll use the defaults.

```python
from transformers import TrainingArguments

training_args = TrainingArguments("test-trainer")
```

The second step is to define the model that we want to use

```python
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)
```

Finally we'll define our trainer

```python
from transformers import Trainer

trainer = Trainer(
    model,
    training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    processing_class=tokenizer,
)
```

Finally we'll train the model

```python
trainer.train()
```

This will start the fine tuning process and report the training loss every 500 steps.

💡 Key Takeaways:

The Trainer API provides a high-level interface that handles most training complexity
* Use processing_class to specify your tokenizer for proper data handling
* TrainingArguments controls all aspects of training: learning rate, batch size, evaluation strategy, and optimizations
* compute_metrics enables custom evaluation metrics beyond just training loss. It computes metrics like accuracy and F1
* Modern features like mixed precision (fp16=True) and gradient accumulation can significantly improve training efficiency. Gradient accumulation accumulates gradients over multiple batches before updating, enabled with gradient_accumulation_steps

[notebook](https://colab.research.google.com/drive/1Z1zzuv61PVLJeCvjr9kEvZep2Tzml2bB#scrollTo=wn8NLIYrCFys)

### A full training loop

```python
from datasets import load_dataset
from transformers import AutoTokenizer, DataCollatorWithPadding

raw_datasets = load_dataset("glue", "mrpc")
checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)


def tokenize_function(example):
    return tokenizer(example["sentence1"], example["sentence2"], truncation=True)


tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
```

Before beginning our training loop, we need to do some postprocessing on our dataset like remove some columns that are unexpected.

```python
tokenized_datasets = tokenized_datasets.remove_columns(["sentence1", "sentence2", "idx"])
tokenized_datasets = tokenized_datasets.rename_column("label", "labels")
tokenized_datasets.set_format("torch")
tokenized_datasets["train"].column_names
```

Notice that we set format to torch which means that we're converting numpy arrays to tensors.

We'll use AdamW for our optimizer which is the adam optimizer with support for weight decay.

```python
from torch.optim import AdamW

optimizer = AdamW(model.parameters(), lr=5e-5)
```

We'll use a learning rate scheduler which will adjust our learning rate after each epoch

```python
from transformers import get_scheduler

num_epochs = 3
num_training_steps = num_epochs * len(train_dataloader)
lr_scheduler = get_scheduler(
    "linear",
    optimizer=optimizer,
    num_warmup_steps=0,
    num_training_steps=num_training_steps,
)
```

Now before we actually use the training loop, we'll want to define the device. If we have access to a GPU, training takes a couple minutes rather than hours on a CPU
```
import torch

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
model.to(device)
device
```

Now we can actually do our training loop

```python
from tqdm.auto import tqdm

progress_bar = tqdm(range(num_training_steps))

model.train()
for epoch in range(num_epochs):
    for batch in train_dataloader:
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()

        optimizer.step()
        lr_scheduler.step()
        optimizer.zero_grad()
        progress_bar.update(1)
```

In a training loop, the correct order of operations is Forward pass → Backward pass → Optimizer step → Scheduler step → Zero gradients

## Learning Curves

Learning curves are visual representations of your model’s performance metrics over time during training. The two most important curves to monitor are:

**Loss curves** Show how the model’s error (loss) changes over training steps or epochs

<img width="1479" height="996" alt="image" src="https://github.com/user-attachments/assets/8d1f7558-bd86-4432-a5b7-de81a4732145" />

**Accuracy curves** Show the percentage of correct predictions over training steps or epochs

<img width="1575" height="1193" alt="image" src="https://github.com/user-attachments/assets/b01aa560-72eb-4a6e-ba62-3243b2fb1613" />

**Overfitting** is when the model performs well on training data but poorly on unseen validation data. Characterized when training loss decreases but validation loss starts increasing

<img width="1558" height="1242" alt="image" src="https://github.com/user-attachments/assets/ccfe7577-1e4f-4644-8d92-2a74d996d80a" />

**Underfitting** A common sign is when both training and validation performance are poor and plateau early.

<img width="1595" height="1511" alt="image" src="https://github.com/user-attachments/assets/fddaa9f9-e3c9-4199-87b7-fcbd09eb52e6" />

**Eratic Learning Curves**

<img width="1643" height="1388" alt="image" src="https://github.com/user-attachments/assets/00beb074-5e88-4161-9810-b2060722156b" />

Consider early stopping when validation performance stops improving or starts degrading
