To make attributes private to a class and only let people set/get the value, we can use **Properties** by using the decorator @name.setter

This setter property will prevent a user using this library from setting the value like 

```py
test_object.name = 7
```

# Debugging

For better debugging capabilities, we can use `repr()` instead of `print()`. print() is meant to be used for readable string representation whereas repr() is meant to be used for debugging and will give representations of **string literals**

