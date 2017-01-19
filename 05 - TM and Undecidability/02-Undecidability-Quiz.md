# Week 5, Quiz 2, Undecidability Quiz
 
## Question 1

For the purpose of this question, we assume that all languages are over input alphabet {`0`,`1`}. Also, we assume 
that a Turing machine can have any fixed number of tapes. Sometimes restricting what a Turing machine can do does 
not affect the class of languages that can be recognized --- the restricted Turing machines can sti l be designed 
to accept any recursively enumerable language. Other restrictions limit what languages the Turing machine can accept. 
For example, it might limit the languages to some subset of the recursive languages, which we know is smaller than 
the recursively enumerable languages. Here are some of the possible restrictions:

 1. Limit the number of states the TM may have.
 2. Limit the number of tape symbols the TM may have.
 3. Limit the number of times any tape cell may change.
 4. Limit the amount of tape the TM may use.
 5. Limit the number of moves the TM may make.
 6. Limit the way the tape heads may move.

Consider the effect of limitations of these types, perhaps in pairs. Then, from the list below, identify the 
combination of restrictions that allows the restricted form of Turing machine to accept all recursively enumerable 
languages.


### Answer

In my instance I had the following options:

 1. Allow only two input symbols, `0` and `1`, and one other tape symbol, `B`.
 2. Allow the TM to run for only `n^10` moves when the input is of length `n`.
 3. Allow the TM to run for only `n^2` moves when the input is of length `n`.
 4. Allow the TM to run for only `2^n` moves when the input is of length `n`.
 
The answer to this one is very easy if you followed the lectures closely; the correct answer is 
**option 1**: Allow only two input symbols, `0` and `1`, and one other tape symbol, `B`. This because we know that
the Universal Turing Machine (UTM) *can* accept all recursively enumerable (RE) languages thus its the correct answer.
Detailed proof is given in [tm3 lecture][1].

[1]: slides/18_tm3.ppt

## Question 2

Which of the following problems about a Turing Machine `M` does Rice's Theorem imply is undecidable?

### Answer

In my instance I had the following options:

 1. Is there some input that causes `M` to halt after no more than 500 moves?
 2. Is the language of `M` empty?
 3. Is the language of `M` a set of strings?
 4. Is the language of `M` recursively enumerable?
 
This was explained in the lectures, the correct answer is **option 2**: Is the language of `M` empty? A little more
explanation would be that the only non-trivial properties that are described in the given options are 2, 4. We know
that all the languages that are accepted in the Universal Turing Machine are recursively enumerate. Additionally, it
is proved in the slides that the 2 is an undecidable problem which you can find [here][1] (slide 19/60).

[1]: slides/19_tm4.ppt

## Question 3

Here is an instance of the Modified Post's Correspondence Problem:

|       | List A | List B |
|:-----:|:------:|:------:|
|   1   |   01   |   010  |
|   2   |   11   |   110  |
|   3   |    0   |   01   |

If we apply the reduction of MPCP to PCP described in the class videos, which of the following 
would be a pair in the resulting PCP instance.

### Converting from MPCP to PCP

Following the direction given in the lecture we have to do the following things

 * Recreate the pairs of the original MPCP but on the first element we add `*` after each element while on the second
 element we prepend `*` before each element.
  * We have to add an *ender* state, `($, *$)`
  * Finally we have to add the *first* pair again but with the first element prepended with `*` while the other 
  elements being construct as previously said.
  
The full conversion follows...

|       |      MPCP     |         PCP         | 
|:-----:|:-------------:|:-------------------:|
|   1   | (`01`, `010`) | (`0*1*`, `*0*1*0`)  |
|   2   | (`11`, `110`) | (`1*1*`, `*1*1*0`)  |
|   3   |  (`0`, `01`)  |   (`0*`, `*0*1`)    |
|   4   |       -       |     (`$`, `*$`)     |
|   5   |       -       | (`*0*1*`, `*0*1*0`) |

Of note are rows 4, 5 as they are the ender and the special version of first pair respectively.

### Answer

In my instance I had the following options:

 1. (`1*1`, `*1*1*0`)
 2. (`*$`, `$`)
 3. (`*0*1*`, `*0*1*0`)
 4. (`*1*1*`, `*1*1*0`)
 
Based on the above we can clearly see that the correct answer is **option 3**: (`*0*1*`, `*0*1*0`) which incidentally
has the same value as our special first pair version.

## Question 4

We wish to perform the reduction of acceptance by a Turing machine to MPCP, as described in the class videos. 
We assume the TM `M` never moves left from its initial position and never writes a blank. We know the following:

 1. The start state of `M` is `q`.
 2. `r` is the accepting state of `M`.
 3. The tape symbols of `M` are `0`, `1`, and `B` (blank).
 4. One of the moves of `M` is `δ(q,0)` = `(p,1,L)`.

Which of the following is **DEFINITELY NOT** one of the pairs in the MPCP instance that we construct for the 
TM `M` and the input `001`?

### Answer

In my instance I had the following options:

 1. (`0r`, `r`)
 2. (`r1`, `q`)
 3. (`0q1`, `q`)
 4. (`0q0`, `p01`)
 
 
The correct answer is **option 3**: (`0q1`, `q`), this is because based on the construction rules outlines in the
lectures this is an *invalid* one as *only* the accepting state can "consume" adjacent tape symbols.

## Question 5

Let's suppose a problem `P1` reduces to a problem `P2`. Which of the following statements can we conclude to be 
**TRUE** based on the above?


### Answer

In my instance I had the following options:

 1. If `P1` is decidable, then it must be that `P2` is undecidable.
 2. If `P1` is RE, then it must be that `P2` is RE.
 3. If `P1` is decidable, then it must be that `P2` is decidable.
 4. If `P1` is non-RE, then it must be that `P2` is non-RE.
 
The correct answer to this question is **option 4**: If `P1` is non-RE, then it must be that `P2` is non-RE.

## Question 6

In this question, `L1`, `L2`, `L3`, `L4` refer to languages and `M`, `M1`, `M2` refer to Turing machines. Now Let

 * `L1` = {`(M1,M2)` | `L(M1)` is a subset of `L(M2)`},
 * `L2` = {`M` | There exists an input on which TM `M` halts *within* 100 steps},
 * `L3` = {`M` | There exists an input `w` of size *less* than 100, such that `M` accepts `w`},
 * `L4` = {`M` | `L(M)` contains *at least* 2 strings}.

Decide whether each of `L1`, `L2`, `L3` and `L4` are recursive, RE or neither. Then identify the *true* 
statement below.


### Answer

In my instance I had the following options:

 1. The intersection of `L2` and `L3` is not recursively enumerable.
 2. `L4` is recursive.
 3. The complement of `L2` is not recursively enumerable.
 4. The complement of `L4` is not recursive.
 
The correct answer to this one is **option 4**: The complement of `L4` is not recursive. That's because `L4` is
*not* a recursive language and since the complement is a *closed* operation it follows that the complement of
`L4` is not a recursive language as well.