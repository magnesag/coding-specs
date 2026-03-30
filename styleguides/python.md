# Python Style Guide

## General philosophy
- Explicit is better than implicit.
- Simple is better than complicated.
- Be SOLID, use abstractions, and be data-centric.

## Package and Project Management
- Versioning and dependencies shall be uniquely managed through a `pyproject.toml` file.
- Use `uv` for package and project management.
  - Use dependency groups: only add to `dependencies` those packages that are needed
  in the production code.
  - Place development dependencies, e.g. testing frameworks, in the `dev` group.
- Always favor well-known third party-libraries over obscure and unknown libraries.
- Make sure to publish packages to the correct index.

### Third-party packages whitelist
These packages can always be used in Python projects
- Numpy
- Scipy
- Matplotlib
- Pandas
- Bleak
- Scikit-learn
- PyTorch
- TensorFlow
- Requests
- Httpx
- Aiohttp

Development packages
- Pytest
- Hypothesis
- Sphinx

Before using a package not from these lists, check if what you need the other
package for cannot be done with one or more of the above. Third-party packages
are always linked to some risk.

## Code formatting
- Use `ruff` or `black` to format Python code.
- Make sure to format your code before committing (avoid format diffs in MRs).

## Naming conventions
For any resource, always use _descriptive_ names. For methods and
functions, make the name start or at least include a verb.

| Resource        | Naming style                                      | Example           |
| --------        | ------------                                      | -------           |
| Script          | Lowercase with underscores                        | `run_foo.py`      |
| Module          | Camelcase, lower case initial                     | `myModule.py`     |
| Constants       | Uppercase with underscores                        | `NO_CHANGE`       |
| Variables       | Lowercase with underscores                        | `my_var`          |
| Attributes      | Lowercase with underscores and leading underscore | `my_attr`         |
| Callables       | Lowercase, with underscores                       | `apply_filter()`  |
| Classes         | Camelcase, upper initial                          | `MyClass()`       |
| Private member  | Prepend underscore                                | `_hidden`         |

**Notes and exceptions**
- Enumeration classes (inheriting from some `enum` object), may use the constants' style (uppercase with underscores).
- As enumerations define object of some type, make sure to use singular names and not plural ones, e.g. define `class Currency(enum.Enum): ...` and _not_ `class Currencies(enum.Enum)`. The former does lead to cleaner and more readable type annotations.
- Private member convention can be applied to any: attributes, methods, and functions.
- These conventions allow for encoding/decoding of what things are, based on their naming style.

### A Note on private members
Python does not really have the concepts _private_ and _public_ for attributes, methods, or functions.
There is a way of obfuscating attributes using a leading double-underscore, but this usually
introduces more issues than it solves problems, in particular when inheritance is used.
Thus, the following convention shall be followed:
- All attributes shall be _regarded_ as private, i.e. they shall not be accessed _directly_ from outside the object.
- If an attribute is needed to be "public", it shall be defined as a `@property`, whose name shall be the one of the
reflected attribute, without the leading underscore, and the needed setter and getter methods are to be implemented.

```python
class Thing:
    """A thing

    Parameters
    ----------
    value : float
      The thing's value
    """

    def __init__(self, value: float):
      self._x = value


    @property
    def x(self) -> float:
      """x-getter

      Returns
      -------
      float
        Value of x
      """
      return self._x

    @x.setter
    def x(self, new: float):
      """x-setter

      Parameters
      ----------
      new : float
        New value for the thing
      """
      self._x = new


thing = Thing(3.14)
x = thing.x
thing.x = 2 * x
# NEVER DO: x = thing._x
```

## Documentation
### Docstrings and comments
Each file, class, method and function has to feature its own docstring. The
docstrings shall include a brief description of what they are referring to
and, for methods and functions, include a list of the parameters, return
values (if any), and exceptions (raises, if any).

