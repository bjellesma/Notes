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

