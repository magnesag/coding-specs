# Python Style Guide

## General philosophy
* Explicit is better than implicit.
* Simple is better than complicated.
* Be SOLID, use abstractions, and be data-centric.

## Code formatting
Use `black` to format Python code.

## Naming conventions
For any resource, always use _descriptive_ names. For methods and
functions, make the name start or at least include a verb.

| Resource      | Naming style                                      | Example           |
|---------------|---------------------------------------------------|-------------------|
| Script        | Lowercase with underscores                        | `run_foo.py`      |
| Module        | Camelcase, lower case initial                     | `myModule.py`     |
| Constants     | Uppercase with underscores                        | `NO_CHANGE`       |
| Variables     | Lowercase with underscores                        | `my_var`          |
| Attributes    | Lowercase with underscores and leading underscore | `_my_attr`        |
| Callables     | Lowercase, with underscores                       | `apply_filter()`  |
| Classes       | Camelcase, upper initial                          | `MyClass()`       |

### A Note on Attributes
Python does not really have the concepts _private_ and _public_ for attributes and methods.
There is a way of obfuscating attributes using a leading double-underscore, but this usually
introduces more issues than it solves problems, in particular when inheritance is used.
Thus, the following convention shall be followed:
* All attributes shall be _regarded_ as private, i.e. they shall not be accessed _directly_ from outside the object,
instead _getter_ and _setter_ methods shall be implemented.
* If an attribute is needed to be "public", it shall be defined as a `@property`, whose name shall be the one of the
reflected attribute, without the leading underscore.

In general, methods should be regarded as public.

```python
class Thing:
    """!A thing

    @param value The thing's value
    """

    def __init__(self, value: float):
      self._y = 0
      self._x = value
      self.update_y()

    @property
    def x(self) -> float:
      """!x-getter"""
      return self._x

    @x.setter
    def x(self, new: float):
      """!x-setter

      @param new New value for the thing
      """
      self._x = new
      self.update_y()

    def get_y(self) -> float:
      """!Non-property attribute getter for y

      @return Value of _y
      """
      return self._y

    def update_y(self):
      """!Update the value of _y"""
      self._y = self._x * 2

thing = Thing(3.14)
x = thing.x
thing.x = 2 * x
y = thing.get_y()
# NEVER DO: y = thing._y
```

## Docstrings and comments
Each file, class, method and function has to feature its own docstring. The
docstrings shall include a brief description of what they are referring to
and, for methods and functions, include a list of the parameters and return
values (if any).

Save the doxygen tags such as `@note` for special notes, not the general
description.

In-code comments shall be kept to a minimum and only be used where special
attention is needed or where some not-so-straightforward code is implemented.

## Annotations and type-hints
Annotate your source code and only use in-code comments (annotations)
when the code is somewhat special (e.g. mark the `else` of a `for-else`)
instruction as belonging to the `for`. Otherwise avoid any in-code
comments and aim at self-explaining code making use of descriptive
naming.

## Executables and `main()`
Any Python file that is expected to be called on its own must include
a `if __name__ == "__main__":` conditional section which is to be run
when executing the file.
Ideally, each executable file also features:
* A `main()` function, which is called in the "main" section
* The shebang line `#!/usr/bin/env python3`

## Import statements
* Group `import` statements by module types - keep one empty line inbetween groups:
  1. Builtin modules
  2. `pip` modules
  3. Custom/own modules
* Keep each group ordered alphabetically

For all of your source code, make sure to have a `__init__.py` in each subfolder
containg Python source which will potentially be imported/used from somewhere else.

## Magic numbers
Never make use of magic numbers - keep the code readable, maintainable, and
configurable.

## Testing
Write unittests for your code, or even better use test-driven development.
Place the tests close to the source, i.e. in each source-containg subfolder,
place a `test/` folder containg the tests related to the source files at
that location.

Write your tests using Python's builtin `unittest` module. Test shall be
runnable by calling `python3 -m unittest discover -vv`
