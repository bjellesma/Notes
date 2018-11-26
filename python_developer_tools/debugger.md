Python has a built in debugger called PDB

You insert two lines of code to start the debugger and then when that line is run, an interactive session will open with pdb

```py
import pdb
pdb.set_trace()
```

For example, in the following code

```py
print("hello world")
x = 2
import pdb
pdb.set_trace()
print("hello world again")
```

You receive a prompt such as the following when you run the code

```
-> print("hello world again")
(Pdb)

```

You can use special commands to see the location of the code and the current line being executed such as `l`

```
(Pdb) l
  1  	print("hello world")
      x = 2
  2  	import pdb
  3  	pdb.set_trace()
  4  ->	print("hello world again")
[EOF]
(Pdb)
```

and `n`

```
(Pdb) n
hello world again
--Return--
```

and `h` for help documentation

You are able to use any python code to analyze the program. For example, you can look at the values of current variables

```
(Pdb) print x
2
```

Some IDEs such as PyCharm will have integrated debuggers

More information is available [here](https://docs.python.org/2/library/pdb.html)
