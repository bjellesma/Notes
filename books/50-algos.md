# 50 Algorithms every Programmer Should know

## Data Structures

Python has 4 major data structures:

* **List** - mutatable, ordered set of data
* **Tuple** - immutable, order set of data
* **Dictionary** - an unordered collection of key-value pairs
* **Set** - An unordered collection of elements. The elements in here are unique so this is a good data structure for getting rid of data. A set is mutable unless it is an ordered set.

Whenever possible, you should prefer to use an immutable set of data over a mutable set of data for performance reasons. Accessing an element in a list is O(n) whereas in a tuple it's O(1) since it's indexed from initialization.

### Pandas Series and Dataframes

**Series** - Think of a series as a single column in a spreadsheet. It is designed to be a one dimensional array of values for homogeneos data.

**DataFrame** - this is designed to be a two dimensional array so that you can represent a full table of values.

An **axis* is defined to be one column or row of data in a pandas series/dataframe.

### Matrices

Using the library numpy, you can created a **matrix** by making a two dimensional array like `np.array([[11,12,13],[21,22,23],[31,32,33]])`

Numpy is insanely fast for Matrix operations, which can normally be `O(n^3)`, because it takes advantage of optimized algorithms.

Numpy arrays are generally faster and more efficient than normal python lists

```py
vector = np.array([22,33,44,55])
```

creates

```sh
[22 33 44 55]
```

## Stacks

A push and pop operation is a stack are both `O(1)` for time complexity since we only need to reference the top of the stack. Examples of stacks might be browser history and the undo button in a word processing application.

## Queues

A queue is like a stack except that it always inserts an item at the end and removes an item from the from. Because of this, the time complexity of these operations are always O(1) since **enqueuing** just means inserting at item at end and **dequeuing** just means removing an item from the ffront. We're never traversing over the data structure.

## Trees

a **tree** is simply a hierarchical data structure where you have a root node, internal nodes (both a parent and child node), and leaf nodes (nodes with no children Nodes)

The **degree** of a node is how many children that it has

### Types of Trees

