# C Style Guide

## General philosophy
* Explicit is better than implicit.
* Avoid useless operations.
* Do not over-optimize using blackmagic

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

Let us see a typical example (imagine this function to be of a generic signature type that many actors have to share):
```C
int some_function( void *_param1, void *_param2) {
  float *param1 = (float *)_param1;
  float *param2 = (float *)_param2;
  
  // ... rest of the function using param1 and param2
}
```

## Bracing style
Conform to the one true brace style (OTBS) for braces.

```c
#include <stdint.h>
#include <stdio.h>

int main(void) {
  uint32_t a = 1034;
  for (uint32_t ii = 0; ii < 100; ++ii) {
    if (a % 2 == 0) {
      a /= 2;
    } else {
      a *= 3;
      a += 1
    }
    printf("%u\n", a);
  }
  return 0;
}
```

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

## Function Arguments
Only pass scalar data by value (`int`s, `float`s, `enum`s). Pass all other variables
by reference (i.e. any array, `struct`, `union`).

## Datacentric Architecture
Favour a datacentric architectural approach - make your data define your SW, not
the other way arouynd.
In order to achieve this, define composite data-structures and build your SW
on these definitions.

## Documentation
Source code documentation is generated using Doxygen.

Document your code by providing docstrings to each file, function, and global
variable/definition. Reduce in-code comments to the bare minimum and spare
such comments for unusual code. Make sure to mark such comments with an `@note`
to avoid Doxygen from ignoring the comment in the generated documentation.

## Testing
Write unittests for as much components as possible, ideally use
test-driven development. Use `unity` as testing environment.
