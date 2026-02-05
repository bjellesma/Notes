## What if my dataset isn't on the hub

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