Docstrings shall be written using the Numpy-docstring style (inspired by
Google's style).

The file docstring shall include an `Author:` list and a `Copyright:` notice.
Assume the author to be called `Primo Coder` (first name Primo, last name Coder),
and the file under consideration to be created in 2026, then the file
docstring would look something like:

```python
"""
Module for the computation of happiness
=======================================

{description}

Author:
    P. Coder
Copyright:
    Magnes AG, (C) 2026.
"""
```

Other (future) contributors can then enter their name on new lines after `P. Coder`
as they contribute to the source. The rationale behind this requirement is that
it helps future developers to gain rapid context to the source - one immediately
knows how old the source is (at most) and who the main contact point for
questions should be (without needing to check the file history in source version
control).

In-code comments shall be kept to a minimum and only be used where special
attention is needed or where some not-so-straightforward code is implemented.

### Annotations and type-hints
Annotate your source code and only use in-code comments (annotations)
when the code is somewhat special (e.g. mark the `else` of a `for-else`)
instruction as belonging to the `for`. Otherwise, avoid any in-code
comments and aim at self-explaining code making use of descriptive
naming.

Make sure specify type annotations for arguments and return types. If
a function does not return anything, `-> None` can be omitted. Define
types (and type-aliases) as needed.

### Design and reporting
Keep a README.md at the repo's root. Make sure to keep it in sync with the
actual implementation.

Generate code documentation from the docstrings and annotations, using suitable
tools such as Sphinx. All the documentation shall live in a `doc/` (or `docs/`)
directory at the repo's root.

Use design docs to plan changes. These may be simple markdown files specifying
the features that are to be implemented. Place them at `doc/design/{feature}/`

Design docs are to be git-tracked. Automatically generated documentation may
not be tracked.


## Import statements
- Group `import` statements by module types - keep one empty line in-between groups:
  1. Builtin modules
  2. Third party modules, i.e. project dependencies installed from public PyPIs.
  3. Custom external modules, i.e. project dependencies installed via private PyPIs.
  4. Custom local modules (project-internal dependencies)
- Keep each group ordered alphabetically

For all of your codebase, make sure to have a `__init__.py` in each subfolder
containing Python source which will potentially be imported/used from somewhere else.

## Executables and `main()`
Any Python file that is expected to be called on its own must include
a `if __name__ == "__main__":` conditional section which is to be run
when executing the file.
Ideally, each executable file also features:
- A `main()` function, which is called in the "main" section

Scripts shall be executable from the repo's root, i.e. the script `script.py` located at
`some/path/repo/mod/x/script.py` shall run with
```bash
uv run mod/x/script.py
```
or
```bash
uv run -m mod.x.script
```

## Magic numbers
Never make use of magic numbers - keep the code readable, maintainable, and
configurable. Define your configuration parameters as human-readable structures.
Several options are available for this:
- Constant variables, e.g. `LINE_HEIGHT`
- Enumerations (for cases where a fixed number of options are viable, e.g. whenever a `Literal` - consider providing mixins for further control)
- Configuration classes (either as bare classes or dataclasses)

Example bare configuration class
```python
class CFG:
    DIR_NAME = os.path.dirname(__file__)

# Use as CFG.DIR_NAME in code
```

## Logging and string formatting
Use f-strings to format strings, not C-style formatting, nor `.format()`.
Use the `logging` module to generate and format log entries. Define one logger
per file using
```python
import logging

...

logger = logging.getLogger(__name__)

...

logger.info(f"Entered stage {ii:d}/{n_stages:d}")
```

## Testing
Write unit tests for your code, or even better use test-driven development,
i.e. define and design the interface of your package first, then implement
(failing) tests based on the interface, covering standard usage and edge
cases, then implement the functions to make the tests pass.

At a minimum, make sure to test the good-weather scenarios and the obvious
edge cases.

Use `pytest` as testing framework and place all tests in a parallel tree
mapping the source tree rooted at the same level as the main source.
For example, the tests for the module `mod` whose source is located
at `some/path/repo/mod/`, shall be located at `some/path/repo/tests/`.
Consider using `hypothesis` to test across ranges of values.

## Legacy styles
The following styles are to be considered legacy and shall be replaced with
the corresponding new style defined above:
- Docstrings in Doxygen format
- Tests close to the source