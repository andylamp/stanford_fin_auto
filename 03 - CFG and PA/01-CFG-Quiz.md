# Week 3, Quiz 1, Context Free Grammars

# Question 1

The parse tree shown below represents a *rightmost* derivation according to the grammar: 

 * `S` → `AB` 
 * `A` → `aS` | `a` 
 * `B` → `bA`
 
![ptree1][ptree] 
 
Find that *rightmost* derivation and select which of the following is a *correct* right-sentential form in 
this derivation?

## Answer

# Question 2

Let's now assume that the parse tree given below represents a *leftmost* derivation according to the grammar `G`: 

 * `S` → `AB` 
 * `A` → `aS` | `a` 
 * `B` → `bA` 
 
![ptree1][ptree]
 
Find that *leftmost* derivation. Which of the following is a *correct* left-sentential form in this derivation?

## Answer

# Question 3

Suppose the parse tree shown below is a parse tree for some unknown grammar `G`. Which of the following productions 
is **definitely not** a production of `G`?

![ptree1][ptree] 

## Answer

# Question 4

Below we have eight simple grammars, each of which generates an infinite language of strings. These strings tend to 
look like alternating `a`'s and `b`'s, although there are some exceptions, and not all grammars generate all 
such strings.

 1. `S` → `abS` | `ab`
 2. `S` → `SS` | `ab`
 3. `S` → `aB`; `B` → `bS` | `a`
 4. `S` → `aB`; `B` → `bS` | `b`
 5. `S` → `aB`; `B` → `bS` | `ab`
 6. `S` → `aB` | `b`; `B` → `bS`
 7. `S` → `aB` | `a`; `B` → `bS`
 8. `S` → `aB` | `ab`; `B` → `bS`


Do note that the *initial symbol* for every grammar given is `S`. Determine the language of each of these grammars. 
Then, find, in the list below, the pair of grammars that define the same language.

## Answer

# Question 5

You are given below a context-free grammar G:

 * `S` → `AB` 
 * `A` → `0A1` | `2`
 * `B` → `1B` | `3A`
 
Which of the following strings is in L(G)?

## Answer

# Question 6

 Let `G` be the grammar:
 
 ```
 S → SS | (S) | ε
 ```

`L(G)` is the language `BP` of all strings of balanced parentheses, that is, those 
strings that could appear in a well-formed arithmetic expression. We want to prove 
that `L(G) = BP`, which requires two inductive proofs:

 1. If `w` is in `L(G)`, then `w` is in `BP`.
 2. If `w` is in `BP`, then `w` is in `L(G)`.
 
We shall here prove only the first. You will see below a sequence of steps in the 
proof, each with a reason left out. These reasons belong to one of three classes:

  1. Use of the inductive hypothesis.
  2. Reasoning about properties of grammars, e.g., that every derivation has at least one step.
  3. Reasoning about properties of strings, e.g., that every string is longer than any of its proper substrings.

The proof is an induction on the number of steps in the derivation of `w`. 
You should decide on the reason for each 
step in the proof below, and 
then identify from the available choices a correct pair 
consisting of a step and a kind of reason (1, 2, or 3).


 1. The only 1-step derivation of a terminal string is `S` => `ε` because **2**
 2. `ε` is in `BP` because **3**

Induction: An n-step derivation for some n>1.
 
  3. The derivation `S` => `n` `w` is either of the form
    a. `S` => `SS` => `n-1` `w` or of the form
    b. `S` => `(S)` => `n-1` `w` because **2**

Case (a):

 4. `w` = `xy`, for some strings `x` and `y` such that `S` => `p` `x` and `S` => `q` `y`, where `p < n` and `q < n` because **2** 
 5. `x` is in `BP` because **1**
 6. `y` is in `BP` because **1**
 7. `w` is in `BP` because **3**

Case (b):

 8. w = (z) for some string z such that S =>n-1 z because **2**
 9. z is in BP because **1**
 10. w is in BP because **3**


## Answer

The above reasons are labeled.

[ptree]: images/parsetree1g.gif
