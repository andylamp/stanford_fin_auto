# Final

## Deterministic Finite Automata

The questions in this group refer to the following DFA:

![dfa_1][dfa1]

We suggest you first examine the automaton and determine intuitively what 
language it accepts.

### Answer

Let's construct the language that is accepted by the automaton, as per lectures we have a starting
state `A` and our (single) end state is `C` and thus we need to construct the arc R `k`-paths for 
k=1...3 for `AC` and `CC` because `AC` is to get from the starting state to the end state and 
`CC` is to get from `C` to `C` again.

 1. k = 0, R<sub>AC</sub> = ∅, as there is no way to go with 0 hop from `A` → `C`
 2. k = 1, R<sub>AC</sub> = ∅, as before there is no way to get with 1 hop from `A` → `C`
 2. k = 2, R<sub>AC</sub> = 0<sup>+</sup>10<sup>+</sup>1, to get with 2 hops from `A` → `C`
 2. k = 3, R<sub>CC</sub> = (0<sup>+</sup>+10<sup>+</sup>10<sup>+</sup>1), to get with 3 hops from `A` → `C`
 
Now the final language 
L is R<sub>AC</sub> R<sub>CC</sub> = (0<sup>+</sup>10<sup>+</sup>1)(0<sup>+</sup>+10<sup>+</sup>10<sup>+</sup>1) 

#### Part A

Which of the following strings is accepted by this DFA? In my instance I had the following options:

 1. `1011`
 2. `01110110`
 3. `0010101001`
 4. `ε`

Based L we generated, the correct answer is **option 3**.

#### Part B

How many strings of length 4 are accepted? In my instance I had the following options:

 1. 0
 2. 2
 3. 4
 4. 6
 
Based on L we generated, the correct answer is **option 4**.

#### Part C

Which of the following regular expressions takes the automaton from state `A` to state `B` 
without passing through state `C`?

 1. `0*1`
 2. `0*(0+1)0*`
 3. `0*10*`
 4. `0*1*0*`
 
Based on the automaton we have, we can easily see that the correct answer is **option 3**.

#### Part D

Which of the following regular expressions generates the same language as the automaton accepts?

 1. `0*10*10*(10*10*10*)*`
 2. `(1*0*10*10*)*`
 3. `0*10*1(0*10*10*1)*`
 4. `(0*1)*(0*10*10*10*)*`
 
Based on the language L and the automaton above we can see that the correct answer is **option 1**.

## Nondeterministic Finite Automata

The questions in this group refer to the following DFA:

![nfa_1][nfa1]

We suggest you first examine the automaton and determine 
intuitively what language it accepts.

## Regular and Context-Free Languages

Classify each of the following languages as either 

 1) regular 
 2) context-free but not regular, or 
 3) not context free 
 
All languages are over the alphabet `{0, 1, 2}`.

### Answer

## Closure Properties

### Answer

## Context-Free Grammars

### Answer

## CYK Algorithm

### Answer

## Grammar Simplification

### Answer

## Homomorphisms

### Answer

## Rice's Theorem

### Answer

## Polynomial-Time Reductions

### Answer

## Post's Correspondence Problem (PSP)

### Answer

## Satisfiability

### Answer

## Intractable Problems

### Answer

[dfa1]: images/dfa1.gif
[nfa1]: images/nfa1.gif