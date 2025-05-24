### This lab will showcase a model working on unstructured data (text) to determine spam comments in the top 5 youtube videos of 2015

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB

def load_labeled_spam_dataset():
    """Load labeled spam dataset."""

    # Path where csv files are located
    base_path = "./data"

    # List of csv files with full path
    csv_files = [os.path.join(base_path, csv) for csv in os.listdir(base_path)]

    # List of dataframes for each file
    dfs = [pd.read_csv(filename) for filename in csv_files]

    # Concatenate dataframes into a single one
    df = pd.concat(dfs)

    # Rename columns
    df = df.rename(columns={"CONTENT": "text", "CLASS": "label"})

    # Set a seed for the order of rows
    df = df.sample(frac=1, random_state=423)
    
    return df.reset_index()

# Save the dataframe into the df_labeled variable
df_labeled = load_labeled_spam_dataset()

# Drop unused columns
df_labeled = df_labeled.drop(['index', 'COMMENT_ID', 'AUTHOR', 'DATE'], axis=1)

# Save the text into the X variable
X = df_labeled.drop("label", axis=1)

# Save the true labels into the y variable
y = df_labeled["label"]

# Use 1/5 of the data for testing later
# stratify will allow us to have a split that is more representative of the entire example
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Print number of comments for each set
print(f"There are {X_train.shape[0]} comments for training.")
print(f"There are {X_test.shape[0]} comments for testing")

# a countvectorizer will count the occurances of word appearing in the comments
# ngrams refers to the length of phrases that we will find meaningful
vectorizer = CountVectorizer(ngram_range=(1, 5))

# now that the text is encoded, we'll use a naive bayes model

def calculate_accuracy(X_tr, y_tr, X_te=X_test, y_te=y_test, 
                       clf=MultinomialNB(), vectorizer=vectorizer):
    """
    Train a text classifier and calculate its accuracy on test data.
    
    This function vectorizes text data, trains a classifier, makes predictions,
    and returns the accuracy score. It handles the complete pipeline from
    raw text to accuracy evaluation.
    
    Parameters
    ----------
    X_tr : pandas.DataFrame
        Training data containing a 'text' column with text samples
    y_tr : array-like
        Training labels corresponding to X_tr
    X_te : pandas.DataFrame, optional
        Test data containing a 'text' column with text samples
        Default is X_test (global variable)
    y_te : array-like, optional  
        Test labels corresponding to X_te
        Default is y_test (global variable)
    clf : sklearn classifier, optional
        Classifier to train and evaluate
        Default is MultinomialNB()
    vectorizer : sklearn vectorizer, optional
        Text vectorizer (e.g., CountVectorizer, TfidfVectorizer)
        Default is vectorizer (global variable)
    
    Returns
    -------
    float
        Accuracy score (between 0 and 1) of the classifier on test data
    
    Examples
    --------
    >>> # Using default parameters
    >>> acc = calculate_accuracy(X_train, y_train)
    >>> print(f"Accuracy: {acc:.3f}")
    
    >>> # Using custom classifier and vectorizer
    >>> from sklearn.svm import SVC
    >>> from sklearn.feature_extraction.text import TfidfVectorizer
    >>> custom_vec = TfidfVectorizer(max_features=5000)
    >>> acc = calculate_accuracy(X_train, y_train, clf=SVC(), vectorizer=custom_vec)
    
    Notes
    -----
    - The vectorizer is fit only on training data to prevent data leakage
    - Test data is transformed using the fitted vectorizer
    - Assumes input DataFrames have a 'text' column containing string data
    """
    
    # Encode train text
    X_train_vect = vectorizer.fit_transform(X_tr.text.tolist())
    
    # Fit model
    clf.fit(X=X_train_vect, y=y_tr)
    
    # Vectorize test text
    X_test_vect = vectorizer.transform(X_te.text.tolist())
    
    # Make predictions for the test set
    preds = clf.predict(X_test_vect)
    
    # Return accuracy score
    return accuracy_score(preds, y_te)

accs = dict()

