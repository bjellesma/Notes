Before any code is written, I'll define the functions in the `lab_utils.py` file

```py
import os
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf


def df_to_tfdata(df, topic_lookup, title_tokenizer, batch_size=32, buffer_size=1000, shuffle=False):
    '''Converts a pandas dataframe to a tf.data.Dataset'''

    # Extract the news titles and topics
    inputs = df['title']    
    labels = df['topic']

    # Convert the titles and topics to integers
    sequences = title_tokenizer(inputs)
    labels = topic_lookup(labels)

    # Combine the numeric representations to a tf.data.Dataset
    dataset = tf.data.Dataset.from_tensor_slices((sequences,labels))

    # Shuffle and create batches
    if shuffle:
        tf_dataset = dataset.shuffle(buffer_size).batch(batch_size)
    else:
        tf_dataset = dataset.batch(batch_size)

    return tf_dataset


def model_reset_weights(model):
    '''Resets the model with random weights'''

    # Loop through the layers of the model
    for ix, layer in enumerate(model.layers):

        # Reset layers with kernel and bias initializers
        if hasattr(model.layers[ix], 'kernel_initializer') and \
                hasattr(model.layers[ix], 'bias_initializer'):
            weight_initializer = model.layers[ix].kernel_initializer
            bias_initializer = model.layers[ix].bias_initializer
    
            old_weights, old_biases = model.layers[ix].get_weights()
    
            model.layers[ix].set_weights([
                weight_initializer(shape=old_weights.shape),
                bias_initializer(shape=old_biases.shape)])

        # Reset layers with an embedding initializer
        if hasattr(model.layers[ix], 'embeddings_initializer'):
            embeddings_initializer = model.layers[ix].embeddings_initializer
    
            embedding_weights = model.layers[ix].get_weights()[0]
    
            model.layers[ix].set_weights([
                embeddings_initializer(shape=embedding_weights.shape)])
    
    return model

def get_errors(model, df, tokenizer, topic_lookup, topic, num_items=20):
    '''Prints erroneous predictions for a given a news topic'''

    # Convert news titles to integer sequences
    df_title_np = df['title'].to_numpy()
    df_title_np_tokenized = tokenizer(df_title_np)

    # Convert news topics to integers
    df_labels_np = df['topic'].to_numpy()
    
    # Get the list of topics
    topics = topic_lookup.get_vocabulary()

    # Pass the news titles to the model and get predictions
    predictions = model.predict([df_title_np_tokenized], verbose=0)

    # Get the top predictions
    top_predictions = map(np.argmax, predictions)

    # Get the ground truth
    ground_truth = topic_lookup(df_labels_np)

    # Initialize counter
    count = 0

    # Loop through each pair of prediction and ground truth
    for index, (result, gt) in enumerate(zip(top_predictions, ground_truth)):
        
        # For a given class, print if the prediction does not match the ground truth
        if (topics[result]==topic) and (result != gt):
            print(
                f'label: {topics[gt]}\n'
                f'prediction: {topics[result]}\n'
                f'title: {df_title_np[index]}\n'
            )
            
            count+=1

        # Stop if we get a specified number of items
        if count == num_items:
            break



def save_data(df, data_dir, filename):
    '''Saves a dataframe to a given directory as a CSV file'''
    
    os.makedirs(data_dir, exist_ok=True)
    df.to_csv(f'{data_dir}/{filename}', index=False)

def save_vocab(tokenizer, vocab_dir):
    '''Saves a vocabulary to a given directory as a text file''' 
    
    os.makedirs(vocab_dir, exist_ok=True)
    tokenizer.save_assets(vocab_dir)

def save_labels(topic_lookup, vocab_dir):
    '''Saves a labels list to a given directory as a text file''' 
    
    os.makedirs(vocab_dir, exist_ok=True)
    
    labels = topic_lookup.get_vocabulary()
    labels_filepath = f'{vocab_dir}/labels.txt'
    
    with open(labels_filepath, "w") as f:
        f.write("\n".join([str(w) for w in labels]))

    
def set_experiment_dirs(base_dir):
    '''Sets the data, model, and vocab directories for an experiment''' 

    data_dir = f'{base_dir}/data'
    model_dir = f'{base_dir}/model'
    vocab_dir = f'{base_dir}/vocab'
    
    return data_dir, model_dir, vocab_dir

def print_metric_per_topic(df, topics, topic_lookup, title_preprocessor, model):
    '''Prints the accuracy per class of news topics''' 

    print(f'ACCURACY PER TOPIC:\n')
    
    for topic in topics:
        topic_df = df[df.topic == topic]
        topic_ds = df_to_tfdata(topic_df, topic_lookup, title_preprocessor)
        result = model.evaluate(topic_ds, verbose=0)
        accuracy = result[1] * 100
        accuracy = "%.2f " % accuracy
        print(f'{topic}: {accuracy}')
```

