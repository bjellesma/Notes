## setuptools

Setup Tools is a python package that you can use to package your project so that others are then able to install it with pip.

For the following example of how to create your package, we use the following tree structure

.
├── project
|   ├── subproject
|   |   ├──new.py
|   ├── sample.py
|   └── readme.md
├── node_modules
|   ├── sample.json
|   └── header.html
├── templates
|   ├── default.html
|   └── post.html

1. Create setup.py in the top level of your project with the following code

```python

from setuptools import setup

setup(name='sample',
      version='0.1',
      description='just a simple project'
      author='me',
      author_email='me@me.com'
      packages=['project', 'project.subproject', 'templates'],
      )
      
__author__=me
```

*NOTE: we need to list project.subproject as one of the packages even though it is in the project directory*

2. On the terminal, we use the following command to create the package

```bash
python setup.py sdist
```

3. Notice that we now have a new dist directory with the file `sample-0.1.tar.gz`, this is the compressed package that you can now ship to others

*NOTE: unzipping these file reveals all of the source python files, we have not created an exe or dmg file

4. From another user's perspective, they can now install the package with the following

```bash
pip install sample-0.1.tar.gz
```

If your package depends on other packages (as many projects do), you can also use the `install_requires` keyword argument

```python
setup(...
      install_requires=[
        'Werkzeug>=0.7'
       ],
       ...
       ]
)
```

This argument specifies that anyone who downloads your package will also automatically download a version of Werkzeug of 0.7 or higher

Pypa (Python Packaging Authority) has a sample project [here](https://github.com/pypa/sampleproject)

## Upload your package to PyPI

You can upload your package to PyPI (Python Packaging Index) so that users can use `pip` in the way that they are familiar with. You need two commands to do this.

```bash
python setup.py register
```

This code will allow you to login or register as a new user on PyPI so that a URL can be generate for your project.

```bash
python setup.py sdist upload
```

This will upload the actual files of your package

## Distributing executables

Although setuptools provides a way to create executables by using the `entry_points` keyword argument, this requires the end user to have their own python interpretter.

The preferred way to make standalone executables for end users without needing a python interpretter is with PyInstaller

