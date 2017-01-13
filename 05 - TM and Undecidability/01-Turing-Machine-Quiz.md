# Week 5, Quiz 1 

## Question 1

Let the Turing Machine (TM), `M` with the following properties:

 * States `p`, `q` with `q` being the start state.
 * Type symbols `0`, `1`, `B`, with `0` and `1` being input symbol while `B` being the blank.
 * Has the following move table:

| State | Tape Symbol | Move |
|:-------:|:-------:|:-------:|
|  `q`  |   `0`   | `(q, 0, R)` |
|  `q`  |   `1`   | `(p, 0, R)` |
|  `q`  |   `B`   | `(q, B, R)` |
|  `p`  |   `0`   | `(q, 0, L)` |
|  `p`  |   `1`   | none (halt) |
|  `p`  |   `B`   | `(q, 0, L)` |

In this question we have to simulate using `M` the input string `w` = `1010110` and identify the correct ID 
(instantaneous description) of `M` from the provided options.

### Expanding of `w`

 1. `q1010110`, found `1` on tape thus `q` → `(p, 0, R)`
 2. `0p010110`, found `0` on tape thus `p` → `(q, 0, L)`
 3. `q0010110`, found `0` on tape thus `q` → `(q, 0, R)`
 4. `0q010110`, found `0` on tape thus `q` → `(q, 0, R)`
 5. `00q10110`, found `1` on tape thus `q` → `(p, 0, R)`
 6. `000p0110`, found `0` on tape thus `p` → `(q, 0, L)`
 7. `00q00110`, found `0` on tape thus `q` → `(q, 0, R)`
 8. `000q0110`, found `0` on tape thus `q` → `(q, 0, R)`
 9. `0000q110`, found `1` on tape thus `q` → `(p, 0, R)`
 10. `00000p10`, found `1` on tape while on state `p` thus we *halt*.

### Answer

In my instance I had the following options:

 1. `10q10110`
 2. `0000000qB`
 3. `0000q110`
 4. `00000000qB`
 
Based on the outline we gave above for the transitions, we can clearly see that the correct answer is 
**option 3**: `0000q110`.

## Question 2

Let the Turing Machine (TM), `M` with the following properties:

 * States `p`, `q` with `q` being the start state.
 * Type symbols `0`, `1`, `B`, with `0` and `1` being input symbol while `B` being the blank.
 * Has the following move table:

| State | Tape Symbol | Move |
|:-------:|:-------:|:-------:|
|  `q`  |   `0`   | `(q, 0, R)` |
|  `q`  |   `1`   | `(p, 0, R)` |
|  `q`  |   `B`   | `(q, B, R)` |
|  `p`  |   `0`   | `(q, 0, L)` |
|  `p`  |   `1`   | none (halt) |
|  `p`  |   `B`   | `(q, 0, L)` |

In this question we have to find the property of the strings `w` that are accepted by the previously defined 
Turing Machine (TM) `M`.

Based on the findings of [Question 1][1], we can clearly see that the property that makes `M` halt is the input string
`w` to have *two* or more consecutive `1`'s.

### Answer

In my instance I had the following options:

 1. `001010`
 2. `00001`
 3. `010110`
 4. `0101`
 
Based on what we said before the correct answer is **option 3**: `010110`, as it is the only one that has *two* or 
more consecutive `1`'s.

[1]: 01-Turing-Machine-Quiz.md

## Question 3

Let's assume a Turing machine `M` with start state `q0` and accepting state `qf` has the following 
transition function table:

|  `δ(q, a)`  |       `0`     |        `1`      |       `B`      |
|:-----------:|:-------------:|:---------------:|:--------------:|
|   `q_0`     | `(q_0, 1, R)` |  `(q_1, 1, R)`  | `(q_f, B, R)`  |
|   `q_1`     | `(q_2, 0, L)` |  `(q_2, 1, L)`  | `(q_2, B, L)`  |
|   `q_2`     |       -       |  `(q_0, 0, R)`  |        -       |
|   `q_f`     |       -       |         -       |        -       |


In this question we have to deduce what `M` does on any input of `0`'s and `1`'s. 

*Hint*: consider what happens when `M` is started in state `q0` at the *left* end of a sequence of any number 
of `0`'s (including zero of them) and a `1`. 

Demonstrate your understanding by identifying the *true* transition of `M` from the list below.

### Examining `M`

