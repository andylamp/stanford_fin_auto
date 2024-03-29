# Week 1, Quiz 1, Finite Automata Quiz

# Question 1

Given the following automaton, identify from the provided strings which one of them it accepts.

![dfa_1][dfa1]

In my instance I had the following choices:

 1. `01011`
 2. `01010`
 3. `1011011`
 4. `011`

## Option Evaluation

In order to answer this question we have to *follow* each one of given strings along the valid automaton paths;
if the string is consumed and leaves the automaton in an *ending* state then it is accepted otherwise it is
either rejected or halts.

Let's start by following the first option:

 S  → `0` → `1` → `0` → `1` → `1` 
 
 `A` → `B` → `D` → `A` → `C` → rejected as we cannot consume `1` from state `C`.
 
Moving on the second option:

 S → `0` → `1` → `0` → `1` → `0`
 
 `A` → `C` → `D` → `A` → `C` → `D`, and is accepted as `D` is a final state.
 
Let us now examine the third option:

 S → `1` → `0` → `1` → `1` → `0` → `1` → `1`
 
 `A` → `C` → `D` → `B` → `D` → `A` → `C` → rejected, as from state `C` we cannot consume `1`
 
Finally, the four and final option:

 S → `0` → `1` → `1`
 
 `A` → `B` → `D` → `B`, which is not an end state, so the automaton halts.
 
## Answer 
 
Thus, given the above evaluation the correct answer to our question is option **2**: `01010`.

# Question 2

The finite automaton given below accepts no word of length zero, no word of length one, 
and only two words of length two (`01` and `10`). There is a fairly simple recurrence 
equation for the number `N(k)` of words of length k that this automaton accepts. 
Discover this recurrence and demonstrate your understanding by identifying the 
correct value of `N(k)` for some particular `k`. 

![dfa_1][dfa1]

Note: the recurrence does not have an easy-to-use closed form, so you will have to 
compute the first few values by hand. You do not have to compute `N(k)` for any `k` 
greater than `14`.

## Recursion explanation

As described in the question the recursion in question does not have a nice, well 
formed closed form; this mean that the first few values have to be calculated beforehand.

We can easily from the automaton drawing that it does not accept any string *less* than 
two characters. Moreover it can only accept *two* distinct 2-character strings altogether: 
`01`, `10`. We can also easily see that from those two strings there are two paths 
states that we can take from each one; `1` takes us to state `B` and `0` takes us back
where we started. Additionally, we can see that from `D` we only need `11` to go back,
using `D` - 1 → `B` - 1 → `D`; thus for every string of length k-2 that ends up in `D`
we need `11` to return back to it. Interestingly, we can also see, in a similar fashion
as before that the same thing happens for strings that end in `D` that are of k-3 length.
These strings can be go back to state `D` using two distinct paths: `010` and `001`. So
the recursion has the following formula:

```
n(k):
    if k < 2
        return 0
    else if k == 2
        return 2
    else
        return n(k-2) + 2*n(k-3)
```

## Answer

Thus the answer would be to run the provided python script provided [here](code/01-FA-q2solver.py).
Just for reference my provided options were:

 1. N(14) = 280
 2. N(13) = 16
 3. N(13) = 84
 4. N(11) = 682

You can run the script to find that the correct answer in this instance is **option 3**: N(13) = 84.

# Question 3

Convert the following nondeterministic finite automaton:

![nfa_3][nfa3]

to a DFA, including the dead state, if necessary. Which of the following sets of 
NFA states is **not** a state of the DFA that is accessible from the start 
state of the DFA?

## Conversion to DFA

First of all we have to create the transition table for the given NFA, which is shown
below.

|      |   0  |  1   |
|:----:|:----:|:----:|
| → A  |   A  |  B   |
|  B   | {A, C} |  ∅  |
| * C   |   ∅   |  {A, B}  |

Then we have to *map* the *ambiguous* NFA states to their equivalent DFA states. 
For example, in our NFA `C` is an *ambiguous* state as for `1` it has two routes
instead of one. This is done using the "lazy" initialization which creates 
additional states on an "as needed" basis. For example, `B` state has two 
routes for `0` in our given NFA, thus in order to satisfy that constraint we
will have to create an additional state in our DFA called `{A, C}` that handles
both routes in one state. Then this state would be evaluated for their paths until
there are no more states left. The final transition/state table for our DFA is given
below.


|      |   0  |  1   |
|:----:|:----:|:----:|
|   → A   |    A   |     B    |
|     B   | {A, C} |     ∅    |
| * {A, C}|    A   |  {A, B}  |
|  {A, B} | {A, C} |     B    |

The DFA equivalent, if drawn, looks like this (higher 
res pdf: [here](images/tex_src/q3_dfa/q3_dfa.pdf)):

![nfa_3_dfa][nfa3_dfa]

## Answer

The given options were the following:

 1. {A, B, C}
 2. {}
 3. {A, B}
 4. {A}
 
The only state that does not exist in our given DFA is the one in **option 1**: {A, B, C}, 
which is the correct answer


# Question 4

Here is a nondeterministic finite automaton:

![nfa_4][nfa4]

Convert this NFA to a DFA, using the **lazy** version of the subset construction 
Which of the following sets of NFA states becomes a state of the DFA 
constructed in this manner?

## NFA to DFA

Similar to the previous question will first create the transition table of the 
given NFA as is shown below.

