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

Recall from the lectures that in order to construct a right-most derivation from a given parse tree, we have to always
replace the *rightmost non-terminal* symbol. As we know, when a non-terminal is replaced during production the
introduced symbols correspond to the *children* of node `n`, in order, from the left.

Now if we try to match, using a right-most derivation, the only that is satisfied is `Aba` as such:

`S` → `AB` → `AbA` → `Aba`

In my case I had the following options to choose from:

 1. `Aba`
 2. `aabAba`
 3. `aABbA`
 4. `aSB`

Thus, based on what was described previously the correct answer is **option 1**: `Aba`

# Question 2

Let's now assume that the parse tree given below represents a *leftmost* derivation according to the grammar `G`: 

 * `S` → `AB` 
 * `A` → `aS` | `a` 
 * `B` → `bA` 
 
![ptree1][ptree]
 
Find that *leftmost* derivation. Which of the following is a *correct* left-sentential form in this derivation?

## Answer

In a similar fashion as above, but from the opposite direction the following derivation holds:

`S` → `AB` → `aSB` → `aABB` → `aabAB` → `aabaB`


In my case I had the following options to choose from:

 1. `aabaB`
 2. `aaABBB`
 3. `aSba`
 4. `aabAba`
 
# Question 3

Suppose the parse tree shown below is a parse tree for some unknown grammar `G`. Which of the following productions 
is **definitely not** a production of `G`?

![ptree1][ptree] 

## Answer

In my case I had the following options to choose from:

 1. `S` → `CB`
 2. None of the other choices. 
 3. `A` → `b`
 4. `B` → `b`
 
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

In my case I had the following options to choose from:

 1. 
    G1: `S` → `aB`, `B` → `bS`, `B` → `a`
    
    G2: `S` → `aB`, `B` → `bS`, `B` → `b`

 2.
 3.
 4.
 
# Question 5

You are given below a context-free grammar G:

 * `S` → `AB` 
 * `A` → `0A1` | `2`
 * `B` → `1B` | `3A`
 
Which of the following strings is in L(G)?

## Answer

In my case I had the following options to choose from:

 1. `00213021`
 2. `0002111112`
 3. `00211100211`
 4. `000211132`

Do note that the second rule generates strings in the form is 0<sup>n</sup>21<sup>n</sup>, 
where `n` can me zero or more. Additionally the third rule zero or more `1`'s, followed by *one* 3 
and something that the second rule generates. Finally since the initial rule generates *first* 
something that A does and *then* something that B generates the general form of the strings
this language rules generate are in the form of: 
0<sup>n</sup>21<sup>m</sup>30<sup>k</sup>21<sup>k</sup> where 0 ≤ n ≤ m and 0 ≤ k.
 
Based on the formula provided above, the correct answer is **option 4**: `000211132`.
 
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
 
  3. The derivation `S` =><sup>n</sup> `w`, because **2**, is either of the form  
        1. `S` => `SS` =><sup>n-1</sup> `w` or of the form
        2. `S` => `(S)` =><sup>n-1</sup> `w` 

Case (i):

 4. `w` = `xy`, for some strings `x` and `y` such that `S` =><sup>p</sup> `x` and 
 `S` =><sup>q</sup> `y`, where `p < n` and `q < n` because **2** 
 5. `x` is in `BP` because **1**
 6. `y` is in `BP` because **1**
 7. `w` is in `BP` because **3**

Case (ii):

 8. `w` = `(z)` for some string `z` such that `S` =><sup>n-1</sup> `z` because **2**
 9. `z` is in `BP` because **1**
 10. `w` is in `BP` because **3**


## Answer

The above reasons are directly embedded as the proof statements are presented.


[ptree]: images/parsetree1g.gif
