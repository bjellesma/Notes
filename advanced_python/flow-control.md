# While Else 

You can use a loop as while else so that the condition continues running if truthy and the else clause is executed only if and when the condition becomes falsy

```py
while condition:
    pass
else:
    pass
```

Typically, these loops are used if the while loop is empty and would normally be skipped over. In this way, our else clause would allow us to fail gracefully.

For example, we could use a while loop to traverse a user defined list. Normally, the loop would only execute if there are item still in the list.
Therefore, if the user defines an empty list, the loop will be skipped over giving the user no indication of why.

```py
while items:
  print("item found")
else:
  print("empty list or list completed execution!")
```

Often, it is far easier to understand a function

```py
def ensure_has_divisor(items, divisor):
    for item in items:
        if item % divisor == 0:
            return item
    items.append(divisor)
    return divisor
```

# Try Else 

try else constructs can be useful if we're trying to handle an exception on one block of
code and not another. In the following code, we will handle the OSError if it is raise
when we attempt to open the file but we will not handle the exception when iterating over the file,
which can also raise an OSError.

```py
try:
    f = open(filename, 'r')
except OSError:
    print("File could not be opened for reading")
else:
    print('Number of lines', sum(1 for line in f))
    f.close()
```

# Emulated Switch Statement

Python doesn't have native support for a switch statement but we can use a dictionary 
of values for our conditions.

```py
command = input()

actions = {
    'N': north(),
    'S': south(),
    'E': east(),
    'W': west()
}
try:
    command = action[command]
except KeyError:
    print('command not understood')
```
