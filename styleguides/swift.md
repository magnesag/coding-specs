# Swift Style Guide

## Naming conventions
* Use CamelCase for types (classes, structs, enums, and protocols) and 
lowerCamelCase for everything else (properties, methods, functions, and variables).
* Clarity is more important than brevity. Include all the words needed to avoid 
ambiguity for a person reading code where the name is used.
* Choose parameter names to serve documentation. Even though parameter names do not 
appear at a function or method’s point of use, they play an important explanatory role.

## General Formatting

### Braces
* In general, for braces follow Kernighan and Ritchie (K&R) style.
* Unless there is an exception there is no line break before curly braces. But there is 
line break after opening brace, before closing brace and after closing brace.

### Semicolons
* They are not used, either to terminate or seperate statements.

### Parentheses
* Parentheses are not used around the top-most expression that follows an if, guard, while, or switch keyword.

### Horizontal Whitespace
In general it is good practice to use space:
* On both sides of any binary or ternary operator,
* Before any closing curly brace (}) that follows code on the same line, before any open curly brace ({), 
and after any open curly brace ({) that is followed by code on the same line,
* For separating any reserved word starting a conditional or switch statement (such as if, guard, while, or switch),
* Before and after the arrow (->) preceding the return type of a function.

### Types with Shorthand Names
Arrays, dictionaries, and optional types are written in their shorthand form whenever possible; 
that is, [Element], [Key: Value], and Wrapped?. The long forms Array<Element>, Dictionary<Key, Value>, and 
Optional<Wrapped> are only written when required by the compiler.

## Type, Variable, and Function Declarations
* In general, most source files contain only one top-level type, especially when the type 
declaration is large. Exceptions are allowed when it makes sense to include multiple related 
types in a single file.
* Each file and type uses some logical order, which its maintainer could explain if asked. 
* When deciding on the logical order of members, it can be helpful for readers and future writers
to use // MARK: comments to provide descriptions for that grouping. These comments are also 
interpreted by Xcode and provide bookmarks in the source window’s navigation bar. 

## Compiler Warnings
Code should compile without warnings when feasible. Any warnings that are able to be removed easily 
by the author must be removed.

## Testing
Write unittests for as much components as possible, ideally use
test-driven development.
