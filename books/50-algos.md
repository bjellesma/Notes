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
