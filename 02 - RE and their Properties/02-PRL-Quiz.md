# Week 2, Quiz 2: Properties of Regular Languages

# Question 1

Here is the transition table of a DFA:

Find the minimum-state DFA equivalent to the above. Then, identify in the list below the 
pair of equivalent states (states that get merged in the minimization process).

## Answer

# Question 2

Let `h` be a homomorphism from the alphabet `{a,b,c}` to `{0,1}`. If `h(a)` = `01`, `h(b)` = `0`, 
and `h(c)` = `10`, which of the following strings is in h<sup>-1</sup>(010010)?

## Answer

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

# Question 4

Which among the following languages is **not** regular (cannot be defined by a regular 
expression or finite automaton)?

1. `L` = {x | x=a<sup>m</sup>(bc)<sup>n</sup>, n, m positive integers}
2. `L` = {x | x=a<sup>k</sup>b<sup>n</sup>c<sup>k</sup>, n, k positive integers}
3. `L` = {x | x=a<sup>m</sup>b<sup>n</sup>c<sup>k</sup>, n, m, k positive integers}
4. `L` = {x | x=(ab<sup>2</sup> c)<sup>n</sup>, n a positive integer}

## Answer