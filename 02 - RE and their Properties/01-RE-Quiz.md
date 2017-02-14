# Week 2, Quiz 1, Regular Expressions

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

The answer to this is quite straightforward, we basically have to see if the string
argument given to `L()` is contained, disjoint or neither from `L`. To do that, let's
examine each one of them, first of is: `1111001`

 * S  → `1` → `1` → `1` → `1` → `0` → `0` → `1`
 
 * `A` → `B` → `C` → `D` → `D` → `C` → `B` → `C`, halts as `C` is not an accepting state.
  
We can also easily see that this language does not take the automaton from state `D` to `D`, 
thus this language is **disjoint** from `L`. Let's now examine the second option: `11011`:

 * S  → `1` → `1` → `0` → `1` → `1`
 
 * `A` → `B` → `C` → `B` → `C` → `D`, accepts as `D` is an accepting state.

Now we have to check if the automaton takes us from `D` to `D`:

 * S  → `1` → `1` → `0` → `1` → `1`
 
 * `D` → `D` → `D` → `C` → `D` → `D`, accepts as `D` is an accepting state.

Thus this language is **contained** in `L` as it both takes the automaton to an accepting state
from `A` → `D` and from `D` → `D`. Let's now move on to examine the 
third option: `110101`:

 * S  → `1` → `1` → `0` → `1` → `0` → `1`
 
 * `A` → `B` → `C` → `B` → `C` → `D` → `C`, halts as `C` is not an accepting state.

We can easily see that that `L(110101)` is **not** contained in `L`, but if the
automaton starts from state `D` and follows the string `110101` it still ends up
in `D` as is shown below:

 * S  → `1` → `1` → `0` → `1` → `0` → `1`
 
 * `D` → `D` → `D` → `C` → `D` → `C` → `D`, accepts as `D` is an accepting state.


This means that this language is **not** contained in `L` but is not 
disjoint to `L`. This basically means that a *portion* of that language is contained 
in `L` but not **all**. Let's now examine the last option `00011101`:

 * S  → `0` → `0` → `0` → `1` → `1` → `1` → `0` → `1`
 
 * `A` → `A` → `A` → `A` → `B` → `C` → `D` → `C` → `D`, accepts as `D` is an accepting state.

Now we have to examine if we can reach `D` starting from `D`:

 * S  → `0` → `0` → `0` → `1` → `1` → `1` → `0` → `1`
 
 * `D` → `C` → `B` → `A` → `B` → `C` → `D` → `C` → `D`, accepts as `D` is an accepting state.

Thus we can see that `L(00011101)` is contained in `L`. Finally, given the above 
information we can summarize the given languages as follows:


 1. `L(1111001)`, *is disjoint* from `L`.
 2. `L(11011)`, *is  contained* in `L`.
 3. `L(110101)`, *is neither disjoint nor contained* in `L`.
 4. `L(00011101)`, *is contained* in `L`.
 
In my instance I had the following options:

 1. `L(1111001)` is disjoint from L.
 2. `L(11011)` is disjoint from L.
 3. `L(00011101)` is neither disjoint from L nor contained in L.
 4. `L(110101)` is contained in L.

Which, given the above findings the only statement that holds true is **option 1**: `L(1111001)` is disjoint from L,
thus it's the correct answer.

# Question 3

Converting a DFA such as the one below to a regular expression requires us to develop 
regular expressions for limited sets of paths --- those that take the automaton from 
one particular state to another particular state, without passing through some set of states. 
For the automaton given below, determine the languages for the following limitations:

 1. L<sub>AA</sub> = the set of path labels that go from `A` to `A` without passing through `C` or `D`.
 2. L<sub>AB</sub> = the set of path labels that go from `A` to `B` without passing through `C` or `D`.
 3. L<sub>BA</sub> = the set of path labels that go from `B` to `A` without passing through `C` or `D`.
 4. L<sub>BB</sub> = the set of path labels that go from `B` to `B` without passing through `C` or `D`.

Automaton:

![dfa2][dfa_2]

Then, identify a correct regular expression from the list below. Note: there are several 
different regular expressions possible for each of these languages. However, each of the 
correct answers can be thought of as built from more limited components. For example, the 
regular expression `1` is the set of path labels that go from `A` to `B` without passing 
through any of the four states.

## Answer

In my instance I had to select from the following options:

 1. L<sub>BA</sub> = (01+0)<sup>\*</sup>
 2. L<sub>AB</sub> = 0<sup>\*</sup>1(01+10)<sup>\*</sup>
 3. L<sub>BB</sub> = (0<sup>\*</sup>1)<sup>\*</sup>
 4. L<sub>BB</sub> =  (00<sup>\*</sup>1)<sup>\*</sup>

Like in the previous question, we have to calculate a regular expression that represents the 
paths in question. Thankfully, the construction principles are the same as before, 
hence after evaluation we can see that the only valid regular expression representing
the given ones is **option 4**: L<sub>BB</sub> =  (00<sup>\*</sup>1)<sup>\*</sup>.