* A **binary tree** is a tree where the root node has a degree of two.![image](https://github.com/bjellesma/Notes/assets/7660667/d492ce38-7417-4d09-8c36-1cad15472fdf)

* A **full tree** is a tree in which every node has either the same degree as all other nodes or is a leaf node. ![image](https://github.com/bjellesma/Notes/assets/7660667/b8f36f75-9cff-4542-8216-eeb84c7f8fd7)

* A **perfect tree** is like a full tree but also has all leaf nodes at the same level ![image](https://github.com/bjellesma/Notes/assets/7660667/976b0607-13b0-4dc7-8827-85e0c220013e)
* an **ordered tree** is just a tree in which the children nodes follow some defined order. for example, if it's organized from left to right.

These data structures, besides being used for search and sort algos in computer science, are used in unsupervised and supervised machine learning as decision trees.

# Searching and Sorting Algorithms

These algos are used extensively in Natural Language Processing

## Bubble Sort

The **bubble sort** is the simplist sorting algorithm but is only recommended for smalled data sets as the time complexity can be O(n^2) which is quadratic time. Bubble sort is simply based on comparing ajacent nodes. If the value in the higher index is greater, then swap, otherwise don't ![image](https://github.com/bjellesma/Notes/assets/7660667/d6cb7071-748f-4df9-be07-a5c2e893e2d0)

In the cases of reversed lists or partial sorted lists, you will need to make subsequent passes which is why the time complexity at worst is quadratic.

## Insertion Sort

**insertion sort** will remove a data point from the data structure that we have and then insert it into the correct positon. So over each iteration, we add remove the next element from a data structure and insert it into the correct position of our sorted part. ![image](https://github.com/bjellesma/Notes/assets/7660667/4fd94ac7-7d83-40c7-82a6-dd775a6f0b96)

```py
def insertion_sort(elements):
  for i in range(len(elements)):
    j = i-1
    next_element= elements[i]

    # iterate backward through the sorted position looking for the appropriate position for next_element
    while j >= 0 and elements[j] > next_element:
      elements[j+1]=elements[j]
      j -= 1

    elements[j+1]=next_element
  return elements

```

In its best case scenarios, time complexity is O(n) or linear because the data is nearly sorted. However for large and random data sets, insertion sort is slightly worse than quadratic. This means that insertion sort is good for smaller datasets or datasets that are nearly sorted. However, this is a bad algo to choose for larger and random data sets.

## Merge Sort

Merge sort remains efficient with large and random datasets because of its divide and conquer mentality. The **merge sort** works by continuously dividing the dataset in half until there are only two elements and then sorting that. ![image](https://github.com/bjellesma/Notes/assets/7660667/8c332f5c-f50c-4197-bd93-58c072f56a44)

## Shell Sort

The Shell sort works like a bubble sort but questions the need to use immediate neighbors. Instead the **shell sort** uses neighbors of a fixed length apart. usually dividing the length of the list by two.

![image](https://github.com/bjellesma/Notes/assets/7660667/eff25475-2269-4bdf-8605-fc0a784a8d35)

Like the bubble sort, the time complexity can be quadratic in the worst case. However, the shell sort is more optimized for data sets of less than 6000 elements. This makes the algo a good candidate for medium sized data sets and if the data is already partially sorted.

## Selection sort

In the **selection sort**, we want optimize the bubble sort swaps and just find the next largest value and put that at the top of the data structure.
![image](https://github.com/bjellesma/Notes/assets/7660667/72ea0081-279f-4635-b097-c3b32182c723)

Selection sort is also quadratic time complexity in its worst case but is better optimized than other algos in its average case making it the go to choice.

## Choosing a sorting algo

Even though the merge sort might be powerful, it might be overkill to employ for some small dataset that's already nearly sorted. 

For small and nearly sorted lists, bubble sort might be best due to its simplicity

For patially sorted lists, insertion sorts work well since it can capitalize on skipping existing order, increasing efficiency.

For larger data sets that are more random, merge sort works well. Think of this like a library that has just received a shipment of books. A good humanistic approach is to sort that big group by various attributes like author and publication data so that we have smaller datasets that we can then merge together.

## Linear Search

**Linear Search** is just a brute force search for the item in the list and, if not found, keep going. The advantage is that this doesn't require the list to be presorted. The disadvantage is that this can be very slow in the worst case if the item we're looking for is at the end which means that it is an O(n) algo.

## Binary Search

the **Binary Search** has a prerequite that the list must already be sorted because it continuously divides the entire list into two parts and keeps track of the lowest and highest indices to see if the value is within either part. Though this introduces the fact that the time complexity is O(log(N)) or logarithmic, this does require that you use a sorting algorithm first if the list is not sorted.

![image](https://github.com/bjellesma/Notes/assets/7660667/2437ba12-c304-499f-95f4-4761df63c293)

## Interpolation Search

the **interpolation search** will use the target value to try to gain context about where to start searching. As with binary search, the list must first be sorted before an accurate search can take place. The best way to think of an interpolation search is if you're looking for catcher and the rye in the library. You'll start with the section starting with C.

The worst case where the data in ununiformly distributed has a time complexity of O(N) whereas the best case where the data is uniformely distributed is O(log(log(N))).

## Fuzzy Search

**Fuzzy Search** is more of a concept to detect near misses on searches to account for real world scenarios like incorrectly spelled data. For example, if you're searching for "Jon Doe", you may also want results for "John Doe". Often a fuzzy search involves using some sort of distance algorithm to detect those near misses.

# Chapter 4: Designing Algorithms

## Basic Concepts of Designing an algorithm

**Functional Requirements** set out aspects like what the input and output should be while **non-functional requirements** set out expectations like what the performance and security should be.

When Designing an algo, three concerns should be addressed

### Correctness: Is the output expected

We need some idea of what the correct output will be for a given set of inputs. This way, we can accurately test and ensure that we get the proper algo.

We also need to consider edge cases and not just the "happy path" so that we can accurately account for all scenarios. Unfortunately, we need to understand that we will not be able to consider every edge case but we should consider as many as possible.

### Performance: Is this the optimal way

This brings up the concept of **P=NP**. P stands for polynomial agorithm such as O(N^k) where k is a power. NP stands for non-polynomial where we do not know of the existance of a polynomial algorithm to solve a certain problem like the traveling salesperson. Therefor, every polynomial problem is a subset of a non-polynomail problem. For example, a searching algo like binary search is known to have a big O notation is polymial time but of course can also be solved in less sophisticated ways that would be a non polynomial efficiency. Conversely, problems like the traveling salesperson are not known to have a polynomial solution.

There is heavy research into finding if these types of problems like traveling salesperson would have a polynomial solution because that would help prove P=NP. Proving that relation would mean major advancements in the fields of AI and other theoretical fields. AI, for example, is still heavily limited by the processing power needed and if it had faster processing, would lead to major advancements.

Here are examples of problems, where they lie, and their explanations.

* P (polynomial) - Hashtable lookup - solvable in polynomial time
* NP (non polynomial) - RSA encryption - not solvable in polynomial time but can be verified in polynomial time
* NP-Hard (non polynomial) - Optimal clustering using the K-means algorithm - complex problems that no one has been able to solve but if solved, would have a measurable polynomial time execution.
* NP-Complete (non polynomial) - optimal solution for the traveling salesperson - this is a combination of NP and NP-hard because it both is complex enough that it has not been solved yet and it won't have a polynomial solution.

### Scalability: How will this perform on larger datasets


Estimating the requirement of the increase in resource requirements as the input data is increased is called **space complexity analysis**. Conversely, the estimate for the increase in time taken to run as the input data is increased is called **time complexity analysis**.

The ability of cloud computing to provision more resources as processing requirements increase is called **elasticity**. 

**Distributed Computing** is a methodology where we break problems into independant subproblems that will run independantly of each other. This follows an algorithm design principle known as **divide and conquer**. Divide and conquer is good for larger problems that can be broken down into independant subproblems but is not good for problems that require intensive iterations.

**Dynamic Programming** is similar to divide and conquer in the way that we break down to the easiest subproblem. The easiest subproblem can then be solved and have its answer saved off in a process called **memoization** so that it doesn't have to be recomputed in the next iteration. You can think of this as a bottom up strategy. Because of this bottom up strategy, we often invoke the strategy of **recursion**. The rule of thumb is that if your recursive algorithm is wasting computation because it's going over the same problem, we should invoke memoization which intellegently saves the answer off in a table that we can reference rather than having to waste compute.

### Greedy algorithms and the Traveling Salesperson problem

In the **traveling salesperson problem**, there a predefined number of cities with a known distance in between them and the goal is to visit each city exactly once and then return back to the initial city. The obvious way to solve this is to use a brute force method to go through every possible permutation of traveling the cities and returning home and then choosing the one that has the minimum distance required. The problem is that this requires interating over `(n-1)!` iterations. This means that for a dataset of just five cities, this is 24 iterations and for 6 cities 120 iterations. It is clear that for larger datasets, this will quickly become unmanageable. 

The idea of using a **greedy algorithm** means that we ignore finding the optimal solution and instead just find a sufficient solution which will require less compute overall. For the traveling salesperson problem, we might just use a reasonable city and then traverse to each of the nearest neighbors. For a list of 2000 cities, using a greedy algorithm may not find the optimal solution but it will find a solution more quickly. In testing, it may only take .5s to run whereas using a brute force method to find the optimal solution will take `1999!` iterations which is `1.65x10^5732` permutations.

## Linear Programming

**Linear Programming** is useful when we have constraints on resources that we can model with mathematical equeations. For example, linear programming is used extensively in the manufacturing industry to model and schedule when technicians and engineers will be available to work on their products. 

# Chapter 6: Graph Algorithms

Graph algorithms are used in real world scenarios such as fraud detection and social media recommendations. In graph theory, a vertex or node represents a real world object such as a person, computer or activity and an edge (bidirectional unless specified otherwise) will represent a connection btween the two vertices (think of a friendship on facebook). 

A **simple graph** is a graph with no parallel edges or loops. ![image](https://github.com/bjellesma/Notes/assets/7660667/c53d4f8e-c479-46ed-aa2d-02b72f382740)

A **directed graph** is a graph where each edge has a direction, indicating a one way relationship

an **undirected graph** is a graph where edges don't have a specific direction, suggesting a mutual relationship.

A **weighted graph** is a graph where each edge carries a weight, often representing distances or costs

At the heart of many graphs is a concept called the **ego network** or **egonet** which is the study of just one specific node and its immediate surroundings. For example, in online social networks an egonet can be used to help detect an influencer.

In graph theory, a **path** is defined as the route between two nodes with the **length** being defined as the number of edges that need to be traversed. Algorithms have been defined to find the shortest possible paths, with **Dijkstra's Algorithm** being the most famous as it is used in modern applications such as GPS.

**Density** is a metric in graph theory used to identify how closely knit a network or segment of a network is. A density close to 1 is more tight knit and closer to 0 indicates a more sparse relationship. This metric is useful in various scenarios such as identifying socail network. For example, if everyone knows each other, the number of edges is going to be high.

$$$
Density = \frac{2x\text{Number of edges}}{\text{Number of vertices}(\text{Number of Vertices - 1}}
$$$

The number of edges connected to a specific node is called the **degree** of the node. 

**eigenvectors** in graph theory are used to identify the significance of nodes by idenfifying if that node is connected to several other nodes that are also significant.

the idea of the **breadth first search (BFS)** is that it traverses nodes layer by layer taking into account how far the node is from another node. Think of Linkedin and how you have first, second, and third connections. In contrast, you have the idea of a **depth first search (DFS)** which will venture deeply down a path of edges first before searching the immediate neighboors of a vertex.

# Unsupervised Machine Learning

unsupervised machine learning is like a dectective trying to piece together clues to find a pattern. **data mining** is the process of discovering meaningful correlations and patterns in the data. **Cross Industry Standard Process for Data Mining** is a popularer process of data mining agreed on by a variety of companies including Crystler and IBM. This process is outlined in the diagram below. ![image](https://github.com/bjellesma/Notes/assets/7660667/36ebe5bd-2414-44f4-8f87-fbc8b719b5c6)

## Business Understanding

This phase focus on what needs to be done and not how it will be done. It's a focus on the business requirements and scope and trying to transform that into machine learning. 

## Data Understanding

This phase is about understanding the available data. This uses tools like visualizations and dashboards to summerize and understand the patterns.

## Data Preparation

We are taking the data and cleaning it to remove outliers, normalize, remove nulls, etc so that we can feed the data into the machine learning algorithm.

## Modeling

This phase is focused on both model training and model tuning. Model training is where we feed the data prepared into the machine learning algorithm while model tuning is a process is which we want to optimize the parameters of the model so that it performs accurately on both prepared data and new untrained data. **overfitting** is a term used to describe when the model performs inaccurately on new data.

## Evaluation

This is where we evaluate the model by using the test data that we've derived during the data preparation data.

## Deployment

This is where we examine if the model is ready. Just because the model evaluated the data accoring to our expectations doesn't mean that the model is ready to solve real world problems. We have to consider how the model will handle edge cases, how it will handle unseen data, and how well it will or won't integrate with existing systems.

## Current research in unsupervised machine learning

**feaures**, in maching learning terminology, refer to measurable characteristics on dataset. For example, a customer dataset will have features such as age, purchase history, or browsing behavior. **Labels** represent the outcomes that we want the model to predict based on those features. Supervised learning focuses on establishing relationships between these features and labels. Unsupervised machine learning is not restricted to these relationships and has wider breadthk. However this also means that unsupervised learning is often more computationally intense. 

## Clustering Algorithm

The simplist form of machine learning is clustering together similar patterns in the data. Because this is not based on any assumptions, this is often considered an unsupervised algo. Think of a librarian grouping together books without being told a characteristic to group by. In machine learning, clustering algorithms work by **quantifying similarities**. By this, we mean that we are plotting their distances or similararities on a graph and measuring their distance. There are two types of clustering for this:

### Intercluster

This refers to the distance between two clusters or groups of data points.

### Intracluster

This refers to the distance between data points within the same cluster.

Therefore, the job of a good clustering algorithm is to maximize the intercluster distance while minimizing the intracluster distance. There are three popular methods for quantifying similaries:

### Euclidean Distance

Euclidean distance is just the "as the crow flies" distance between two data points in 3 dimensional space. It can be found by using the pythagorean formula if you plot these points on a graph.

### Manhattan distance

It is named as this because it models how you get from a to b in a city. You must travel through a bunch of different streets and can't use the "as the crow flies" distance. For this reason, this is usually a more accurate way to quantify distance depending on the grid lines being used. 

### Cosine Distance

Euclidean and Manhattan distances work well in lower dimensional space but lose value as the data points are plotted in higher dimensional space. Cosine uses the angle between the data points to get a reading. textual data is almost always using cosine similarity because it frequentlly uses high dimensions.

## k means clustering algorithm

**k means clustering algorithm** is one of the more popular algorithms used in machine learning. K refers to the number of features that we're finding the distance between. K must be predetermined which is a limitation of this algo. The algo is useful because they are simple iterations to perform which is why it is popular. it is simple and fast. another note is that you will need a stop condition in order for the algo to stop iterating.

# Supervised Learning Algorithms

Supervised Machine Learning is a popular methodology in machine learning characterized by giving the algorithm a set of inputs, **features**, and getting corresponding sets of output, **labels**. Features are usually things like user profiles and historical sales figures while the labels are outcomes that we want to predict like customer purchasing habits. using a given dataset, a supervised ml algorithm is used to train a model that captures the complex relationship between the features and labels represented by a mathematical formula. This trained model is the basic vehicle that is used for predictions. 

The ability to learn from existing data in supervised learning is similar to the ability of the human brain to learn from experience. 

Besides features and labels, we can define the following terms:

**feature engineering** - Transforming features to prepare them for the chosen supervis ml algo 
**feature vector** - befor providing an input to a supervised ml algo,, all of the features are combined to a data structure called a feature vector
**training/testing data** - historical data with examples is divided into two parts - a larger dataset call training data and a smaller dataset called the testing data
**model** - a mathematical formulation of the patterns that best capture the relationship between label and feature
**testing** - evaluating the trained model against testing data
**predicting** - using our trained model to estimate a label

A supervised ML algo needs some enabling conditions to be met in order to perform:

* Enough Samples - We say that we have enough examples when we have conclusive evidence that the pattern of interest is fulljy represented in our dataset.
* Patterns in historical data - the examples used to train our model should have some type of discernable pattern.
* Valid Assumptions - look at an example of an algo granting work visas. It is understood that the laws and policies will not change between the time that the algo is trained and when it is used to make predictions. If the laws/policies change, then the model will need to be retrained because we made an assumption.

continuous variables are numeric variables that can have an infinite number of values between two values while categorical variable are qualitative variabless that are classified into distinct categories. This is useful to tell which type of algo to use, classifier or regressor.

A **Classifier Algorithm** is used if the label is a category variable. Some examples of the questions a classifier algo might answer are:

* Is this abnormal tissue growth a malignant tumor
* Based on the current weather conditions, will it rain tomorrow
* Based on the profile of a particular applicant, should their mortgage application be approved

A **Regressor algorithm** is used if the label is a continuous variable.

* Based on the current weather conditions, how much will it rain tomorrow
* What will the price of a particular home be with the given characteristics

## Understanding classification algorithms

* historical data is called labeled data
* production data that needs to be predicted is called unlabeled data

Within feature engineering, the process of selecting relevant data to the context of the problem is called **feature selection**.

**One hot encoding** is a process that transforms a categorical variable into a format the ML algos can understand better, namely into a continuous variable. `sklearn` has a method called `sklearn.preprocessing.OneHotEncoder()`. An example is that if a spreadsheet has a gender column for male/female, sklearn's onehotencoding method will transform that one categorical column into two numerical columns, male and female, where 1 represents male and 0 represents female.

**feature normalization** is a process of ensuring that the variables all fall into the line of 0-1. This helps with performance by ensuring that no individual feature dominates over the others. 

a **binary classifier** is the simplist example with it classifying it as either one thing or the other. For example, the algorithm can be trained to recognize if something is a hotdog or not a hotdogl.

A model may perform well in development and degrade in production. This is a case of the model being **overfitted** because it resembles the training data too closely and thus only performs well with that.

**Variance**, in the context of machine learning, refers to the amount by which the model's prediction would change when using different training data. A model with high variance pays a lot of attention to training data and tends to learn from noise and details. 

**Bias** is a term used to quantify how much our predictions deviate from true values.

Ideally both bias and variance would be low but real world scenarios often indicate that there must be a trade off with one being low and the other being high. We can visualize this in the following image.

![image](https://github.com/user-attachments/assets/ff7962dc-5761-42fb-917d-ac6d045678c5)

A **confusion matrix** can be used to evaluate an ML algorithm's performance. We can evaluate True Positives vs True negatives vs false positives vs false negatives on every situation.

![image](https://github.com/user-attachments/assets/3a4a6bab-107f-406e-bf27-881e485448fc)

Decision tree algorithms are popular in machine learning because they're easy to understand but have a downside that are subject to create artificial rules and become overfitting. This makes them ideal for classifier algorithms such as mortgage applications where an applicant may be likely to default on a number of loans due to historical data.

The **random tree algorithm** combines multiple decision trees together so that the final decision can be influenced by the number of trees. The final decision operates on a majority vote mentality. Each tree uses a random subset of the training data and the trees operate independently of one another. This is different than another technique known as **ensemble boosting** whereas it also use multiple models or decision trees but each one is built on the results of previous models in an attempt to correct past errors.

## Naive Bayes Algorithm

This is based on Bayes theorem which calculates the probability of an event given a previous event. This algo is useful when the dimensionality is high as in text classification and sentament analysis. It does make the naive assumption that these are independent. 

## Regression Algorithms for continuous variables

Suppose that we want to predict the temperature for the next two weeks based on historical data so we use a regressor algo. In simple terms, this is a models where we observe a change in the variable plotted on the y axis changes as the x axis changes. This often follows the slope intercept formula of `y=mx+b`. In linear regression, not all data will be able to fall on the `y=mx+b` line but we can visually approximate a line. y is the **dependent variable** that depends on x, the **independent variable**

![image](https://github.com/user-attachments/assets/fba6d70d-a0c0-4ac5-b26e-819b20f17d72)

## Multiple regression

When there are multiple independent variables, you need to use a tecnique called multiple regression. This is often more representative of the real world. For example, the price of a house (dependent variable) will often depends on numberous factors such as size, age, and location which are all independent variables. 

![image](https://github.com/user-attachments/assets/64afdc85-3291-49e6-968d-c6b764b4c13d)

regression analysis is often used to quantify relations between events and responses such as clinical drug trials or market research. However this leads to a limitation that this approach only works with numerical data.

## Gradiant boost regression

Gradiant boost regression will often have the best performance by combining regression analysis of looking at independent variables but the sequentially combines them into decision trees. Each tree will look at a different variable. For example, in the price of a house the first tree may look at size and then the next tree will look at location. The idea is that these trees will learn from the output of the previous one so the 2nd tree may notice that higher sizes will usually lead to a higher price and age will have less weight on the overall outcome. this is an iterative process.

# Chapter 8: Neural Network Algorithms

At it's most basic level a neural network is composed of several layers of neurons each doing its own task. The interative process of these layers of neurons processing based on information from the previous layer is what enables deep learning. In the human brain, neurons are made of the **dendrite** which provides the sensory information and the axon which acts as the long and slender part which transmits the signal through **synapses**, interconnecting tissue, to other neurons. This organic pipeline keeps going until it reaches the target muscle or gland. 

The idea of a neural network was first proposed back in 1957. However, limitations in hardware led to an **AI winter** in 1969. In the 90s, when hardware began to come very far down in price, high tech companies like Google decided to make AI the heart of their research again, leading to **AI Spring**. 

Traditional ML Algorithms looked at previously such as decision trees and linear regression work great for many important use cases but will fall short when the underlying patterns in the training dataset begin to become non-linear and multi-dimensional. This is where neural networks begin to shine as a very important tool for modeling.

For instance, image and speech recognition has input data (pixels and sound waves) which are non linear so traditional ML algorithms have trouble with this. 

a neural network consists on three types of layers

* input layer - the features are fed to the network as input
* hidden layer - there may be one (**simple neural network**) or many (**deep neural network**) and these are arrays of **activation functions** which performs the actual calculations. These hidden layers are organized in a hierarchical structure to allow for the extraction of progressively more abstract and nuanced features from the input.
* output layer - this is the final layer which gives the final result.

as we move deeper into the hidden layers, these layers begin to integrate the basic patterns detected by the lower layers, assembling them into more complex and meaningful structures. 

a neural network also consists of the following other concepts:

**loss function** - this provides the feedback signal used in various iterations of the learning process. This provides the deviation for a single example
**cost function** - the loss function as applied to a complete set of examples
**optimizer** - determines how the feedback from a loss function will be interpretted.
**weights** - correspond to the importance of each of the inputs of the training model.
**activation function** - the values will be multiplied by their weights and then aggregated and interpretted by the activation function

Using the above information, we can think of the difference between the expected output and the predicted output as the loss. 

## Popular tools

**Keras** is a popular, user friendly, and modular library for building neural networks and is often used with **tensorflow** an open source library provided by google to give Keras the backend deep learning capabilities. **Theano** is another backend deep learning engine that can be used with Keras as well as the **Microsoft Cognitive Toolkit (CNTK)**

These backend engines can all run on top of either the CPU with tools like **eigen** or GPU with tools like **CUDA** which was developed by NVIDIA. 

## Hyperparameters

a param whose value is chosen before the learning process starts like the activation function, number of hidden layers, or the number of neurons per layer.

**Functional API** - this allows us to architect models for acyclic graphs of layers. More complex models normally use this.

**Sequential API** - architect models for a linear stack of layers. This is better for uncomplicated data but is limited to only being able to hdnle one input tensor and one output tensor.

We can actually write tensorflow code in a number of higher level languages like c++ and python. In tensorflow terms, a **matrix** is a 2 dimensional array while a 3 dimensional array is a **3D tensor**. we use the term **rank** to refer to dimsionality so a scaler is rank 0, a vecotor is rank 1, and a matrix is rank 2. all of these data structures are referred to as **tensors**.

Downsampling is a process of reducing the **resolution** of your data meaning lessoning the complexity or dimensionality. 

## Generative Adversarial Networks

This is a class of neural networks developed in 2014 specializing in generating synthetic data. These can be used to generate things like profiles of people that don't exist. The training process of these models can be quite challenging leading to issues such as **mode collapse** where the the generator start producing limited varieties of samples. the quality of the generated data is also largely dependent of the quality and diversity of the input data. 

## Transfer Learning

These can be used for things like transcribing audio and detecting objects in videos/images. Transfering learning is mostly the idea that we don't create a new model from scratch and can instead modify an existing model. In the process, we may **freeze** existing branches/layers which have established learning so that we can allow others to grow. 

# Chapter 9: Natural language processing

NLP is a branch of ML that deals with the interaction between computers and natural language. 

a **corpus** is a large and structured collection of text or speech data that serves as a resource for NLP algos
**normalization** in NLP, this is a process of converting text into standardized form such as converting all characters to lowercase or removing punctuation.
**Tokenization** breaks down text into smaller parts called tokens so that the data is more structured.
**Named Entity Recognition** identifies and classifies entities within text like names and locations
**Stop words** - commonly used words like the which are filtered out of the algo as they don't contribute much meaning
**Stemming and lemmatization** - converting words to their dictionary form helping to analyze the core meaning

**word embeddings** used to translate words into numerical form
**language modeling** developing statistical models that can predict or generate sequences of words based on patterns found in the given corpus
**machine translation** automatingically translating text from one language to another using nlp techniques
**sentiment analysis** determing the attride or sentiment expressed in a piece of text by analyzing context

NLP algos use a preprocessing step to organize the messy corpus into structured data

after preprocessing the text using things like tokenization to structure the text, we move on to cleaning data which will involve normalization and stop words. Data cleaning might bring the text "Today, Ottawa is becomming cold again" to "today ottawa becom cold". Note the word "becom" this is because lemmatization may make it so the word is not proper english but can still be processed. 

Word embedding is now the process of taking a word like "apple" and translating that a vector something like `[.5, .9, .2]`. These numbers may represent different features of fruit such as sweetness acidity, and juiciness. The point of this is so that an algorthim can now understand this better. It may use another vector for a different fruit banana to be `[.2, .3, .3]`. Now the algorithm can plot these two points in 3d space and analyze the distance between them using euclidean distance or cosine similarity and analyze the similarity of the fruits.

# Chapter 10: Sequential models

Sequential models are a type of model in machine learning arranged in such a way that the output of one layer is the input of another layer. 

## Understanding sequential data

**Sequential data** is a specific type of data where the order matters because each element has a relational dependency on the element that preeceeded it. Here are the primary categories of sequential data.

* Time series Data - These are listed in time order so each value is dependent on the previous one.
* Textual Data - NLP references this data because the order of the data affects the meaning of the sentenses.
* Spatial-Temporal data - Like weather patterns or traffic flows in a specific geographic region, this data captures both spatial and temporal relationships.

## Types of sequential models

### One to many

A singular event or input can initiate the generation of an entire sequence. These are often part of **generative ai**, a burgeoning field of ai research which aims to create relavent content. Therefore, one to many sequential models will be used in generative ai applications such as writing poetry or generating art. Training these models is often time consuming and computationally expensive because the model must not only learn the relationship between input and output but also the patterns and structures in the generated content. 

## Many to one

The opposite of one to many, these models will take several inputs and translate it to one output. The applications of this are more for a rating system or sentiment analysis such as distilling loads of information into one review. Training these models involves teaching the model to be able to recognize the vital features among a whole slew of input so that it can be recognized accurately in the output.

### Many to many

This type of model will take sequential data as input and output sequential data. An example of this would be machine translation such as english to french. 

## Recurrent Neural Networks (RNNs)

**RNNs** are a special type of network that carry state from one step in the sequence to the next. Because of state, RNNs often provide a feedback loop back to itself which is where it gets the recurrent part of the name. Each loop of processing an element is referred to as a "run" so each run will retain some information from previous steps. ChatGPT and other LLMs are very similar to RNNs because they are neural networks that carry state from previous. However, LLMs are prone to **hallucinations** because they will often try to give an answer even if the answer isn't correct or doesn't make sense. Therefore, LLMs employ another technique called **teacher forcing** where we will often react to hallucinations by guiding the LLM back on the right track by saying that the answer is not correct and trying to offer hints by giving more context.

RNNs can be useed in translation of entire sentenses because to get it right, the RNN cannote translate each word in isolation, it needs to capture the context of the words that have been translated so far so that the RNN can translate the entire sentence correctly. 

The activation function `tanh` is often chosen to combat the **vanishing gradient problem**. This is a problem in the world of neural networks because as we keep traing our models, occasionally the gradient values which are the weight adjustments that we assign to certain features will drop. `tanh` is chosen as it acts as a buffer against this issue.

## Predicting with RNNs

1. Input preparation
2. Model utilization - now that you have the learned weights and biases from the training phase, it can be used in conjunction with the input data and processed through each layer of the network
3. Activation Functions - as in standard neural networks, activation functions transform the data as it moves through the layers
4. Generating predictions - the final prediction is generated after moving through the final layer
5. Interpretations - the predictions are then interpreted based on the task at hand such as classifying a sequence of text

There are two directions for RNNs. **Unidirectional RNNs** can only process data in one direction. This is a limitation because the RNN cannot look ahead to gain more context. **Bidirectional RNNs** can look both ways. If we're looking at a sentence "Cricket is a great ____, it is a sport played around the word", the unidirectional RNN might use the word insect because that is what a cricket is but a bidirectional RNN might use the word sport because it can look ahead to see the context that we're talking about playing cricket. 

A **gated neural network** (GRU) is a special type of RNN where it utilizes a gating mechanism to stop and think. It checks out the information and is able to select what it needs and forgets what it doesn't. By blending old information with this filtered approach, GRUs are much better at following long stories without getting lost. The aim of GRUs was to simplify **long short term memory** (LTSM) RNNs which were developed first in 1997 and are more complicated. GRUs were developed in 2014. 

GRUs also differ from standard neural networks in that they use a second activation function to decide whether or not to update the hidden state whereas standard neural networks will always do that. LTSMs take this a step further and instead have two states, the cell and hidden state. The **cell state** is designed to remember more long term information. 

# Advanced Sequential Models

**autoencoders** were introduced in early 2010 to revolutionize encoding and decoding tasks. Think of this as encoding the data into an internal representation, compressing, and then decoding the information into something that should closely match the original. 

![image](https://github.com/user-attachments/assets/003d3777-2c3d-4401-8f45-931983456f9e)


**Seq2seq Models** came about closer to the mid 2010s bring about new methodologies for translating text. Now we have an encoder, thought vector, and decoder. This model built on top of autoencoder in that it can work with translations which usually vary in length. Since this is typically a recurrent neural network, the thought vector is the final hidden state and is relayed to te decoder. 

The key difference in this model is that you have special tokens instructing the model. `<EOS>` signifies the end of the encoding process. `<GO>` is ent at the end of the encoding process once the thought vector is in place as input and indicates that the decoding process can begin. `<UNK>` replaces infrequent words in the input to make sure that the vocabulary remains manageable. `<PAD>` is used for padding shorter sequences standardizing sequence length during training.

Both autoencoders and seq2seq are great but run into issues with large amounts of text. This is why attention mechanisms which came about as the magnifying glass over specific parts of the text came into play.

**attention mechanism** came about is 2015 allowing models to focus on specific portions of text essentially placing more weight on them. 

2017 brought about the **transformer architecture** which fully leveraged attention mechanisms.

All of these advancements brought about **Large Language Models**.
