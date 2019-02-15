Class objects will have special underscore methods associated with them like `__dict__`

**__dict__** - returns a dictionary representation of class attributes and methods. Though direct access to __dict__ can be useful
for more advanced programming, it is often safer to use `getattr()`, `hasattr()`, `delattr()`, and `setattr()`. You are able to override
these functions with surrounding __ like `__getattr__`

Using this knowledge, you can create a class that is **private** in nature by setting `__setattr__` to raise an error when it is invoked. You would also do this with `__delattr__`.

You can use `vars()` to get the attributes of a class in much the same way as `__dict__()`. The difference is that vars() will return an immutable dictionary while `__dict__()` will return a mutable dictionary. Therefore, if you are planning to set the attributes dictionary, you should use `__dict__()` whereas if you are just accessing attributes, you should use `vars()`.

Keep in mind that if you use `vars()` you also need to include self like `vars(self)` whereas with `__dict()__`, we'd use `self.__dict()__`.

`__getattr__()` is only invoked if the class cannot access the attributes with `__getattribute__()`. Therefore, if we wish to override the access of attributes, we should ovveride `__getattribes__()`.