This is because in order to represent *all* paths that go from state `B` to `B` and **do not** 
pass through `C` or `D` are (00<sup>\*</sup>1)<sup>\*</sup>. This is because, if we are in state
`B` the only way to move forward is to have `1` and the only way to go *back* is to have `0`; thus given
our restrictions we *must always* go back *before* we go forward. This is represented by the following
regular expression:

 * (01)

We can also have any number of them, which is shown again below:

 * (01)<sup>\*</sup>

This means that for each `1` there must be a `0` *before* it. Incidentally, if we are in state `A`, which we go 
if we have a `0` from `B` we can have an arbitrary number of `0`'s until we have the next `1` to advance to `B`, so
in order to reflect this our new regular expression is the following:

 * (00<sup>\*</sup>1)<sup>\*</sup>
 
Thus, the correct answer is **option 4**: L<sub>BB</sub> =  (00<sup>\*</sup>1)<sup>\*</sup>.

# Question 4

Identify from the list below the regular expression that generates all and only the 
strings over alphabet `{0,1}` that end in `1`.

## Answer

Let us examine our given options one by one, in my case I had the following 
regular expressions to choose from:

 1. (0<sup>\*</sup>1<sup>\+</sup>)<sup>\+</sup>
 2. (0<sup>\*</sup>+1)<sup>\*</sup>
 3. (0<sup>\*</sup>1)<sup>\*</sup>
 4. (00+01+10+11)<sup>\*</sup>1

We can easily see that the first expressions is the one that meets all of the
given requirements, hence it is the correct answer; let's see why this is the case.

To find the correct answer we need to find *all* the strings that end in `1` and 
are comprised out of `{0, 1}`. We can easily see that in order to construct *any*
permutation of strings that have `0` or `1`, including the empty string it is 
sufficient to use the following expressions: 

 * (0+1)<sup>\*</sup>
 
We can easily see that in our case we do **not** want to generate the empty string as
the minimum string we can accept has to have *at least* one `1`. Thus a regular 
expression to generate the string that has an arbitrary amount of zeros and ends in
`1` is the following:

 * (0<sup>\*</sup>1<sup>+</sup>)
 
This holds, as in order the above regular expression to be valid it has to have *zero* or 
*any* number of `0`'s followed by *at least* one or *more* `1`'s. The final key to 
the puzzle is to allow *at least* one or *more* of these expressions to be given 
any at time, which can be easily done by adding `+` as is shown below:

 * (0<sup>\*</sup>1<sup>+</sup>)<sup>+</sup>

The second option, (0<sup>\*</sup>+1)<sup>\*</sup> violates two constraints, first of 
all the empty string is *allowed*, secondly the accepted string does not 
necessarily end in `1` as inside the parenthesis we have the `+` sign which means either
in this case; this would make `0` an acceptable string.

The third option, (0<sup>\*</sup>1)<sup>\*</sup> allows the empty string to be accepted, thus
it generates more strings...

And finally the fourth option, does not generate all of the required string, as it 
fails to generate `11` or `01` and others...

Thus given the above, and as we said previously the correct answer is 
**option 1**: (0<sup>\*</sup>1<sup>\+</sup>)<sup>\+</sup>.


# Question 5

Apply the construction given in the video lectures to convert the regular expression 
(0+1)<sup>*</sup>(0+ε) to an ε-NFA. Then, identify the true statement about your ε-NFA from 
the list given below.

## Regular-Expression to ε-NFA construction

Recall from the lectures (specifically from the handy slides [here][lec_re]), that the amount of discreet states was
equal to double the amount of sum of the operands present in the RE plug the respective operators between each
operand. Concretely, in our case we have the following RE: (0+1)<sup>*</sup>(0+ε), which as we can see 
has four (4) distinct operands, and four operators, two (2) `+`, one (1) '\*', and one concatenation. We also 
know from the lectures each operand introduces two states, and that `+` and '\*' operators also introduce two 
states each while the concatenation operator does not introduce one. Hence, the total amount of states we
have is fourteen (`2\*(4+2+1)=2\*7=14`).

As for the arcs, `+` and `\*` operators introduce four (4) `ε` arcs each, while concatenation and `ε` itself introduce
one (1) epsilon arc. Thus the number of the `ε`-arcs is *four* times the number of `+`, `*` (`3*4`) plus the two
arcs introduced by concatenation and `ε`; this brings the total number of `ε`-arcs to fourteen (14).

The resulting ε-nfa is shown below (higher res [here][enfa_q6_pdf]).

![e_nfa_q6][enfa_q6]

## Answer

In my instance I had the following options to select from:

 1. There are 12 states with more than one arc in
 2. There are 16 states in total
 3. There are 2 states with more than one arc in
 4. There are 14 ε-arcs in total

From what was previously said the only correct option from the ones given is 
**option 4**: There are 14 ε-arcs in total.

[lec_re]: slides/5_re1.ppt
[dfa_2]: images/dfa_qz2_q2.gif
[enfa_q6]: images/enfa_q6.png
[enfa_q6_pdf]: images/tex_src/q6_re_enfa.pdf