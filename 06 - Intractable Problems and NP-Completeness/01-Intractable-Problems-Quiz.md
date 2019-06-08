# Week 6, Quiz 1, Intractable Problems Quiz
 
## Question 1

In the following expressions, - represents negation of a variable. For example, 
`¬x` stands for "NOT x"), + represents logical OR, and juxtaposition represents logical 
AND (e.g., `(x+y)(y+z)` represents (x OR y) AND (y OR z).

Identify the expression that is satisfiable, from the list below.

 1. `(¬x+y)(¬x+¬y)(y+z)(x)`
 2. `(x+y)(x+¬y)(¬x+y)(¬x+¬y)`
 3. `(x)(¬x+¬y)(¬y+z)(¬z+¬x)`
 4. `(x+¬y)(x+y)(¬x+¬y)(¬x+y)`

### Answer

To answer this, the correct way would be to find the independent set of the vertex cover of each problem 
which in turn will provide the solution. Or, for a hacky and more quick solution you can just solve
it quickly since the problems are small enough and only hold two variables. In any case, the correct answer is
**option 3**: `(x)(¬x+¬y)(¬y+z)(¬z+¬x)`.

## Question 2

Suppose there are three languages (i.e., problems), of which we know 
the following:

 1. L1 is in P.
 2. L2 is NP-complete.
 3. L3 is not in NP.

Suppose also that we do not know anything about the resolution of the 
"P vs. NP" question; for example, we do not know definitely whether P=NP. 
Classify each of the following languages as (a) Definitely in P, 
(b) Definitely in NP (but perhaps not in P and perhaps not NP-complete) 
(c) Definitely NP-complete (d) Definitely not in NP:

 1. L1 ∪ L2.
 2. L1 ∩ L2.
 3. L2cL3, where c is a symbol not in the alphabet of L2 or L3 
 (i.e., the marked concatenation of L2 and L3, where there is a 
 unique marker symbol between the strings from L2 and L3).
 4. The complement of L3.

Based on your analysis, pick the correct, definitely true statement 
from the list below.

### Answer

In my instance I had the following answers:

 1. L1 ∩ L2 is definitely NP-complete.
 2. The complement of L3 is definitely not in NP.
 3. L1 ∪ L2 is definitely not in NP.
 4. L1 ∪ L2 is definitely in NP. 

From the aforementioned options the correct one is **option 4**. To provide a more 
detailed answer let's try to classify each of the provided languages individually.

 1. L1 ∪ L2: We know that L1 is in P and L2 is NP-Complete and since P ⊆ NP then
 the union will be definitely in NP since we do not know that P=NP and thus we
 cannot definitely conclude that either L is either P or NP-complete and thus we
 take NP (which includes both P and NP-complete).
 2. L1 ∩ L2: In the same property as above and since the intersection operation
 is closed (see Q4 below) then the intersection will be definitely in NP.
 3. L2cL3.
 4. The complement of L3: Since we only know that L3 is not in NP, then if L3 is in P
 due to fact that P is closed under complementation hence L will be in P as well.
 Suppose now that L3 is an undecidable problem (not in NP) but its complement be 
 decidable but NP-hard - similarly we can construct other problem instances where
  we do not have a clear cut answer in which class L resides. Thus, with only 
  knowing that L3 is not in NP we cannot really deduce in which class the complement 
  of L3 will be.

## Question 3

The classes of languages P and NP are closed under certain operations, 
and not closed under others, just like classes such as the regular languages or 
context-free languages have closure properties. Decide whether P and NP are 
closed under each of the following operations.

 1. Union.
 2. Intersection.
 3. Intersection with a regular language.
 4. Concatenation.
 5. Kleene closure (star).
 6. Homomorphism.
 7. Inverse Homomorphism.

### Answer

In my instance I had the following options to select from:

 1. NP is not closed under union.
 2. NP is not closed under Kleene closure.
 3. P is not closed under intersection with a regular language.
 4. NP is not closed under homomorphism.
 
Naturally, the only true statement (as per lectures) is that NP is **not**
closed under homomorphism. Further, a more detailed breakdown with respect which 
one is closed or not based on the operation is shown below.

 1. Union (P: YES, NP: YES).
 2. Intersection (P: YES, NP: YES).
 3. Intersection with a regular language (P: YES, NP: YES).
 4. Concatenation (P: YES, NP: YES).
 5. Kleene closure (star) (P: YES, NP: YES).
 6. Homomorphism (P: NO, NP: NO).
 7. Inverse Homomorphism (P: YES, NP: YES).

## Question 4

The polynomial-time reduction from SAT to CSAT, as described in the class videos 
needs to introduce new variables. The reason is that the obvious manipulation of a 
boolean expression into an equivalent CNF expression could exponentiate the size of 
the expression, and therefore could not be polynomial time. Suppose we apply this 
construction to the expression `(u+(vw))+x`, with the parse implied by the 
parentheses. Suppose also that when we introduce new variables, we use 
`y1`, `y2`,... After constructing the corresponding CNF expression, 
identify one of its clauses from the list below. 

Note: logical OR is represented by `+`, logical AND by juxtaposition, and 
logical NOT by `¬`.


### Answer

In my instance I had the following options to select from:

 1. `(y3+y2+u)`
 2. `(u)`
 3. `(y2+¬y1+w)`
 4. `(y1+v)`

To answer this question we first need to construct the CNF form for our expression, namely: `(u+(vw))+x`. 
Recall from the lectures that you can easily do this by finding where this expression is false - for our 
particular example this is the case when using the following assigments:

 1. `u=0`, `v=0`, `w=0`, `x=0`
 2. `u=0`, `v=0`, `w=1`, `x=0`
 3. `u=0`, `v=1`, `w=0`, `x=0`
 
This creates the following three 4-clause terms:

```
 (¬u+¬v+¬w+¬x)(¬u+¬v+w+¬x)(¬u+v+¬w+¬x)
```

Now, to reduce this 4-sat problem to a 3-sat we can use "stick"-variables for each term, I will only show the
second term decomposition, as that will also reveal our corresponding answer - but you can easily infer 
how to do the others as well.

```
(¬u+¬v+w+¬x) = (¬u+¬v+y1)(w+y2+¬y1)(w+¬x+¬y2)
```

To decompose 4 terms we need 2 "sticky" variables, namely `y1` & `y2`, and you can see that the correct answer
given our options is **option 3**.

## Question 5

### Part A

The proof that the Node cover problem is NP-complete depends on a construction 
given in the class videos, which reduces 3SAT to Vertex (or Node) Cover. 
Apply this construction to the 3SAT instance:

```
(u+v+w)(¬v+¬w+x)(¬u+¬x+y)(x+¬y+z)(u+¬w+¬z)
```

Note that `¬` denotes negation, e.g., `¬v` stands for the literal NOT `v`. Also, 
remember that the construction involves the creation of nodes 
denoted `[i,j]`. The node `[i,j]` corresponds to the jth literal of the 
ith clause. For example, `[1,2]` corresponds to the occurrence of `v`.

After performing the construction, identify from the list below the one pair of nodes 
that does NOT have an edge between them.

### Answer

Let's perform the construction of the vertex cover the result of which is 
shown below (higher resultion [here][3sat_vec_cover_pdf])

![e_3sat_vec][3sat_vec_cover_small]



After performing the construction, identify from the list below the one pair of nodes 
that does **NOT** have an edge between them.

#### List A (first part)

 1. `[2, 3]` and `[4, 1]`
 2. `[1, 1]` and `[1 ,3]`
 3. `[3, 1]` and `[5 ,1]`
 4. `[4, 1]` and `[4 ,3]`

Based on our construction above we can easily see that the pair of nodes that
do **NOT** have an edge between them from the list is **option 1**, 
`[2, 3]` and `[4, 1]`.

#### List B (second part)

 1. `[3, 2]` and `[3 ,3]`
 2. `[3, 1]` and `[5 ,1]`
 3. `[1, 1]` and `[5 ,1]`
 4. `[1, 1]` and `[3 ,1]`

Similarly, we can easily see that the pair of nodes that
do **NOT** have an edge between them from the list is **option 3**, 
`[1, 1]` and `[5 ,1]`.

## Question 6

What is the size of a minimal vertex (or node) cover for the graph below?

![e_ind_set][ind_set]

### Answer

 1. `{B, C, D, F, G, I, J, K}`
 2. `{A, C, E, G, H, I, L}`
 3. `{A, B, C, E, H, J, K, L}`
 4. `{B, D, F, G, H, I, K}`
 
Let's start by defining what a vertex cover of a given graph is; A vertex cover
is the *set* of vertices such that each edge of the graph is incident to at least
once vertex of the set. Now the minimum vertex cover is a vertex cover that has
the minimum required nodes in order to be formed.

Our graph is defined as `P={A, B, C, D, E, F, G, H, I, J, K, L}`

The easiest way to check if a set of nodes is indeed a vertex cover is to check
if it's complement is not an independent set. This is easily shown by forming
the complement which is the difference between option 2 and `P`: `{D, F, J, K}`
but we can readily see that this is not an independent set since `D`, `J` are 
linked.

Moving on to option 3, we can see again by forming its complement: `{D, F, G, I}`
that is not an independent set since `D` and `I` are linked.

In a similar fashion we can see in option 4 by forming its complement: 
`{A, C, E, J, L}` that is not an independent set since `E` and `J` are linked.

Finally, we form the complement of option 1, which is `{A, E, H, L}` is indeed
an independent set since none of these nodes are linked and also is the minimal
cover having a size of 8. Please also do note that the solution is not *unique* 
and there can be a number of valid minimal covers for a given graph 
(but all will have the *same length*, if they are indeed minimal covers!).

[ind_set]: images/indepSet.gif
[3sat_vec_cover_small]: images/3sat-cover-small.png
[3sat_vec_cover_pdf]: pdfs/3sat-cover.pdf