## Scoping

Identify a business problem - The company needs a news article classifier to integrate into the application they are building. You'll want to identify the relevant business metrics and determine if the technology can indeed help improve those metrics. In this case, an ML model can help scale up the company's operations as they get more news sources. Manual sorting can't keep up with the velocity of the data, and traditional rule-based algorithms may have given subpar results.

Brainstorm AI solutions - This part has already been done for you. The previous developer settled on an AI solution that classified news articles using their title. In other projects, you may want to brainstorm a few different solutions to see which one addresses the business problem most effectively.

Assess the feasibility and value of potential solutions - ML has demonstrated excellent performance in the area of text classification, so you're confident that this project can be successful. The company already has a prototype, but they want to build something better. Here, you can ask about the data collection process and the problems they encountered with the initial deployment. To assess project ethics, you can also ask if there is an official agreement with the news sources, and if users are linked directly to the publisher's website if they click on an article. Determine the company's stance on fake news and other types of misinformation. Make sure this is a project that moves humanity forward and aligns with your personal ethical values.

Determine milestones and budget for resourcing - Identify the metrics for success and estimate the time and resources needed to carry out the project. Since the company is just starting to integrate ML into their workflow, they also want to better understand its capabilities. They have defined a simple model to predict an article's topic based only on its title. The initial model's results establish a baseline measure of performance as you improve the system. You committed 3 weeks to build and test a proof-of-concept based only on their existing prototype. This will help you estimate future timelines and have a feel for the resources you'll need to build a proper end-to-end project.

## Data

```py
import lab_utils
import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
```

Now let's take a look at the data in the training set. We have the title, topic, link, domain, and published date. The title is the input to the model, the topic is the category of the article as labeled by a previous ML algo, and the other data is just metadata.

```py
# Set the column width so you can see the entire length of the `title` column
pd.set_option('display.max_colwidth', None)

# Load the datasets into dataframes
train_df = pd.read_csv(f'{data_dir}/train_data.csv')
test_df = pd.read_csv(f'{data_dir}/test_data.csv')

# Preview the first 10 rows of the training set
train_df[:10]
```

