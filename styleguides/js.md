# JS Style Guide
## Code formatting
Use [ESLint](https://eslint.org/) with the recommended settings
as a linter in your `js` projects.
- Your code should read as much as possible as English.
- The prime directive of line-wrapping is: prefer to break at a
higher syntactic level.
- Indent by 2 spaces at a time, no tabs.
- Put one space before and one after operators mathematical and logical operators.
- Use [JSDoc](https://google.github.io/styleguide/jsguide.html#jsdoc) on all
classes, fields, and methods.

## Naming conventions
For any resource, always use _descriptive_ names. For methods and
functions, make the name start or at least include a verb, such as 
`get`, `set`, `compute`, ..., etc.


| Resource      | Naming style                  | Example           |
|---------------|-------------------------------|-------------------|
| Script        | Lowercase with underscores    | `run_foo.js`      |
| Module        | Camelcase, upper case initial | `MyModule.js`     |
| Constants     | Uppercase with underscores    | `NO_CHANGE`       |
| Variables     | Camelcase, lowercase initial  | `myVar`           |
| Callables     | Camelcase, lowercase initial  | `applyFilter()`  |
| Classes       | Camelcase, upper initial      | `MyClass()`       |

## Import statements
* Group `import` statements by module types - keep one empty line inbetween groups:
  1. `npm` modules
  2. Custom/own modules
* Keep each group ordered alphabetically

## Magic numbers
Never make use of magic numbers - keep the code readable and maintainable.

## Testing
Write unittests for your code, or even better use test-driven development.
In the projects root directory, make a `test/` directory, to house them.

Write your tests using the `jest` module.