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