![image](https://github.com/user-attachments/assets/38de5d40-b436-4dd7-af39-df60645beae0)

We're given an exercise when defining data in this project to manually make labels for data to showcase how there can be inconsistencies

```py
# Indices of the dataframe to use
start_index = 30
end_index = 40

# Sample titles to label
train_df[['title']][start_index:end_index]

# # When you're done, uncomment the next line to see the 'true' labels 
# train_df[['title', 'topic']][start_index:end_index]
```

![image](https://github.com/user-attachments/assets/8eeb9247-b050-4379-8710-56e78f18e655)

```py
# Sample titles to label
train_df[['title']][start_index:end_index]

# # When you're done, uncomment the next line to see the 'true' labels 
train_df[['title', 'topic']][start_index:end_index]
```

![image](https://github.com/user-attachments/assets/cc021660-d2c5-49b3-a334-ba19cecf71a6)

If there are inconsistencies when labeling the data, it may be worth asking the following kinds of questions.

How were the labels determined? How many labellers were involved and how were their outputs aggregated? What is the inter-rater reliability?
How is each topic defined? For example, how are Science articles different from Technology ones?
Can any of the other 3 unused columns be used as a predictive feature in the model?
Is the article's title really enough for this application? If I could collect data again, what other predictive features would I want to have in order to generate more consistent labels?
Will it help accuracy to add a new topic, or to merge two overlapping topics?

## Establishing a baseline

We'll want to establish a baseline by looking at the previous model in tensorflow

```py
# Load the model
model = tf.keras.models.load_model(model_dir)

# Show the model architecture
model.summary()
```
![image](https://github.com/user-attachments/assets/1c75ae29-6a69-4441-8d93-b23685bbcc97)

From this, we can see that the model is relatively simple with 1 embedding layer and 1 dense layer. The following code will also show you the optimizer, loss, and metrics used in the model.

```py
model.get_compile_config()
```

```js
{'optimizer': {'module': 'keras.optimizers',
  'class_name': 'Adam',
  'config': {'name': 'Adam',
   'weight_decay': None,
   'clipnorm': None,
   'global_clipnorm': None,
   'clipvalue': None,
   'use_ema': False,
   'ema_momentum': 0.99,
   'ema_overwrite_frequency': None,
   'jit_compile': False,
   'is_legacy_optimizer': False,
   'learning_rate': 0.0010000000474974513,
   'beta_1': 0.9,
   'beta_2': 0.999,
   'epsilon': 1e-07,
   'amsgrad': False},
  'registered_name': None},
 'loss': {'module': 'builtins',
  'class_name': 'function',
  'config': 'sparse_categorical_crossentropy',
  'registered_name': 'function'},
 'metrics': [[{'module': 'keras.metrics',
    'class_name': 'MeanMetricWrapper',
    'config': {'name': 'sparse_categorical_accuracy',
     'dtype': 'float32',
     'fn': {'module': 'builtins',
      'class_name': 'function',
      'config': 'sparse_categorical_accuracy',
      'registered_name': 'function'}},
    'registered_name': None}]],
 'loss_weights': None,
 'weighted_metrics': None,
 'run_eagerly': None,
 'steps_per_execution': None,
 'jit_compile': None}
```

We'll use tensorflow's StringLookup to **tokenize** that is to convert the strings to integers. Notice that during tokenization, we're only using titles up to 20 characters because our team informed us that there are rarely titles of more than 20 characters.

```py
# Create a lookup list for the labels
topic_lookup = tf.keras.layers.StringLookup(vocabulary=f'{vocab_dir}/labels.txt', num_oov_indices=0)

# Check the list of labels
topic_lookup.get_vocabulary()

# Title length and vocabulary size used by the team for the prototype
MAX_LENGTH = 20
VOCAB_SIZE = 10000

# Instantiate a layer for text preprocessing
title_preprocessor = tf.keras.layers.TextVectorization(max_tokens=VOCAB_SIZE, output_sequence_length=MAX_LENGTH)

# Load the vocabulary file
title_preprocessor.load_assets(vocab_dir)

# Check the vocabulary size
print(f'vocabulary size: {title_preprocessor.vocabulary_size()}')

# Get a sample title
sample_title = train_df['title'][10]

# Sample title in string format
print(f"sample text: {sample_title}")

# Sample title represented as an integer sequence
print(f"sample text (preprocessed): {title_preprocessor(sample_title)}")
```

![image](https://github.com/user-attachments/assets/af9e86c1-82c4-44a3-bc18-d3302ec13fed)

Finally, we can get the metrics for our data

```py
# Convert the test dataframe to a tf dataset
test_ds = lab_utils.df_to_tfdata(test_df, topic_lookup, title_preprocessor)

# Get the metrics
model.evaluate(test_ds)
```

![image](https://github.com/user-attachments/assets/9df34def-782f-4305-bdfd-090567ac5734)

So we have an accuracy of about 77% which we will treat as our baseline

## Label and Organize Data

We want to take a data centric approach so that means that we'll be keeping the model static and focus on improving the data quality. Here's a flowchart of the data pipeline that we'll follow

![image](https://github.com/user-attachments/assets/0c146032-1e33-44c2-a7cc-df31f92253c5)

As you can see in the below screenshot, the splits for the test and training set are very imbalanced which is not great when acting on small datasets. In the screenshot, science has a very low percentage in the training set and will likely underperform.

![image](https://github.com/user-attachments/assets/022b6c06-2873-4001-ab65-3fb9a7c75956)

So let's split the data into a more balanced set of 60%/20%/20%

```py
# EXERCISE

# Load the train and test sets
train_df = pd.read_csv(f'{data_dir}/train_data.csv')
test_df = pd.read_csv(f'{data_dir}/test_data.csv')

# Combine the two datasets. Set ignore_index to False.
combined_df = pd.concat([train_df,test_df], ignore_index=True)

### START CODE HERE ###

# Split the combined dataset to 60% train, 20% dev, and 20% test set. Produce a balanced split along the `topic` column.
train_df, test_df = train_test_split(combined_df, test_size=0.4, stratify=combined_df['topic'])
train_df, dev_df = train_test_split(test_df, test_size=0.5, stratify=test_df['topic'])

### END CODE HERE
```

![image](https://github.com/user-attachments/assets/82fc50d5-5e59-4f99-9fb5-5f6a037414d8)

## Modeling

We're now in the modeling phase of the product lifecycle.

```py
import lab_utils
import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

# Working folder for the experiment
BASE_DIR = './E1'

# Get the subdirectories that contain the experiment files
_, model_dir, _ = lab_utils.set_experiment_dirs(BASE_DIR)

# Load the model
model = tf.keras.models.load_model(model_dir)

# Working folder for the experiment
BASE_DIR = './E2'

# Title length and vocabulary size used by the team for the prototype
MAX_LENGTH = 20
VOCAB_SIZE = 10000

# Get the subdirectories that contain the experiment files
data_dir, model_dir, vocab_dir = lab_utils.set_experiment_dirs(BASE_DIR)

# Load the train and test sets
train_df = pd.read_csv(f'{data_dir}/train_data.csv')
dev_df = pd.read_csv(f'{data_dir}/dev_data.csv')
test_df = pd.read_csv(f'{data_dir}/test_data.csv')

# Instantiate a layer for text preprocessing
title_preprocessor = tf.keras.layers.TextVectorization(max_tokens=VOCAB_SIZE, output_sequence_length=MAX_LENGTH)

# Create a lookup list for the labels
topic_lookup = tf.keras.layers.StringLookup(vocabulary=f'{vocab_dir}/labels.txt', num_oov_indices=0)
```

Once again, keep in mind that we're taking a data centric approach and we're just going to be using our new balanced dataset with the existing model. However, before we feed the data into the existing model, we want to make sure that we update our preprocessor according to the data pipeline that we've laid out.

Let's first update our title preprocessor

```py
# Extract the titles from the new training set
train_inputs = train_df['title']

# Generate a new vocabulary
title_preprocessor.adapt(train_inputs)

# Save the new vocabulary
lab_utils.save_vocab(title_preprocessor, vocab_dir)
```

Now we can run the data inside the model

```py
NUM_EPOCHS = 5

# Convert the string datasets to Tensorflow datasets
train_ds = lab_utils.df_to_tfdata(train_df, topic_lookup, title_preprocessor, shuffle=True)
dev_ds = lab_utils.df_to_tfdata(dev_df, topic_lookup, title_preprocessor)
test_ds = lab_utils.df_to_tfdata(test_df, topic_lookup, title_preprocessor)

# Reset the model weights
model = lab_utils.model_reset_weights(model)

# Train the model. Use the dev set to check if your model is overfitting.
model.fit(train_ds, epochs=NUM_EPOCHS, validation_data=dev_ds, verbose=1)

model.evaluate(test_ds)
```

We can see now that the accuracy is about 85% which is better than the 77

### Error Analysis

Let's now analyze the errors on each of the topics to decide what to work on

```py
# Get the list of topics
topics = topic_lookup.get_vocabulary()

# Evaluate the model's performance for each topic
lab_utils.print_metric_per_topic(dev_df, topics, topic_lookup, title_preprocessor, model)
```

![image](https://github.com/user-attachments/assets/13ae5420-2f8e-4c94-8335-3ef4e50eae65)

