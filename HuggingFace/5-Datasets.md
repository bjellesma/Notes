## What if my dataset isn't on the hub

Here is the [acompanying notebook]([https://colab.research.google.com/drive/1J6WI4AyhZo0aOTHiNjhVLLzYkvUHtpf_#scrollTo=2QGzZ0fg52ZJ](https://colab.research.google.com/drive/1KFcDxZ-qPT9EvAm2zY84PrM24pFnuSoA))

We can use huggingface to load a dataset from our local machine. In the following command, the first arg is the file type. In this case, we're loading json but others like csv and parquet are supported.

```python
from datasets import load_dataset

squad_it_dataset = load_dataset("json", data_files="SQuAD_it-train.json", field="data")
```

When using the json data type, field is necessary because it points to the field in the json we want. The file looks like

```json
{
     data: [],
     version: "1.1"
}
```

We can even load pickled dataframes by specifying the dataset as pandas

```python
squad_it_dataset = load_dataset("pandas", data_files="SQuAD_it-train.pkl", field="data")
```

Notice that we've only loaded the training set but we can also load both the training and test sets by using a mapping. Notice that we're also using the compressed files. HuggingFace can handle the compressed files.

```python
data_files = {"train": "SQuAD_it-train.json.gz", "test": "SQuAD_it-test.json.gz"}
squad_it_dataset = load_dataset("json", data_files=data_files, field="data")
```

This gives us a DatasetDict object

```
DatasetDict({
    train: Dataset({
        features: ['title', 'paragraphs'],
        num_rows: 442
    })
    test: Dataset({
        features: ['title', 'paragraphs'],
        num_rows: 48
    })
})
```

You can also point the data files arg directly to github and avoid having to download locally

```python
url = "https://github.com/crux82/squad-it/raw/master/"
data_files = {
    "train": url + "SQuAD_it-train.json.gz",
    "test": url + "SQuAD_it-test.json.gz",
}
squad_it_dataset = load_dataset("json", data_files=data_files, field="data")
```

### Data Cleaning

We can use the unique keyword to find all unique instances of a field.

```python
print(len(squad_it_dataset['train'].unique("title")))
```

We can filter out all Null values as we do with pandas

```python
def filter_nones(x):
    return x["condition"] is not None

drug_dataset = drug_dataset.filter(lambda x: x["condition"] is not None)
```

We'll now use the map function to make a new condition column which will be lowercase versions of the symptom

```python
def lowercase_condition(example):
    return {"condition": example["condition"].lower()}

drug_dataset = drug_dataset.map(lowercase_condition)
```

Note that the map function can also be used to create a new column

It's also worth noting that sometimes long form text will have html entities associated with them so it's sometimes useful to unescape them. We can also use the `batched` argument to process several entries at once (batch processing).

```python
import html
new_drug_dataset = drug_dataset.map(
    lambda x: {"review": [html.unescape(o) for o in x["review"]]}, batched=True
)
```

Now we want to use this knowledge to tokenize our dataset

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

def tokenize_and_split(examples):
    return tokenizer(
        examples["review"],
        truncation=True,
        max_length=128,
        return_overflowing_tokens=True,
    )

tokenized_dataset = drug_dataset.map(
    tokenize_and_split, batched=True, remove_columns=drug_dataset["train"].column_names
)
```

Notice that we're removing the original columns. This is necessary because return_overflowing_tokens=True can produce multiple output rows from a single input row (when a review exceeds 128 tokens). The original columns can't be aligned with this new row count, so we drop them and keep only the tokenizer's output: input_ids, attention_mask, etc.

Huggingface is designed to be interoperable with pandas so we can do

```python
drug_dataset.set_format("pandas")
drug_dataset["train"][:3] #This now gives us a dataframe.

frequencies = (
    train_df["condition"]
    .value_counts()
    .to_frame()
    .reset_index()
    .rename(columns={"index": "condition", "count": "frequency"})
)
frequencies.head()
```

We can also back to datasets after we've used pandas

```python
freq_dataset = Dataset.from_pandas(frequencies)
freq_dataset
```

Finally, we can save this dataset to disk

```python
drug_dataset_clean.save_to_disk("drug-reviews")
```

Note that this creates a directory like

```
drug-reviews/
├── dataset_dict.json
├── test
│   ├── dataset.arrow
│   ├── dataset_info.json
│   └── state.json
├── train
│   ├── dataset.arrow
│   ├── dataset_info.json
│   ├── indices.arrow
│   └── state.json
└── validation
    ├── dataset.arrow
    ├── dataset_info.json
    ├── indices.arrow
    └── state.json
```

### Loading Big Data

Though huggingface does have good support for big data under the hood, we can also use the `streaming=true` to return a generator object

```python
pubmed_dataset_streamed = load_dataset(
    "json", data_files=data_files, split="train", streaming=True
)
```

### Creating a dataset

Sometimes, it might be useful to create our own datasets. We can do things like create our own corpus from all of our github issues and use that to make a classifier to assign tags.

Note in the following code that we've created a header object with a github token.

```python
import time
import math
from pathlib import Path
import pandas as pd
from tqdm.notebook import tqdm

headers = {"Authorization": f"token {GITHUB_TOKEN}"}

def fetch_issues(
    owner="huggingface",
    repo="datasets",
    num_issues=10_000,
    rate_limit=5_000,
    issues_path=Path("."),
):
    if not issues_path.is_dir():
        issues_path.mkdir(exist_ok=True)

    batch = []
    all_issues = []
    per_page = 100  # Number of issues to return per page
    num_pages = math.ceil(num_issues / per_page)
    base_url = "https://api.github.com/repos"

    for page in tqdm(range(num_pages)):
        # Query with state=all to get both open and closed issues
        query = f"issues?page={page}&per_page={per_page}&state=all"
        issues = requests.get(f"{base_url}/{owner}/{repo}/{query}", headers=headers)
        batch.extend(issues.json())

        if len(batch) > rate_limit and len(all_issues) < num_issues:
            all_issues.extend(batch)
            batch = []  # Flush batch for next time period
            print(f"Reached GitHub rate limit. Sleeping for one hour ...")
            time.sleep(60 * 60 + 1)

    all_issues.extend(batch)
    df = pd.DataFrame.from_records(all_issues)
    df.to_json(f"{issues_path}/{repo}-issues.jsonl", orient="records", lines=True)
    print(
        f"Downloaded all the issues for {repo}! Dataset stored at {issues_path}/{repo}-issues.jsonl"
    )
```

Now we'll load the issues into a dataset

```python
fetch_issues()
issues_dataset = load_dataset("json", data_files="datasets-issues.jsonl", split="train")
```

Now let's create a new boolean column to determine if this is a pull request

```python
issues_dataset = issues_dataset.map(
    lambda x: {"is_pull_request": False if x["pull_request"] is None else True}
)
```

Finally, as we've seen in the previous chapter, we can push to hub 

```python
issues_dataset.push_to_hub("github-issues")
```

### Creating a search engine using FAISS

Let's load a new dataset to create a question and answer corput

```python
from datasets import load_dataset

issues_dataset = load_dataset("lewtun/github-issues", split="train")
```

With this issues dataset, let's filter out pull requests 

```python
issues_dataset = issues_dataset.filter(
    lambda x: (x["is_pull_request"] == False and len(x["comments"]) > 0)
)
```

Let's explode our comments into a table using pandas

```python
# turn into pandas
issues_dataset.set_format("pandas")
df = issues_dataset[:]
comments_df = df.explode("comments", ignore_index=True)

# turn back into dataset
comments_dataset = Dataset.from_pandas(comments_df)
comments_dataset
```

Now what's interesting is that we can concatenate everything into a new concatenated column combining all of the text

```python
def concatenate_text(examples):
    return {
        "text": examples["title"]
        + " \n "
        + examples["body"]
        + " \n "
        + examples["comments"]
    }


comments_dataset = comments_dataset.map(concatenate_text)
```

Now we'll use the sentences transformer to create embedded vectors for our semantic search

```python
from transformers import AutoTokenizer, AutoModel

model_ckpt = "sentence-transformers/multi-qa-mpnet-base-dot-v1"
tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
model = AutoModel.from_pretrained(model_ckpt)

# enable GPU if possible
import torch
device = torch.device("cuda")
model.to(device)

# We want to pool (average) our token embeddings
def cls_pooling(model_output):
    return model_output.last_hidden_state[:, 0]

# This helper function will create the embedded vectors using the model (which we made to run on GPU if possible)
def get_embeddings(text_list):
    encoded_input = tokenizer(
        text_list, padding=True, truncation=True, return_tensors="pt"
    )
    encoded_input = {k: v.to(device) for k, v in encoded_input.items()}
    model_output = model(**encoded_input)
    return cls_pooling(model_output)
```

Now we can map a new embedded vector onto each item in the dataset

```python
embeddings_dataset = comments_dataset.map(
    lambda x: {"embeddings": get_embeddings(x["text"]).detach().cpu().numpy()[0]}
)
```

Now we'll add the Facebook AI Similarity Search (FAISS) to each embedding on our dataset.

```python
embeddings_dataset.add_faiss_index(column="embeddings")
```

Finally, we'll create the question embeddding

```python
question = "How can I load a dataset offline?"
question_embedding = get_embeddings([question]).cpu().detach().numpy()

# Find the most similar embedding to our question embedding
scores, samples = embeddings_dataset.get_nearest_examples(
    "embeddings", question_embedding, k=5
)
```

To check out the results, let's print out the results

```python
import pandas as pd

samples_df = pd.DataFrame.from_dict(samples)
samples_df["scores"] = scores
# Print the top results
samples_df.sort_values("scores", ascending=False, inplace=True)

for _, row in samples_df.iterrows():
    print(f"COMMENT: {row.comments}")
    print(f"SCORE: {row.scores}")
    print(f"TITLE: {row.title}")
    print(f"URL: {row.html_url}")
    print("=" * 50)
    print()
```

```
"""
COMMENT: Requiring online connection is a deal breaker in some cases unfortunately so it'd be great if offline mode is added similar to how `transformers` loads models offline fine.

@mandubian's second bullet point suggests that there's a workaround allowing you to use your offline (custom?) dataset with `datasets`. Could you please elaborate on how that should look like?
SCORE: 25.505046844482422
TITLE: Discussion using datasets in offline mode
URL: https://github.com/huggingface/datasets/issues/824
==================================================

COMMENT: The local dataset builders (csv, text , json and pandas) are now part of the `datasets` package since #1726 :)
You can now use them offline
\`\`\`python
datasets = load_dataset("text", data_files=data_files)
\`\`\`

We'll do a new release soon
SCORE: 24.555509567260742
TITLE: Discussion using datasets in offline mode
URL: https://github.com/huggingface/datasets/issues/824
==================================================

COMMENT: I opened a PR that allows to reload modules that have already been loaded once even if there's no internet.

Let me know if you know other ways that can make the offline mode experience better. I'd be happy to add them :)

I already note the "freeze" modules option, to prevent local modules updates. It would be a cool feature.

----------

> @mandubian's second bullet point suggests that there's a workaround allowing you to use your offline (custom?) dataset with `datasets`. Could you please elaborate on how that should look like?

Indeed `load_dataset` allows to load remote dataset script (squad, glue, etc.) but also you own local ones.
For example if you have a dataset script at `./my_dataset/my_dataset.py` then you can do
\`\`\`python
load_dataset("./my_dataset")
\`\`\`
and the dataset script will generate your dataset once and for all.

----------

About I'm looking into having `csv`, `json`, `text`, `pandas` dataset builders already included in the `datasets` package, so that they are available offline by default, as opposed to the other datasets that require the script to be downloaded.
cf #1724
SCORE: 24.14896583557129
TITLE: Discussion using datasets in offline mode
URL: https://github.com/huggingface/datasets/issues/824
==================================================

COMMENT: > here is my way to load a dataset offline, but it **requires** an online machine
>
> 1. (online machine)
>
> ```
>
> import datasets
>
> data = datasets.load_dataset(...)
>
> data.save_to_disk(/YOUR/DATASET/DIR)
>
> ```
>
> 2. copy the dir from online to the offline machine
>
> 3. (offline machine)
>
> ```
>
> import datasets
>
> data = datasets.load_from_disk(/SAVED/DATA/DIR)
>
> ```
>
>
>
> HTH.


SCORE: 22.893993377685547
TITLE: Discussion using datasets in offline mode
URL: https://github.com/huggingface/datasets/issues/824
==================================================

COMMENT: here is my way to load a dataset offline, but it **requires** an online machine
1. (online machine)
\`\`\`
import datasets
data = datasets.load_dataset(...)
data.save_to_disk(/YOUR/DATASET/DIR)
\`\`\`
2. copy the dir from online to the offline machine
3. (offline machine)
\`\`\`
import datasets
data = datasets.load_from_disk(/SAVED/DATA/DIR)
\`\`\`

HTH.
SCORE: 22.406635284423828
TITLE: Discussion using datasets in offline mode
URL: https://github.com/huggingface/datasets/issues/824
==================================================
"""
```
