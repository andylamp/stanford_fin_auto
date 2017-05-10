# Week 2, Quiz 2: Properties of Regular Languages

# Question 1

Here is the transition table of a DFA (arrow indicates starting states and `*` ending ones):

|         |   `0`   |   `1`   |
|:-------:|:-------:|:-------:|
|  → A    |     E   |    D    |
|  * B    |     A   |    C    |
|    C    |     G   |    B    |
|    D    |     E   |    A    |
|  * E    |     H   |    C    |
|    F    |     C   |    B    |
|    G    |     F   |    E    |
|    H    |     B   |    H    |

Find the minimum-state DFA equivalent to the above. Then, identify in the list below the 
pair of equivalent states (states that get merged in the minimization process).

## Constructing the distinguishable state table

Recall from the lectures, the way to construct this table is the following. First we have
to find the end states which in this case are `B` and `E`, which we can deduce that are
*distinguishable*. Then we have to proceed to find which states transition to an end state
with one and zero which we put into two separate sets.


 * Transition to end states on `0`: {A, D, H}
 * Transition to end states on `1`: {C, F, G}

 Now using the algorithm presented in the course lectures we construct the
 table shown below:

|      |   H   |   G   |   F   |   E   |   D   |   C   |   B   |
|:----:|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
|  A   |      |   x  |   x  |   x  |   x  |  x   |   x   |
|  B   |  x   |   x  |   x  |      |   x  |  x   |   _   |
|  C   |  x   |      |      |   x  |   x  |  _   |   _   |
|  D   |      |   x  |   x  |   x  |   _  |  _   |   _   |
|  E   |  x   |   x  |   x  |   _  |   _  |  _   |   _   |
|  F   |  x   |      |   _  |   _  |   _  |  _   |   _   |
|  G   |  x   |   _  |   _  |   _  |   _  |  _   |   _   |

## Answer

In my instance I had the following options:

 1. A and B
 2. D and G
 3. A and C
 4. B and E
 
Based on the previously presented table the correct answer is **option 4**: B and E.

# Question 2

Let `h` be a homomorphism from the alphabet `{a,b,c}` to `{0,1}`. If `h(a)` = `01`, `h(b)` = `0`, 
and `h(c)` = `10`, which of the following strings is in h<sup>-1</sup>(010010)?

## Answer

Recall that homomorphism is basically a map from a set of characters to another. Concretely in this
case h<sup>-1</sup>(10) would be equal to `a`.

In my instance I had the following options:

 1. cbbc
 2. baba
 3. abcb
 4. bcbc
 
Let's examine which is their equivalent by using the properties defined above.

 1. cbbc → 10 - 0 - 0 - 10 → 100010 which is not correct.
 2. baba → 0 - 01 - 0 - 01 → 001001 which, again is not correct.
 3. abcb → 01 - 0 - 10 - 0 → 010100 which, one more time is not correct.
 4. bcbc → 0 - 10 - 0 - 10 → 010010 which is the *desired* solution.
 
Based on what we said above the correct answer is **option 4**: bcbc.

# Question 3

The operation `DM(L)` where `L` is a regular language is defined as follows:
 
 1. Throw away every even-length string from `L`.
 2. For each odd-length string, remove the middle character.

For example, if `L` = `{001, 1100, 10101}`, then `DM(L)` = `{01, 1001}`. That is, even-length 
string `1100` is deleted, the middle character of `001` is removed to make `01`, and the 
middle character of `10101` is removed to make `1001`. It turns out that if `L` is a regular 
language, `DM(L)` may or may not be regular. For each of the following languages `L`, 
determine what `DM(L)` is, and tell whether or not it is regular.

 * L<sub>1</sub>: the language of regular expression `(01)*0`.
 * L<sub>2</sub>: the language of regular expression `(0+1)*1(0+1)*`.
 * L<sub>3</sub>: the language of regular expression `(101)*`.
 * L<sub>4</sub>: the language of regular expression `00*11*`.
 
Now, identify the true statement below.

## Answer

In my instance I had the following options:

 1. DM(L<sub>3</sub>) is regular; it is the language of regular expression 10(101101)*01.
 2. DM(L<sub>2</sub>) is regular; it is the language of regular expression ((0+1)(0+1))*.
 3. DM(L<sub>2</sub>) is not regular; it consists of all strings of the form (0+1)<sup>n</sup>00(0+1)<sup>n</sup>.
 4. DM(L<sub>2</sub>) is not regular; it consists of all even-length strings with more 0's than 1's.

# Question 4

Which among the following languages is **not** regular (cannot be defined by a regular 
expression or finite automaton)?

1. `L` = {x | x=a<sup>m</sup>(bc)<sup>n</sup>, n, m positive integers}
2. `L` = {x | x=a<sup>k</sup>b<sup>n</sup>c<sup>k</sup>, n, k positive integers}
3. `L` = {x | x=a<sup>m</sup>b<sup>n</sup>c<sup>k</sup>, n, m, k positive integers}
4. `L` = {x | x=(ab<sup>2</sup> c)<sup>n</sup>, n a positive integer}

## Answer

First of all, recall from the lectures that using the pumping lemma is the easiest solution of proving if a language
is regular or not... intuitively, in finite automata constraints of type a<sup>k</sup>b<sup>n</sup>c<sup>k</sup>, this
is well explained in the lectures; first of all this language is not regular, moreover RE's and FA's don't have
the expressive power to perform this (hence the requirement for CFG's and other constructs). Concretely, we can
use a RE or an FA to express the language if we don't have any *shared* constraints for the "replication" 
factors of each unique letter, which in our previous example are `a`, `b` and `c` for the letters and `k`, `n` for 
the replication factors. In the above case we can see that we *bind* the number of `a`'s to be *equal* to the 
number of `c`'s. This is **not** enforceable by just using RE's or FA's. Obviously, examples 1 and 3 have no 
relation in their replication factors and the only somewhat interesting case that remains is option 4. In option 
4, we can see that we have a potential relation of the operands, but in this case the Kleene star is *outside* and 
the `b` factor is fixed, equal to two (2); thus is can be expressed.

Based on what was previously said the only correct option that **cannot** be expressed by either a regular expression
of a finite automaton is **option 2**: `L` = {x | x=a<sup>k</sup>b<sup>n</sup>c<sup>k</sup>, n, k positive integers}