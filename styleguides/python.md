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

| Resource        | Naming style                                      | Example           |
| --------        | ------------                                      | -------           |
| Script          | Lowercase with underscores                        | `run_foo.py`      |
| Module          | Camelcase, lower case initial                     | `myModule.py`     |
| Constants       | Uppercase with underscores                        | `NO_CHANGE`       |
| Variables       | Lowercase with underscores                        | `my_var`          |
| Attributes      | Lowercase with underscores                        | `my_attr`         |
| Callables       | Lowercase, with underscores                       | `apply_filter()`  |
| Classes         | Camelcase, upper initial                          | `MyClass()`       |
| Private memeber | Leading underscore                                | `_*`              |

### A Note on Privacy
Python does not really have the concepts _private_ and _public_.
In classes, there is a way of obfuscating attributes using a leading double-underscore, but this usually
introduces more issues than it solves problems, in particular when inheritance is used.

Stick to the standard convention that a _leading underscore_ denotes a "private" member.
So, in a class attirbutes and methods starting with a leading underscore shall never 
be accessed directly from outside the instance; in a module, functions starting with a
leading underscore shall never be called from outside the module (i.e. after import).

The exception to this rule is testing: for testing purposes direct access is allowed.

```python
class Square:
    """!A square

    @param side_len The square's side length
    """

    def __init__(self, side_len: float):
        self._area: float = 0
        self._side = value
        self.update_area()

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, new: float):
        """!Side setter

        @param new New side length
        """
        self._side = new
        self.update_area()

    def get_area(self) -> float:
        """!Non-property attribute getter for area

        @note Properties should be preferred over getter methods.

        @return Value of _area
        """
        return self._area

    def _update_area(self):
        """!Update the value of _area"""
        self._area = self._side * 2

plaza = Square(3.14)
x = plaza.side
plaza.side = 2 * x
p_area = thing.get_area()
# NEVER DO: y = thing._area
# NEVER DO: thing._update_area()
```

## Docstrings and comments
Each file, class, method and function has to feature its own docstring. The
docstrings shall include a brief description of what they are referring to
and, for methods and functions, include a list of the parameters and return
values (if any).

Save the special tags such as `[@]note` for special notes, not the general
description.

In-code comments shall be kept to a minimum and only be used where special
attention is needed or where some not-so-straightforward code is implemented.

Make sure to use a proper documentation generation tool, and align the docstring
style to the used tool. Valid options include Doxygen and Sphinx.

## Annotations and type-hints
Annotate your source code in terms of type-hints and only use in-code comments (annotations)
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
* The shebang line `#!/usr/bin/env python`

## Import statements
* Group `import` statements by module types - keep one empty line inbetween groups:
  1. Builtin modules
  2. `pip` modules
  3. Custom/own modules
* Keep each group ordered alphabetically

For all of your source code, make sure to have a `__init__.py` in each subfolder
containg Python source which will potentially be imported/used from somewhere else.

Make sure to delete any unused imports.

## Magic numbers
Never make use of magic numbers - keep the code readable, maintainable, and
configurable. This does not only apply to numerical values, but also to other
types such as strings.

Rely on tools such as configuration classes/modules and enumerations for
the definitions.

## Environments
At the bare minimum, use virtual environments for Python projects. Even better is
the usage of Python project tools relying on `pyproject.toml`. `hatch` and `setuptools`
(alongside `build` are the preferred tools).

## Testing
Write unittests for your code, or even better use test-driven development.
Place the tests close to the source, i.e. in each source-containg subfolder,
place a `test/` folder containg the tests related to the source files at
that location.
Alternatively, have a `tests/` directory at root, and replicate the module's
tree within the `tests/` directory, and collect all tests in it.

Write your tests eithe using Python's builtin `unittest` module or using `pytest`.
Test shall be runnable by calling `python -m unittest discover -vv` or `pytest . -vv`
or `python -m pytest . -vv`