|             |     0     |     1    |
|:-----------:|:---------:|:--------:|
|     → A     |  {A, B}   |     C    |
|    {A, B}   |  {A, B}   |  {C, D}  |
|    {C, D}   | {A, B, D} |     D    |
| * {A, B, D} |  {A, B}   |  {C, D}  |
|      B      |     ∅     |  {C, D}  |
|    * D      |     A     |     D    |
|      C      |  {B, D}   |     D    |
| * {B, D}    |     A     |  {C, D}  |
  
The DFA equivalent, if drawn, looks like this (higher 
res pdf: [here](images/tex_src/q4_dfa/q4_dfa.pdf)):

![nfa_4_dfa][nfa4_dfa]

## Answer

This given the above, my options to select the correct answer from were the following:

 1. {A, D}
 2. {B}
 3. {B, C, D}
 4. {A, B, D}
 
Clearly, we correct answer is **option 4**: {A, B, D}

# Question 5

Here is an epsilon-NFA:

![enfa_1][enfa1]

Suppose we construct an equivalent DFA by the construction described in the video 
lecture. That is, start with the epsilon-closure of the start state A. For each set 
of states `S` we construct (which becomes one state of the DFA), look at the 
transitions from this set of states on input symbol 0. See where those transitions 
lead, and take the union of the epsilon-closures of all the states reached on 0. 
This set of states becomes a state of the DFA. Do the same for the transitions 
out of `S` on input `1`. When we have found all the sets of epsilon-NFA states 
that are constructed in this way, we have the DFA and its transitions. Carry out 
this construction of a DFA, and identify one of the states of this DFA (as a 
subset of the epsilon-NFA's states) from the list below.

## ε-NFA to DFA

In order to convert an ε-NFA to a regular NFA we have to remove the ambiguity that
is introduced by the shadow ε-jumps (called also as *nop-states*).

First of all we will have to find all of the *closures* of the nop-states; after
doing that we are left with basically three cases, as you can see we only have
two ways using `0` which are `0` and `00`. Likewise, we only have two ways 
getting to `N` using `1`, which are `1` and `10`. Finally we can see that
we can use a nop-jump to go from the start state directly to `N`. After
calculating all of the closures we are left with three *distinct* states
for our DFA, these are the following:

 1. ABCDHIJKMN
 2. BCDEGHIJKLMN
 3. BCDFGHIJKMN
 
Thus the DFA equivalent, if drawn, looks like this (higher 
res pdf: [here](images/tex_src/q5_dfa/q5_dfa.pdf)):

![nfa_5_dfa][nfa5_dfa]

## Answer

This given the above, my options to select the correct answer from were the following:

 1. ABCD
 2. BCDFGHIJKMN
 3. ABCDEFGHIJKLMN
 4. IJKMN
 
Clearly, we correct answer is **option 2*: BCDFGHIJKMN

# Question 6

Here is the transition function of a simple, deterministic automaton with start 
state `A` and accepting state `B`:

|     |  0  |  1  |
|:---:|:---:|:---:|
|  A  |  A  |  B  |
|  B  |  B  |  A  |

We want to show that this automaton accepts exactly those strings with an odd 
number of `1`'s, or more formally:

```
 δ(A,w) = B if and only if w has an odd number of 1's.
```

Here, `δ` is the extended transition function of the automaton; that is, `δ(A,w)` is the 
state that the automaton is in after processing input string `w`. The proof of the 
statement above is an induction on the length of `w`. Below, we give the proof with 
reasons missing. You must give a reason for each step, and then demonstrate your 
understanding of the proof by classifying your reasons into the following 
three categories:

1. Use of the inductive hypothesis.
2. Reasoning about properties of deterministic finite automata, e.g., 
that if string `s` = `yz`, then `δ(q,s)` = `δ(δ(q,y),z)`.
3. Reasoning about properties of binary strings (strings of `0`'s and `1`'s), 
e.g., that every string is longer than any of its proper substrings.

Basis (`|w|` = `0`):

 1. `w` = `ε` because (C)
 2. `δ(A,ε)` = `A` because (B)
 3. `ε` has an even number of `1`'s because (C)
 
    Induction (`|w|` = `n > 0`)
    
 4. There are two cases: (a) when `w` = `x1` and (b) when `w` = `x0` because (C)

    Case (a)
    
 5. In case (a), `w` has an odd number of `1`'s if and 
 only if `x` has an even number of `1`'s because (C)
 6. In case (a), `δ(A,x)` = `A` if and only if `w` has an odd number 
 of `1`'s because (A)
 7. In case (a), `δ(A,w)` = `B` if and only if `w` has an odd number 
 of `1`'s because (B)

    Case (b):

 8. In case (b), `w` has an odd number of `1`'s if and only if `x` has an odd number 
 of `1`'s because (C)

 9. In case (b), `δ(A,x)` = `B` if and only if `w` has an odd number 
 of `1`'s because (A)

 10. In case (b), `δ(A,w)` = `B` if and only if `w` has an odd number of `1`'s because (C)

## Answer

In my instance I had the following options:

 1. (2) for reason (B)
 2. (5) for reason (A)
 3. (6) for reason (C)
 4. (10) for reason (C)
 
Judging from the above, we can clearly see that the correct answer is **option 1**: (2) for reason (B).

[dfa1]: images/dfa1.gif
[nfa3]: images/nfa3.gif
[nfa3_dfa]: images/nfa3_dfa.png
[nfa4_dfa]: images/nfa4_dfa.png
[nfa5_dfa]: images/nfa5_dfa.png
[nfa4]: images/nfa4.gif
[enfa1]: images/enfa1.gif
