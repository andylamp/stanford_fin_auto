# Week 1 Quiz

# Question 1

Given the following automaton, identify from the provided strings which one of them it accepts.

![dfa_1][dfa1]

In my instance I had the following choices:

 1. `01011`
 2. `01010`
 3. `1011011`
 4. `011`

## Answer

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
 
This given the above analysis the correct answer to our question is option **2**: `01010`.

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

## Answer

# Question 3

Convert the following nondeterministic finite automaton:

![nfa_3][nfa3]

## Answer

# Question 4

Here is a nondeterministic finite automaton:

![nfa_4][nfa4]

Convert this NFA to a DFA, using the **lazy** version of the subset construction 
Which of the following sets of NFA states becomes a state of the DFA 
constructed in this manner?

## Answer

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

## Answer

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

 1. `w` = `ε` because ________
 2. `δ(A,ε)` = `A` because ________
 3. `ε` has an even number of `1`'s because ________
 
    Induction (`|w|` = `n > 0`)
    
 4. There are two cases: (a) when `w` = `x1` and (b) when `w` = `x0` because ________

    Case (a)
    
 5. In case (a), `w` has an odd number of `1`'s if and 
 only if `x` has an even number of `1`'s because ________
 6. In case (a), `δ(A,x)` = `A` if and only if `w` has an odd number 
 of `1`'s because ________
 7. In case (a), `δ(A,w)` = `B` if and only if `w` has an odd number 
 of `1`'s because ________

    Case (b):

 8. In case (b), `w` has an odd number of `1`'s if and only if `x` has an odd number 
 of `1`'s because ________
 9. In case (b), `δ(A,x)` = `B` if and only if `w` has an odd number 
 of `1`'s because ________
10. In case (b), `δ(A,w)` = `B` if and only if `w` has an odd number of `1`'s because ________

## Answer

[dfa1]: images/dfa1.gif
[nfa3]: images/nfa3.gif
[nfa4]: images/nfa4.gif
[enfa1]: images/enfa1.gif