# Week 4, Question 1

Let the grammar `G` of `L` be the one below:

`S` → `AS` | `A`

`A` → `0A` | `1B` | `1`

`B` → `0B` | `0`

# Conversion of CFL to PDA

In order to convert the above CFL `L` into a PDA `P` that has the 
following properties:

 * One state `q`
 * The input symbols of `P` are the terminals of `G`
 * The stack symbols of `P` are the symbols of `G`
 * The start symbol of `P` is the start symbol of `G`
 
# Formal Construction of `P`

Let `P` = (`{q}`, Σ, V ∪ Σ, δ, `q`, `S`), where `δ` is defined by:

 1. If a transition `B` is in `V`, then `δ(q, ε, B)` = {`(q, α)` | `B` → `α` is in transitions of `G`}
 2. If `α` is in `Σ`, then `δ(q, α, α)` = {`(q, α)` = {`(q, ε)`}}

Now given the above grammar `G`, its equivalent PDA `P` is defined as:

`P` = (`{q}`, `{0, 1}`, `{0, 1, A, B, S}`, `δ`, `q`, `S`)

and has the following transitions:

 1. `δ(q, ε, S)` = `{(q, AS), (q, A)}`
 2. `δ(q, ε, A)` = `{(q, 0A), (q, 1B), (q, 1)}`
 3. `δ(q, ε, B)` = `{(q, 0B), (q, 0)}`
 4. `δ(q, 0, 0)` = `{(q, ε)}`
 5. `δ(q, 1, 1)` = `{(q, ε)}`
 

# Answer

In my instance I had the following options to select from:

 1. `δ(q, ε, B)` = `{(q, 0)}`
 2. `δ(q, ε, A)` = `{(q, 0A)}`
 3. `δ(q, 1, A)` = `{(q, B), (q, ε)}`
 4. `δ(q, ε, B)` = `{(q, 0B), (q, 0)}`
 
Based on our results above the correct answer is **option 4**: `δ(q, ε, B)` = `{(q, 0B), (q, 0)}`, as that
move is included in the final transition set that we have for `P`.