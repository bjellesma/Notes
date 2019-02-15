Class objects will have special underscore methods associated with them like `__dict__`

**__dict__** - returns a dictionary representation of class attributes and methods. Though direct access to __dict__ can be useful
for more advanced programming, it is often safer to use `getattr()`, `hasattr()`, `delattr()`, and `setattr()`. You are able to override
these functions with surrounding __ like `__getattr__`