Now if we look at the function transition table of `M`, we might be able to spot that what basically `M` does, is to
flip `0`'s and `1`'s in the string and *finishes* padding a `B` to the string. An example of that would be the 
following: `0110` |-* `1001B`, let's show how this happens.

 1. `[q0]0110`, found `0` on tape thus `q0` → `(q0, 1, R)`
 2. `1[q0]110`, found `1` on tape thus `q0` → `(q1, 1, R)`
 3. `11[q1]10`, found `1` on tape thus `q1` → `(q2, 1, L)`
 4. `1[q2]110`, found `1` on tape thus `q2` → `(q0, 0, R)`
 5. `10[q0]10`, found `1` on tape thus `q0` → `(q1, 1, R)`
 6. `101[q1]0`, found `0` on tape thus `q1` → `(q2, 0, L)`
 7. `10[q2]10`, found `1` on tape thus `q2` → `(q0, 0, R)`
 8. `100[q0]0`, found `0` on tape thus `q0` → `(q0, 1, R)`
 9. `1001[q0]`, found `B` on tape thus `q0` → `(qf, B, R)`
 10. `1001B[qf]`, `M` halts
 
 Another example is `11` |-* `11B` and its expansion follows.
 
  1. `[q0]11`, found `1` on tape thus `q0` → `(q1, 1, R)`
  2. `1[q1]1`, found `1` on tape thus `q1` → `(q2, 1, L)`
  3. `[q2]11`, found `1` on tape thus `q2` → `(q0, 0, R)`
  4. `0[q0]1`, found `1` on tape thus `q0` → `(q1, 1, R)`
  5. `01[q1]`, found `B` on tape thus `q1` → `(q2, B, L)`
  6. `0[q2]1B`, found `1` on tape thus `q2` → `(q0, 0, R)`
  7. `00[q0]B`, found `B` on tape thus `q0` → `(q2, B, R)`
  8. `00B[qf]`, `M` halts

### Answer

In my instance I had the following answers:

 1. `[q0]0011` |-* `1100[qf]`
 2. `[q0]1100` |-* `0011B[qf]`
 3. `[q0]1010` |-* `1001B[qf]`
 4. `[q0]1010` |-* `1101B[qf]`
 
Based on the above steps we can clearly see that the correct answer to this question is 
**option 2**: `[q0]1100` |-* `0011B[qf]`

## Question 4

Let's assume a *Non-deterministic* Turing machine `M` with start state `q0` and accepting state `qf` has 
the following transition function table:

|  `δ(q, a)`  |       `0`     |        `1`      |       `B`      |
|:-----------:|:-------------:|:---------------:|:--------------:|
|   `q_0`     | `(q_1, 1, R)` |  `(q_1, 1, R)`  | `(q_f, B, R)`  |
|   `q_1`     | {`(q_1, 1, R)`, `(q_2, 0, L)`} |  {`(q_1, 1, R)`, `(q_2, 1, L)`}  | {`(q_1, 1, R)`, `(q_2, B, L)`}  |
|   `q_2`     | `(q_f, 0, R)` |  `(q_2, 1, L)`  |        -       |
|   `q_f`     |        -      |         -       |        -       |


In this question we have to simulate all sequences of 5 moves, starting from initial ID `q01010`. Find, in the 
list below, one of the ID's reachable from the initial ID in **EXACTLY** 5 moves.

### Expanding moves

Similarly to the previous question we will expand the TM `M` up to the required path, which is equal to the number
of moves we have to search -- in this case 5.

The expansion for the above string up to either the branch halts, or is at depth 5 follows:

 1. `[q0]1010 `, found `0` on tape thus `q0` → `(q1, 0, R)`
 2. `0[q1]010`, found `0` on tape thus `q1` → `(q1, 1, R)`, `(q2, 0, L)`
    * `[q2]0010`, found `0` on tape thus `q2` → `(qf, 0, R)`
        `[qf]00010`, branch halts at *3 moves*.
    * `01[q1]10`, found `1` on tape thus `q1` → `(q1, 1, R)`, `(q2, 1, L)`
        * `0[q2]110`, found `1` on tape thus `q2` → `(q2, 1, L)` 
            * `[q2]0110`, found `0` on tape thus `q2` → `(qf, 0, R)`
                * `0[qf]110`, halts at **5 moves**.
        * `011[q1]0`, found `0` on tape thus `q1` → `(q1, 1, R)`, `(q2, 0, L)`
            * `01[q2]10`, found `1` on tape thus `q2` → `(q2, 1, L)` 
                * `0[q2]110`, **5 move mark**
            * `0111[q1]`, found `B` on tape thus `q1` → `(q1, 1, R)`, `(q2, B, L)`
                * `01111[q1]`, **5 move mark**
                * `011[q2]1B`, **5 move mark**
        

### Answer

In my instance I had the following answers:

 1. `0[qf]111`
 2. `0[q2]111`
 3. `011[q2]11`
 4. `0[q2]110`
 
Based on the above expansion tree, we can clearly see that the correct answer in this 
case is **option 4**: `0[q2]110`