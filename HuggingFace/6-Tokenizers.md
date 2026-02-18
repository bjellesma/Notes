As a reminder, the following steps need to first be done by the tokenizer.

* Normalization (any cleanup of the text that is deemed necessary, such as removing spaces or accents, Unicode normalization, etc.)
* Pre-tokenization (splitting the input into words)
* Running the input through the model (using the pre-tokenized words to produce a sequence of tokens)
* Post-processing (adding the special tokens of the tokenizer, generating the attention mask and token type IDs)

<img width="1799" height="1031" alt="image" src="https://github.com/user-attachments/assets/1258a218-159f-4dcd-86b1-8b470d31496a" />

The tokenizers library has a lot to help out with this.

* normalizers contains all the possible types of Normalizer you can use (complete list here).
* pre_tokenizers contains all the possible types of PreTokenizer you can use (complete list here).
* models contains the various types of Model you can use, like BPE, WordPiece, and Unigram (complete list here).
* trainers contains all the different types of Trainer you can use to train your model on a corpus (one per type of model; complete list here).
* post_processors contains the various types of PostProcessor you can use (complete list here).
* decoders contains the various types of Decoder you can use to decode the outputs of tokenization (complete list here).

Training a tokenizer is different from training a model in that the tokenizer is trained by having a statistical analysis run over the corpus of text to build a vocabulary. There are no gradients or loss functions used when training a tokenizer as there is with training a model. 

Because of this difference, Huggingface has a seperate tokenizers library for tokenizers training.

To avoid loading an entire batch into memory, we can use generators

```python
def get_training_corpus():
    return (
        raw_datasets["train"][i : i + 1000]["whole_func_string"]
        for i in range(0, len(raw_datasets["train"]), 1000)
    )


training_corpus = get_training_corpus()
```

In the code above, we're using a generator expression so we don't need a yield keyword. This is equivalent to

```python
def get_training_corpus():
    dataset = raw_datasets["train"]
    for start_idx in range(0, len(dataset), 1000):
        samples = dataset[start_idx : start_idx + 1000]
        yield samples["whole_func_string"]
```

Now that we have a generator for our corpus, we are ready to train a new tokenizer. The AutoTokenizer library will choose the tokenizer written in python or rust depending on what hardware is available to you.

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

tokenizer = tokenizer.train_new_from_iterator(training_corpus, 52000)
```

To check if you're able to take advantage of the fast tokenizer, use `tokenizer.is_fast`

We can now use something like

```python
example = """class LinearLayer():
    def __init__(self, input_size, output_size):
        self.weight = torch.randn(input_size, output_size)
        self.bias = torch.zeros(output_size)

    def __call__(self, x):
        return x @ self.weights + self.bias
    """
tokenizer.tokenize(example)
```

to show us our tokens

```
['class', 'ĠLinear', 'Layer', '():', 'ĊĠĠĠ', 'Ġdef', 'Ġ__', 'init', '__(', 'self', ',', 'Ġinput', '_', 'size', ',',
 'Ġoutput', '_', 'size', '):', 'ĊĠĠĠĠĠĠĠ', 'Ġself', '.', 'weight', 'Ġ=', 'Ġtorch', '.', 'randn', '(', 'input', '_',
 'size', ',', 'Ġoutput', '_', 'size', ')', 'ĊĠĠĠĠĠĠĠ', 'Ġself', '.', 'bias', 'Ġ=', 'Ġtorch', '.', 'zeros', '(',
 'output', '_', 'size', ')', 'ĊĊĠĠĠ', 'Ġdef', 'Ġ__', 'call', '__(', 'self', ',', 'Ġx', '):', 'ĊĠĠĠĠĠĠĠ',
 'Ġreturn', 'Ġx', 'Ġ@', 'Ġself', '.', 'weights', 'Ġ+', 'Ġself', '.', 'bias', 'ĊĠĠĠĠ']
```

and then save the trained tokenizer

```python
tokenizer.save_pretrained("code-search-net-tokenizer")
```

Now we'll use this model to make predictions

```python
model_checkpoint = "dbmdz/bert-large-cased-finetuned-conll03-english"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForTokenClassification.from_pretrained(model_checkpoint)

example = "My name is Sylvain and I work at Hugging Face in Brooklyn."
inputs = tokenizer(example, return_tensors="pt")
outputs = model(**inputs)
```

Now we use a softmax to convert the output logits to probabilities

```python
import torch

probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)[0].tolist()
predictions = outputs.logits.argmax(dim=-1)[0].tolist()
print(predictions)
```

Finally, we'll use the trained tokenizer along with our predictions

```python
import numpy as np

results = []
inputs_with_offsets = tokenizer(example, return_offsets_mapping=True)
tokens = inputs_with_offsets.tokens()
offsets = inputs_with_offsets["offset_mapping"]

idx = 0
while idx < len(predictions):
    pred = predictions[idx]
    label = model.config.id2label[pred]
    if label != "O":
        # Remove the B- or I-
        label = label[2:]
        start, _ = offsets[idx]

        # Grab all the tokens labeled with I-label
        all_scores = []
        while (
            idx < len(predictions)
            and model.config.id2label[predictions[idx]] == f"I-{label}"
        ):
            all_scores.append(probabilities[idx][pred])
            _, end = offsets[idx]
            idx += 1

        # The score is the mean of all the scores of the tokens in that grouped entity
        score = np.mean(all_scores).item()
        word = example[start:end]
        results.append(
            {
                "entity_group": label,
                "score": score,
                "word": word,
                "start": start,
                "end": end,
            }
        )
    idx += 1

print(results)
```
