* PEP* recommends the following code standards
  * 4 spaces per level
  * line length should be a max of 79 characters
  * 2 blank lines between classes
  * 1 blank line between methods inside of a class
  * Naming
    * Modules: short, lowercase names
    * Classes: CapitalizedNames
    * functions, variables, methods: lowercase_with_underscores
    * constants: ALL_CAPS
    * Non public names: start with underscore

    ```python
    self._size = 2
    ```

* You can configure a pylint configuration file with the following command `pylint --generate-rcfile > pylintrc`
