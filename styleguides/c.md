# C Style Guide

## General Philosophy
- Explicit is better than implicit.
- Avoid useless operations.
- Do not over-optimize using black magic.
- Prefer readable and predictable code over clever code.
- Fix root causes, not symptoms.

## Naming Conventions
For any resource, always use descriptive names. For functions, make the name
include a verb.

Because C has no real namespacing, all public symbols shall use a short prefix.
In this repository, the practical namespace prefix is the source-file acronym.

For example, in `nushuTimeUtil.h`, public functions and variables should be
prefixed with `ntu_`.

Private (`static`) members can be left without a public prefix if the scope is
strictly local to the source file.

| Resource      | Naming style                               | Example               |
|---------------|--------------------------------------------|-----------------------|
| File          | lower camel case, lower-case initial       | `myLib.c`             |
| Main file     | fixed name                                 | `main.c`              |
| Constants     | uppercase with underscores                 | `NO_CHANGE`           |
| `#define`     | uppercase with underscores                 | `PRECOMP_DEF`         |
| Enum values   | uppercase with underscores                 | `enum {ZERO, ONE};`   |
| Variables     | lowercase with underscores                 | `my_var`              |
| Functions     | lowercase with underscores                 | `apply_filter()`      |
| Types         | lowercase with underscores, trailing `_t`  | `new_thing_t`         |
| Void pointers | lowercase with underscores, leading `_`    | `_any_data`           |

### Function Naming
Functions shall use lowercase words connected by underscores.

Use explicit names that say what the function does. Prefer verbs and proper
domain names over vague verbs.

Good:
```c
predict_gait_phase();
predict_activity_by_cnn();
```

Avoid:
```c
predict();
process();
handle();
```

### Variables Naming
Variables follow the same lowercase-with-underscores convention, but avoid verbs
in variable names.

Use file-private variables (`static`) where needed. If external access is
required, prefer controlled access through `get_<variable>()` and, where needed,
`set_<variable>()`.

Use `volatile` where necessary to prevent the compiler from optimizing away
state that may change outside the current execution flow.

### Void Pointers
Void pointers are useful, but they reduce type safety. They are allowed, but
must be named in a specific way.

At Magnes, `void *` instances shall use a leading underscore. This has two
benefits:
1. A leading underscore strongly suggests the variable is a `void *`
2. After casting, the same name without the underscore can be reused

Example:
```c
int some_function(void *_param1, void *_param2) {
  float *param1 = (float *)_param1;
  float *param2 = (float *)_param2;

  /* ... use param1 and param2 ... */
}
```

## Bracing Style
Use the one true brace style (OTBS), as enforced by the repository formatter.

The `.clang-format` file at the repository root is the formatting source of
truth. It is based on Google style and currently uses right-aligned pointers.

Example:
```c
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>

int main(void) {
  uint32_t a = 1034;
  for (uint32_t ii = 0; ii < 100; ++ii) {
    if (a % 2 == 0) {
      a /= 2;
    } else {
      a *= 3;
      a += 1;
    }
    printf("%" PRIu32 "\n", a);
  }
  return 0;
}
```

## Integer Types
Always prefer standard integer types with explicit width from `stdint.h`, e.g.
`uint8_t`, `int16_t`, `uint32_t`.

The main exception is textual data, where `char *` remains appropriate.

## Include Guards
Use dunder preprocessor definitions as include guards.

If the header is `myHead.h`, structure it like this:
```c
/**
 * @file myHead.h
 * <Rest of the file docstring>
 */
#ifndef __MY_HEAD_H__
#define __MY_HEAD_H__

/* All inclusions and definitions go here */

#endif /* __MY_HEAD_H__ */
```

## Include Instructions
1. Group includes by type, starting with standard libraries (`<...>`)
2. Then include ESP-IDF or other external-library headers
3. Then include project-local headers
4. Sort includes alphabetically within each group
5. If a specific order is required, add a short note explaining why

Example:
```c
#include <stdint.h>
#include <stdio.h>

#include "esp_log.h"

#include "nushuTimeUtil.h"
#include "nushuWiFiCommon.h"
```

## Function Arguments
Only pass scalar data by value, e.g. integers, floats, enums, booleans, and
pointers.

Pass arrays, structs, unions, and other composite data by reference.

This avoids unnecessary copying and makes data ownership clearer.

## Data-Centric Architecture
Favor a data-centric architecture. Let the data model define the software
structure, not the other way around.

Define the relevant composite data structures first, then build the behavior
around those explicit contracts.

## Logging
Use ESP logging macros such as `ESP_LOGE()`, `ESP_LOGW()`, `ESP_LOGI()`, and
`ESP_LOGD()` for output.

Define log tags via uppercase macros.

Example:
```c
#define DRIVER_XY_TAG "[Driver XY]"
```

## Pragmas and Literals
Preprocessor pragmas and literals defined through them shall be uppercase with
underscores.

Example:
```c
#define MY_PRAGMA
```

## Line Length
Avoid excessively long lines. As a rule of thumb, stay within about 100 columns.

Prefer splitting long expressions over forcing dense unreadable code.

## Magic Numbers
Avoid magic numbers.

Configuration numbers have meaning and should be named explicitly. Include units
in the name when relevant.

Example:
```c
#define MAIN_TASK_MEMORY_BYTES 2048
#define READ_TASK_MEMORY_BYTES 1024
```

Such definitions can be collected in dedicated configuration headers, e.g.
`<module>Config.h`.

## Data Exchange Between Modules
Minimize the use of `extern` variables and functions. They create implicit
dependencies and pollute the global namespace.

## Nonos
- Do not use `goto` except for cleanup/error-unwind patterns at the end of a function.
- Do not use circular dependencies.
- Do not make high-level code depend on low-level implementation details.
- Do not leave commented-out code in the codebase once development is done.

For example, an estimator should not care which concrete IC provides the data it
uses.

## Documentation
Source code documentation is generated using Doxygen.

Document:
- each source file
- each header file
- each public function
- each global variable or global definition

Functions shall be documented where their prototype is declared. If a function
has no prototype, document it at the implementation site.

Keep inline comments to a minimum. Prefer self-explanatory naming. Use inline
comments only for unusual behavior or non-obvious constraints. Mark such
comments with `@note` where appropriate so they remain visible in generated
documentation.

## Testing
Write unit tests for as much code as possible. Unity is the required test
framework for C code in this project.

Use both:
- on-device tests
- host-side tests, where abstraction makes them possible

Test-driven development is encouraged.

If a function cannot reasonably be tested in isolation, write an ignored test
with a clear reason.

Example:
```c
TEST_CASE("Test SPI transaction", SPI_DRIVER_TEST_TAG) {
  TEST_IGNORE_MESSAGE(
      "SPI transaction call requires IC with which to "
      "communicate - function is tested within SPI-IC-driver tests");
}
```
