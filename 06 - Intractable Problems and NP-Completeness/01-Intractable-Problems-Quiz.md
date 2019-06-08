# Week 6, Quiz 1, Intractable Problems Quiz
 
## Question 1

### Answer

## Question 2

### Answer

## Question 3

### Answer

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
and there can be many minimal covers for a given graph (but all will have the
same length, if they are indeed minimal covers!).

[ind_set]: images/indepSet.gif
[3sat_vec_cover_small]: images/3sat-cover-small.png
[3sat_vec_cover_pdf]: pdfs/3sat-cover.pdf