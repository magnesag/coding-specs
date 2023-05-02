# C Style Guide

## Naming conventions
For any resource, always use _descriptive_ names. For functions, make
the name include a verb. In order to prevent excessive namespace pollution,
define and use an acronym prefix for each library you write. For example,
in the `superAwesomeLibrary.h`, one shall prepend all public members
with `sal_`. Private (`static`) members can be left without prefix.

| Resource      | Naming style                                  | Example               |
|---------------|-----------------------------------------------|-----------------------|
| File          | Camelcase, lower case initial                 | `myLib.c`             |
| Constants     | Uppercase with underscores                    | `NO_CHANGE`           |
| `#define`     | Uppercase with underscores                    | `PRECOMP_DEF`         |
| Enum vals     | Uppercase with underscores                    | `enum {ZERO, ONE};`   |
| Variables     | Lowercase with underscores                    | `my_var`              |
| Functions     | Lowercase, with underscores                   | `apply_filter()`      |
| Types         | Lowercase, with underscores, trailing `_t`    | `new_thing_t`         |
| Void pointers | Lowercase, with underscoder, leadinfg `_`     | `_any_data`           |

### Void Pointers
Void pointers are both, a blessing and a curse at the same time.
They enable generic programming in C at the cost of some losses
in terms of type checking - as if C wasn't unsafe enough. While
void pointers are not discouraged, it is good practice to name
instances thereof in a specific way. At Magnes they shall be named
with a leading underscore.
This has a double benefit:
1. A leading inderscore variable is most probably a void pointer (implicit meaning)
2. When casting coid poiters to some usable type, the same variable name, without leading undeerscore can be used

## Integer types
Always use the standard integers with explicit size defined in
`stdint.h`. Sole exception are `char *` for text strings, but even
those should be kept at a minimum.

## Include guards
Use dunder precompiler definitions as include guards, i.e. if the header
`myHead.h` is to be included anywhere (and it will), put all of its code
as follows:
```C
/**
 * @file myHead.h
 * <Rest of the file docstring>
 */
#ifndef __MY_HEAD_H__
#define __MY_HEAD_H__

/* All the inclusions and definitions go here */

#endif /** __MY_HEAD_H__ */
```

## Include instructions
1. Group the `#include`s by type, starting from the standard libraries (the ones included with `<>`)
2. Sort the include statements alphabetically within each group
3. If some include statements require a specific sequence, use comments/notes to enforce and clarify the sequence.

## Documentation
Source code documentation is generated using Doxygen.

Document your code by providing docstrings to each file, function, and global
variable/definition. Reduce in-code comments to the bare minimum and spare
such comments for unusual code. Make sure to mark such comments with an `@note`
to avoid Doxygen from ignoring the comment in the generated documentation.

## Testing
Write unittests for as much components as possible, ideally use
test-driven development. Use `unity` as testing environment.