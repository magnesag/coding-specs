# Python Style Guide

## General philosophy
* Explicit is better than implicit.

## Code formatting
Use `black` to format Python code.

## Naming conventions
For any resource, always use _descriptive_ names. For methods and
functions, make the name start or at least include a verb.

| Resource      | Naming style                  | Example           |
|---------------|-------------------------------|-------------------|
| Script        | Lowercase with underscores    | `run_foo.py`      |
| Module        | Camelcase, lower case initial | `myModule.py`     |
| Constants     | Uppercase with underscores    | `NO_CHANGE`       |
| Variables     | Lowercase with underscores    | `my_var`          |
| Callables     | Lowercase, with underscores   | `apply_filter()`  |
| Classes       | Camelcase, upper initial      | `MyClass()`       |

## Docstrings
Each file, class, method and function has to feature its own docstring.

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

## Magic numbers
Never make use of magic numbers - keep the code readable and maintainable.

## Testing
Write unittests for your code, or even better use test-driven development.
Place the tests close to the source, i.e. in each source-containg subfolder,
place a `test/` folder containg the tests related to the source files at
that location.

Write your tests using Python's builtin `unittest` module.
