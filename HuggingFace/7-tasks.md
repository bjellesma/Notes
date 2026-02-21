# Token Classification

This is generic task for attributing a label to each token in a sentence. This can be used for tasks such as

* Named entity recognition (NER): Find the entities (such as persons, locations, or organizations) in a sentence. This can be formulated as attributing a label to each token by having one class per entity and one class for “no entity.”
* Part-of-speech tagging (POS): Mark each word in a sentence as corresponding to a particular part of speech (such as noun, verb, adjective, etc.).

## NER

A named entity recognition dataset may give data like 

```
['O', 'B-PER', 'I-PER', 'B-ORG', 'I-ORG', 'B-LOC', 'I-LOC', 'B-MISC', 'I-MISC']
```

* 0 means the word doesn’t correspond to any entity.
* B-PER/I-PER means the word corresponds to the beginning of/is inside a person entity.
* B-ORG/I-ORG means the word corresponds to the beginning of/is inside an organization entity.
* B-LOC/I-LOC means the word corresponds to the beginning of/is inside a location entity.
* B-MISC/I-MISC means the word corresponds to the beginning of/is inside a miscellaneous entity.

# Fine tuning a masked language model

For most tasks, you can just use a pretrained model from the hugging face hub and fine tune it directly on your data for your use case. However there are instances where you want to first fine tune the language models on your data like if your dataset is a contract and therefore will contain rare tokens. This process of fine-tuning a pretrained language model on in-domain data is usually called **domain adaptation**. A deep dive is available [here](https://huggingface.co/learn/llm-course/chapter7/3).

Perplexity is often a metric that is used to score a language model. Perplexity measures how "surprised" or uncertain a model is when it sees text. Lower perplexity = the model found the text more predictable = better. A model assigns a probability to every possible next token at each step. If the model is confident and correct, those probabilities are high for the right tokens. Perplexity averages this uncertainty across an entire sequence — it's essentially asking "on average, how many equally likely choices did the model feel like it had at each step?"

So a perplexity of 10 means the model behaved as if it were choosing uniformly among 10 options at each token. A perplexity of 2 means it was nearly sure what came next.

If your perplexity is 10, it doesn't mean the model literally saw 10 equally likely options. It means the model's uncertainty at each step was equivalent to flipping a fair 10-sided die.

The vocab size is the upper bound. If a model had no idea what came next and spread probability evenly across 50,000 tokens, perplexity would be 50,000. So going from 50,000 down to 10 represents an enormous amount of learned structure about language.

# Summerization

This is one of the most challenging NLP tasks as it requires a range of abilities, such as understanding long passages and generating coherent text that captures the main topics in a document. A deep dive is available [here](https://huggingface.co/learn/llm-course/chapter7/5)

## Rogue metric

For summarization, one of the most commonly used metrics is the ROUGE score (short for Recall-Oriented Understudy for Gisting Evaluation). The basic idea behind this metric is to compare a generated summary against a set of reference summaries that are typically created by humans.

For example, we'll take the following

```
generated_summary = "I absolutely loved reading the Hunger Games"
reference_summary = "I loved reading the Hunger Games"
```

Take recall and precision

$$
\text{Recall} = \frac{\text{Number of overlapping words}}{\text{Total number of words in reference summary}}
$$

In the above, everything in the reference summary is overlapping so it's 6/6

$$
\text{Precision} = \frac{\text{Number of overlapping words}}{\text{Total number of words in generated summary}}
$$

In the above, the 6 overlapping words were in the 10 word generated summary so this gives us 6/7 (0.86).

With both precision and recall, we can produce an F1 score, the harmonic mean of precision and recall

$$
F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
$$

These scores can be handled with the `rogue_score` package

```python
import evaluate

rouge_score = evaluate.load("rouge")
scores = rouge_score.compute(
    predictions=[generated_summary], references=[reference_summary]
)
```

```
{'rouge1': AggregateScore(low=Score(precision=0.86, recall=1.0, fmeasure=0.92), mid=Score(precision=0.86, recall=1.0, fmeasure=0.92), high=Score(precision=0.86, recall=1.0, fmeasure=0.92)),
 'rouge2': AggregateScore(low=Score(precision=0.67, recall=0.8, fmeasure=0.73), mid=Score(precision=0.67, recall=0.8, fmeasure=0.73), high=Score(precision=0.67, recall=0.8, fmeasure=0.73)),
 'rougeL': AggregateScore(low=Score(precision=0.86, recall=1.0, fmeasure=0.92), mid=Score(precision=0.86, recall=1.0, fmeasure=0.92), high=Score(precision=0.86, recall=1.0, fmeasure=0.92)),
 'rougeLsum': AggregateScore(low=Score(precision=0.86, recall=1.0, fmeasure=0.92), mid=Score(precision=0.86, recall=1.0, fmeasure=0.92), high=Score(precision=0.86, recall=1.0, fmeasure=0.92))}
```

The rouge1 variant is the overlap of unigrams which is the value that we calculated above. rouge2 measures the overlap between bigrams (think the overlap of pairs of words)

```
(I, absolutely), (absolutely, loved), (loved, reading), 
(reading, the), (the, Hunger), (Hunger, Games)
```
, while rougeL and rougeLsum measure the longest matching sequences of words by looking for the longest common substrings in the generated and reference summaries. The “sum” in rougeLsum refers to the fact that this metric is computed over a whole summary, while rougeL is computed as the average over individual sentences.

## Baseline

A common baseline for text summarization is to simply take the first three sentences of an article, often called the lead-3 baseline. we'll use the nltk library. `punkt` is our punctuation ruleset that we can use.

```
import nltk

nltk.download("punkt")
from nltk.tokenize import sent_tokenize


def three_sentence_summary(text):
    return "\n".join(sent_tokenize(text)[:3])


print(three_sentence_summary(books_dataset["train"][1]["review_body"]))
```

```
'I grew up reading Koontz, and years ago, I stopped,convinced i had "outgrown" him.'
'Still,when a friend was looking for something suspenseful too read, I suggested Koontz.'
'She found Strangers.'
```

## Fine Tuning

Since summarization is a sequence-to-sequence task, we can load the model with the AutoModelForSeq2SeqLM class, which will automatically download and cache the weights

```python
from transformers import AutoModelForSeq2SeqLM
model_checkpoint = "google/mt5-small"
model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
```

We’ll need to generate summaries in order to compute ROUGE scores during training. Fortunately, 🤗 Transformers provides dedicated Seq2SeqTrainingArguments and Seq2SeqTrainer classes that can do this for us automatically!

```python
from transformers import Seq2SeqTrainingArguments

batch_size = 8
num_train_epochs = 8
# Show the training loss with every epoch
logging_steps = len(tokenized_datasets["train"]) // batch_size
model_name = model_checkpoint.split("/")[-1]

args = Seq2SeqTrainingArguments(
    output_dir=f"{model_name}-finetuned-amazon-en-es",
    evaluation_strategy="epoch",
    learning_rate=5.6e-5,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    weight_decay=0.01,
    save_total_limit=3,
    num_train_epochs=num_train_epochs,
    predict_with_generate=True,
    logging_steps=logging_steps,
    push_to_hub=True,
)
```

The next thing we need to do is provide the trainer with a compute_metrics() function so that we can evaluate our model during training. For summarization this is a bit more involved than simply calling rouge_score.compute() on the model’s predictions, since we need to decode the outputs and labels into text before we can compute the ROUGE scores.

```python
import numpy as np


def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    # Decode generated summaries into text
    decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    # Replace -100 in the labels as we can't decode them
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    # Decode reference summaries into text
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    # ROUGE expects a newline after each sentence
    decoded_preds = ["\n".join(sent_tokenize(pred.strip())) for pred in decoded_preds]
    decoded_labels = ["\n".join(sent_tokenize(label.strip())) for label in decoded_labels]
    # Compute ROUGE scores
    result = rouge_score.compute(
        predictions=decoded_preds, references=decoded_labels, use_stemmer=True
    )
    # Extract the median scores
    result = {key: value.mid.fmeasure * 100 for key, value in result.items()}
    return {k: round(v, 4) for k, v in result.items()}
```

We need a data collator. Luckily, 🤗 Transformers provides a DataCollatorForSeq2Seq collator that will dynamically pad the inputs and the labels for us.

```python
from transformers import DataCollatorForSeq2Seq

data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)
```

Finally, we can train

```python
from transformers import Seq2SeqTrainer

trainer = Seq2SeqTrainer(
    model,
    args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)
trainer.train()
```

