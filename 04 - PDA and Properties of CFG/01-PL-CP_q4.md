# Week 4, Question 4

Apply the `CYK` algorithm to the input `ababaa` and the grammar `G`:

 `S` → `AB` | `BC`

 `A` → `BA` | `a`

 `B` → `CC` | `b`

 `C` → `AB` | `a`
 
Compute the table of entries `Xij` = the set of non-terminals that derive positions `i` through `j`, 
inclusive, of the string `ababaa`. Then, identify a true assertion about one of the `Xij`'s in the 
list below. 

# Algorithm run

We need to create a triangular matrix based on the algorithm rules; this results in the following matrix:

|     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|
| `X_{15} = {S}` |     |     |     |     |     |
| `X_{15} = {A, B}` | `X_{26} = {A, S}` |     |     |     | |
|   `X_{14} = {B}`  |   `X_{25} = {}`   | `X_{36} = {S, A}` |     |     | |
|   `X_{13} = {B}`  | `X_{24} = {A, S}` |   `X_{35} = {B}`  |   `X_{46} = {}`   |                   |      |
| `X_{12} = {S, C}` | `X_{23} = {A, S}` | `X_{34} = {A, C}` | `X_{45} = {A, S}` |   `X_{55} = {B}`  |      |
| `X_{11} = {A, C}` |   `X_{22} = {B}`  | `X_{33} = {A, C}` |   `X_{44} = {B}`  | `X_{55} = {A, C}` | `X_{66} = {A, C}` |


# Answer

In my instance I had the following options to select from:

 1. `X_{36}` = `{S,A,C}`
 2. `X_{15}` = `{S,C}`
 3. `X_{15}` = `{B}`
 4. `X_{26}` = `{S,A}`
