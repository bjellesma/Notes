You'll want to train a new tokenizer when your dataset is different from the one used by an existing pretrained model, and you want to pretrain a new model

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

# Fast Tokenizer in the QA cycle

As a reminder, we can use the following code as an example to do question answering.

```python
from transformers import pipeline

question_answerer = pipeline("question-answering")
context = """
🤗 Transformers is backed by the three most popular deep learning libraries — Jax, PyTorch, and TensorFlow — with a seamless integration
between them. It's straightforward to train your models with one before loading them for inference with the other.
"""
question = "Which deep learning libraries back 🤗 Transformers?"
question_answerer(question=question, context=context)
```

We get an answer like this

```python
{'score': 0.97773,
 'start': 78,
 'end': 105,
 'answer': 'Jax, PyTorch and TensorFlow'}
```

How this works under the hood is that we have logits for the start of the answer token and logits for the end of the answer token.

As usual, we use the softmax activation function to convert our logits to probabilities.

```python
start_probabilities = torch.nn.functional.softmax(start_logits, dim=-1)
end_probabilities = torch.nn.functional.softmax(end_logits, dim=-1)
```

# Normalization and Pre Tokenization

As a reminder, the following steps need to first be done by the tokenizer.

* Normalization (any cleanup of the text that is deemed necessary, such as removing spaces or accents, Unicode normalization, etc.)
    * The `normalizer` attribute has a `normal_str()` method to do things like remove whitespace and accents.  
* Pre-tokenization (splitting the input into words)
    * Typically just simply done on whitespace and punctuation
* Running the input through the model (using the pre-tokenized words to produce a sequence of tokens). The goal of this step is to get a vocabulary of tokens.
    * Note that this is the tokenizer model (e.g., BPE, WordPiece, Unigram) — not the language model itself
    * Descriptions of the algorithms are summerized below
* Post-processing (adding the special tokens of the tokenizer, generating the attention mask and token type IDs)
    * The last step in the tokenization pipeline is post-processing. We need to add the [CLS] token at the beginning and the [SEP] token at the end (or after each sentence, if we have a pair of sentences). We will use a TemplateProcessor for this, but first we need to know the IDs of the [CLS] and [SEP] tokens in the vocabulary:    

<img width="1799" height="1031" alt="image" src="https://github.com/user-attachments/assets/1258a218-159f-4dcd-86b1-8b470d31496a" />

## Byte Pair Encoding (BPE)

BPE (Byte Pair Encoding) starts with a base vocabulary of individual characters, then iteratively merges the most frequently occurring pairs of tokens together until it reaches a target vocabulary size.. It's first widely available usage was in GPT but it is still widely used in models like GPT3/4 and Llama.

## Wordpiece

Mainly used by google in BERT

WordPiece is similar in structure but instead of picking the most frequent pair, it picks the pair that maximizes the likelihood of the training data when merged. Practically this means it asks "does merging these two tokens make the overall language model better?" rather than just "which pair appears most often?"

A concrete way to think about it: WordPiece scores a candidate merge as:

frequency of AB / (frequency of A × frequency of B)

The practical difference is subtle but WordPiece tends to produce slightly more linguistically meaningful subwords. It's also why BERT's tokenizer marks subwords with a ## prefix (e.g. token + ##ization) rather than BPE's end-of-word marker approach.

## Unigram

Unigram takes a fundamentally different approach — instead of starting small and merging up like BPE and WordPiece, it starts big and prunes down.
The process:

1. Start with a massive vocabulary — every possible subword and character in the corpus
2. Train a unigram language model over that vocabulary (assigns a probability to every token)
3. For each token in the vocabulary, calculate how much the overall loss would increase if you removed it
4. Remove the bottom X% of tokens that hurt the least when removed
5. Repeat until you hit your target vocabulary size

### The key conceptual difference

BPE and WordPiece are deterministic — given a word, there's only one way to tokenize it based on the merge rules. Unigram is probabilistic — it can tokenize a word multiple ways and assigns a probability to each segmentation. It picks the most likely one, but it actually knows about alternatives.
For example "low" might be tokenizable as l + ow, or lo + w, or low — unigram scores all of them and picks the best.

# Building a tokenizer

The tokenizers library has a lot to help out with this.

* normalizers contains all the possible types of Normalizer you can use (complete list here).
      
* pre_tokenizers contains all the possible types of PreTokenizer you can use (complete list here).
* models contains the various types of Model you can use, like BPE, WordPiece, and Unigram (complete list here).
* trainers contains all the different types of Trainer you can use to train your model on a corpus (one per type of model; complete list here).
* post_processors contains the various types of PostProcessor you can use (complete list here).
* decoders contains the various types of Decoder you can use to decode the outputs of tokenization (complete list here).

We'll first build our corpus

```python
from datasets import load_dataset

dataset = load_dataset("wikitext", name="wikitext-2-raw-v1", split="train")


def get_training_corpus():
    for i in range(0, len(dataset), 1000):
        yield dataset[i : i + 1000]["text"]
```

For this example, we'll create a tokenizer with a wordpiece model. Note that unk_token is needed when we encounter characters that the model hasn't seen before.

```
from tokenizers import (
    decoders,
    models,
    normalizers,
    pre_tokenizers,
    processors,
    trainers,
    Tokenizer,
)

tokenizer = Tokenizer(models.WordPiece(unk_token="[UNK]"))
```

```python
# 1. Normalization
tokenizer.normalizer = normalizers.BertNormalizer(lowercase=True)
# 2. Pre Tokenization
tokenizer.pre_tokenizer = pre_tokenizers.BertPreTokenizer()
# 3. Model (using wordpiece in this example)
special_tokens = ["[UNK]", "[PAD]", "[CLS]", "[SEP]", "[MASK]"]
trainer = trainers.WordPieceTrainer(vocab_size=25000, special_tokens=special_tokens)
tokenizer.train_from_iterator(get_training_corpus(), trainer=trainer)
# 4. Post processing
cls_token_id = tokenizer.token_to_id("[CLS]")
sep_token_id = tokenizer.token_to_id("[SEP]")
tokenizer.post_processor = processors.TemplateProcessing(
    single=f"[CLS]:0 $A:0 [SEP]:0",
    pair=f"[CLS]:0 $A:0 [SEP]:0 $B:1 [SEP]:1",
    special_tokens=[("[CLS]", cls_token_id), ("[SEP]", sep_token_id)],
)
encoding = tokenizer.encode("Let's test this tokenizer...", "on a pair of sentences.")
print(encoding.tokens)
print(encoding.type_ids)
```

Now we get these tokens

```
['[CLS]', 'let', "'", 's', 'test', 'this', 'tok', '##eni', '##zer', '...', '[SEP]', 'on', 'a', 'pair', 'of', 'sentences', '.', '[SEP]']
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
```

Now we can use this tokenizer to decode

```python
tokenizer.decoder = decoders.WordPiece(prefix="##")
tokenizer.decode(encoding.ids)
```

```
"let's test this tokenizer... on a pair of sentences."
```
