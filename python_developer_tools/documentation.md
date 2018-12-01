## Docstrings

* PEP257 is the standard for conventions

* the docstring muust be the first line in the module, class, or function
Here's an example of a singleline docstring

```python
def function(a, b):
  """Do X and return a list."""
```

One line docstrings should be used only for really obvious cases

Here's an example of a multiline docstring

```python
def complex(real=0.0, imag=0.0):
  """Form a complex number

  Keyword Arguments
  real - the real part (default 0.0)
  imag - the imaginary part (default 0.0)
  """
```

More information can be found about [PEP 257](https://www.python.org/dev/peps/pep-0257/)

## ReStructured Text

[Here](https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html) is a great resource for learning ReStructured

* Like python, rst is very sensative to indentation

* Paragraphs must be seperated by a single line

* Code is done with double backticks to surround the code

* If you're familiar with markdown, rst is the same thing

* In order to create links to other rst files, we use the following code to create the link

```rst
:ref:`api`
```

  * and the following code is the directive of where the links goes

  ```rst
  .. _api:
  ```

* For creating a reference to a class or function, you will use the following code

```rst
:class: `Maze`
:func:`generate`
```

This code is very similar to references for other rst files. The following code is the directive of where the code is to lead. Notice the addition of the autodoc

```rst
.. class:: Maze
.. function:: generate
.. autofunction:: generate()
```

* Autodocing requires you to change the autodocing directory in your `conf.py` file

The following example changes autodocing to look in the parent directory for the code
```python
sys.path.insert(0, os.path.abspath('..'))
```

* You can use rst in your docstrings so that autodocing will convert them. For example:

def complex(real=0.0, imag=0.0):
  """Form a complex number

  Keyword Arguments
  :param: real - the real part (default 0.0)
  :param: imag - the imaginary part (default 0.0)

  Here is a link to :func:`generate` function within the docstring
  """
```
