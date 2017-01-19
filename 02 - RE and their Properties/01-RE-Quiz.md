# Week 2, Quiz 1: Regular Expressions

# Question 1

Which of the following strings is NOT in the Kleene closure of the language `L = {011, 10, 110}`?

## Answer

 1. `10011101`
 2. `011011110`
 3. `01110011`
 4. `11001110`
 
Well, in order to find that we have to evaluate each option; remember that for a string to be
in the Kleene star of a language it has to be comprised out of multiples of each contents, that is
we *must* be able to break the string down to multiples of the language alphabet; for example
the string `01110` *is* in the Kleene star of `L` because it's comprised out of 1 x `011` and 
1 x `10`. Now from the given strings above the only string that we **cannot** break up into
multiples of `L` basic constructs is the one from **option 1**: `10011101`

Let us examine why this is the case, fist of all the string can be matched initially using 
only `10`, then we are left with `011101`. This we can match using again only one 
construct `011`, and we are left with `101`. Then we can match again `10` and we are 
left with a single `1` character that we cannot match, as `L` does not have a single `1` in 
its set of constructs.

Thus the correct answer is **option 1**: `10011101`

# Question 2

This DFA shown below accepts a certain language `L`. In this problem we shall consider certain 
other languages that are defined by their tails, that is, languages of the form `(0+1)*w`, 
for some particular string `w` of `0`'s and `1`'s. Call this language `L(w)`. Depending on `w`, 
`L(w)` may be contained in `L`, disjoint from `L`, or neither contained nor disjoint 
from `L` (i.e., some strings of the form `xw` are in `L` and others are not).

![dfa2][dfa_2]

Your problem is to find a way to classify `w` into one of these three cases. 
Then, use your knowledge to classify the following languages:

 1. `L(1111001)`, i.e., the language of regular expression `(0+1)*1111001`.
 2. `L(11011)`, i.e., the language of regular expression `(0+1)*11011`.
 3. `L(110101)`, i.e., the language of regular expression `(0+1)*110101`.
 4. `L(00011101)`, i.e., the language of regular expression `(0+1)*00011101`.

## Answer

# Question 3

Converting a DFA such as the one above to a regular expression requires us to develop 
regular expressions for limited sets of paths --- those that take the automaton from 
one particular state to another particular state, without passing through some set of states. 
For the automaton given below, determine the languages for the following limitations:

 * LAA = the set of path labels that go from `A` to `A` without passing through `C` or `D`.
 * LAB = the set of path labels that go from `A` to `B` without passing through `C` or `D`.
 * LBA = the set of path labels that go from `B` to `A` without passing through `C` or `D`.
 * LBB = the set of path labels that go from `B` to `B` without passing through `C` or `D`.

Automaton:

![dfa2][dfa_2]

Then, identify a correct regular expression from the list below. Note: there are several 
different regular expressions possible for each of these languages. However, each of the 
correct answers can be thought of as built from more limited components. For example, the 
regular expression `1` is the set of path labels that go from `A` to `B` without passing 
through any of the four states.

## Answer

# Question 4

Identify from the list below the regular expression that generates all and only the 
strings over alphabet `{0,1}` that end in `1`.

## Answer

# Question 5

Apply the construction given in the video lectures to convert the regular expression 
`(0+1)*(0+ε)` to an ε-NFA. Then, identify the true statement about your ε-NFA from 
the list below:

## Answer

[dfa_2]: images/dfa_qz2_q2.gif