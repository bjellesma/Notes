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

Like the bubble sort, the time complexity can be quadratic in the worst case. However, the shell sort is more optimized for data sets of less than 6000 elements. This makes the algo a good candidate for medium sized data sets.

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

**Linear Search** is just a brute force search for the item in the list and, if not found, keep going. The advantage is that this doesn't require the list to be presorted. The disadvantage is that this can be very slow in the worst case if the item we're looking for is at the end.
