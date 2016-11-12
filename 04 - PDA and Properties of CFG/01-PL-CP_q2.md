# Week 3, Question 2

Suppose one transition rule of some PDA `P` is `δ(q,0,X)` = `{(p,YZ), (r,XY)}`. If we convert PDA `P` to 
an equivalent context-free grammar `G` in the manner described in the class videos. which of the following 
could be a production of `G` derived from this transition rule? You may assume `s` and `t` are states of `P`, 
as well as `p`, `q`, and `r`.

# Formal construction from PDA to CFG

We can clearly see that our transition function `δ` has two available moves in this instance, namely: 
`(p, YZ)`, `(r, YZ)`. We can also easily spot that `δ` consumes a zero (`0`) from the input and has 
a different state `q` than in its two available transitions which have states `p` and `r` respectively. 
Additionally we can see that in the first transition `X` is *replaced* by *two* symbols, `YZ` while 
in the second case `X` is *padded* by `XY`.

Example constructions:

 * Popping rules, e.g. `(p, ε)` in `δ(q, α, Z)` is `[qZp]` → `a`
 * Replacement symbol rule, e.g. `(p, Y)` in  `δ(q, α, Z)` is `[qZr]` → `α[pZr]`
 * Two symbol replacement rule, e.g. `(p, XY)` in `δ(q, α, Z)` is `[qZs]` → `a[pXr][rYs]`

Generally `n`-symbol replacement rules require `n`-chain states to be implemented in CNF form.

Now let's tackle each one of the moves separately, starting with `(p, YZ)` which translates in the following:

 * `[qXs]` → `0[pYt][tZs]`, in which we required two chain states to go from `q` → `s`
 
Then we continue to tackle the other move, which is `(r, XY)`, which translates into the following:

 * `[qXs]` → `0[rXt][tYs]`

# Answers

In my instance I had the following options to select from:

 1. `[qXs]` → `0[qYt][tZp]`
 2. `[qXs]` → `0[qXt][tYr]`
 3. `[qXs]` → `0[rXt][tYs]`
 4. `[qXs]` → `0[rXt][pYs]`
 
Based on what we demonstrated previously the correct answer is **option 3**: `[qXs]` → `0[rXt][tYs]`.