# since this is random labeling, let's run this 10 times to establish a more accurate lower bound
# Empty list to save accuracies
rnd_accs = []

for _ in range(10):
    # Add every accuracy to the list
    rnd_accs.append(calculate_accuracy(X_train, np.random.randint(0, 2, X_train.shape[0])))

# Save result in accs dictionary
accs['random-labels'] = sum(rnd_accs)/len(rnd_accs)

# Print result
print(f"The random labeling method achieved an accuracy of {accs['random-labels']*100:.2f}%")

# Now we'll use the ground truth labels to establish an upper bound

# Calculate accuracy when using the true labels
true_acc = calculate_accuracy(X_train, y_train)

# Save the result
accs['true-labels'] = true_acc

print(f"The true labeling method achieved and accuracy of {accs['true-labels']*100:.2f}%")

# for our first iteration, let's make this rule based and say that if the words free, subs or http appear, we'll classify it as spam

def labeling_rules_1(x):
    
    # Convert text to lowercase
    x = x.lower()
    
    # Define list of rules
    rules = [
        "free" in x,
        "subs" in x,
        "http" in x
    ]
    
    # If the comment falls under any of the rules classify as SPAM
    if any(rules):
        return 1
    
    # Otherwise, NO_LABEL
    return -1

# Apply the rules to the comments in the train set
labels = [labeling_rules_1(label) for label in X_train.text]

# Convert to a numpy array
labels = np.asarray(labels)

print(labels)
# array([-1, -1, -1, ..., -1, -1,  1])

# Now that we've made an initial classification based on rules, let's remove the comments that were flagged in that rule
X_train_al = X_train[labels != -1]

# Remove predictions with NO_LABEL label
labels_al = labels[labels != -1]

print(f"Predictions with concrete label have shape: {labels_al.shape}")

print(f"Proportion of data points kept: {labels_al.shape[0]/labels.shape[0]*100:.2f}%")

# Now let's get the model performance on the 382 out of the original 1564 comments
# Compute accuracy when using these labels
iter_1_acc = calculate_accuracy(X_train_al, labels_al)

# Display accuracy
print(f"First iteration of automatic labeling has an accuracy of {iter_1_acc*100:.2f}%")
# First iteration of automatic labeling has an accuracy of 51.28%

# Save the result
accs['first-iteration'] = iter_1_acc

# Now let's improve our rule based approach from the first iteration
def labeling_rules_2(x):
    
    # Convert text to lowercase
    x = x.lower()
    
    # Define list of rules to classify as NOT_SPAM
    not_spam_rules = [
        "view" in x,
        "song" in x
    ]
    
    # Define list of rules to classify as SPAM
    spam_rules = [
        "free" in x,
        "subs" in x,
        "gift" in x,
        "follow" in x,
        "http" in x
    ]
    
    # Classify depending on the rules
    if any(not_spam_rules):
        return 0
    
    if any(spam_rules):
        return 1
    
    return -1

# We can also take a look at a third rule because we notice that non spam comments are usually shorter

from statistics import mean

print(f"NOT_SPAM comments have an average of {mean([len(t) for t in df_labeled[df_labeled.label==0].text]):.2f} characters.")
print(f"SPAM comments have an average of {mean([len(t) for t in df_labeled[df_labeled.label==1].text]):.2f} characters.")
# NOT_SPAM comments have an average of 49.64 characters.
# SPAM comments have an average of 137.34 characters.

def labeling_rules_3(x):
    
    # Convert text to lowercase
    x = x.lower()
    
    # Define list of rules to classify as NOT_SPAM
    not_spam_rules = [
        "view" in x,
        "song" in x,
        len(x) < 30
    ]
    

    # Define list of rules to classify as SPAM
    spam_rules = [
        "free" in x,
        "subs" in x,
        "gift" in x,
        "follow" in x,
        "http" in x,
        "check out" in x
    ]
    
    # Classify depending on the rules
    if any(not_spam_rules):
        return 0
    
    if any(spam_rules):
        return 1
    
    return -1



