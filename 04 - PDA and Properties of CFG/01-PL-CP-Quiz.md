# Week 4 

## Question 1

Let the grammar `G` of `L` be the one below:

`S` → `AS` | `A`

`A` → `0A` | `1B` | `1`

`B` → `0B` | `0`

### Conversion of CFL to PDA

In order to convert the above CFL `L` into a PDA `P` that has the 
following properties:

 * One state `q`
 * The input symbols of `P` are the terminals of `G`
 * The stack symbols of `P` are the symbols of `G`
 * The start symbol of `P` is the start symbol of `G`
 
### Formal Construction of `P`

Let `P` = (`{q}`, Σ, V ∪ Σ, δ, `q`, `S`), where `δ` is defined by:

 1. If a transition `B` is in `V`, then `δ(q, ε, B)` = {`(q, α)` | `B` → `α` is in transitions of `G`}
 2. If `α` is in `Σ`, then `δ(q, α, α)` = {`(q, α)` = {`(q, ε)`}}

Now given the above grammar `G`, its equivalent PDA `P` is defined as:

`P` = (`{q}`, `{0, 1}`, `{0, 1, A, B, S}`, `δ`, `q`, `S`)

and has the following transitions:

 1. `δ(q, ε, S)` = `{(q, AS), (q, A)}`
 2. `δ(q, ε, A)` = `{(q, 0A), (q, 1B), (q, 1)}`
 3. `δ(q, ε, B)` = `{(q, 0B), (q, 0)}`
 4. `δ(q, 0, 0)` = `{(q, ε)}`
 5. `δ(q, 1, 1)` = `{(q, ε)}`
 

### Answer

In my instance I had the following options to select from:

 1. `δ(q, ε, B)` = `{(q, 0)}`
 2. `δ(q, ε, A)` = `{(q, 0A)}`
 3. `δ(q, 1, A)` = `{(q, B), (q, ε)}`
 4. `δ(q, ε, B)` = `{(q, 0B), (q, 0)}`
 
Based on our results above the correct answer is **option 4**: `δ(q, ε, B)` = `{(q, 0B), (q, 0)}`, as that
move is included in the final transition set that we have for `P`.

## Question 2

Suppose one transition rule of some PDA `P` is `δ(q,0,X)` = `{(p,YZ), (r,XY)}`. If we convert PDA `P` to 
an equivalent context-free grammar `G` in the manner described in the class videos. which of the following 
could be a production of `G` derived from this transition rule? You may assume `s` and `t` are states of `P`, 
as well as `p`, `q`, and `r`.

### Formal construction from PDA to CFG

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

### Answer

In my instance I had the following options to select from:

 1. `[qXs]` → `0[qYt][tZp]`
 2. `[qXs]` → `0[qXt][tYr]`
 3. `[qXs]` → `0[rXt][tYs]`
 4. `[qXs]` → `0[rXt][pYs]`
 
Based on what we demonstrated previously the correct answer is **option 3**: `[qXs]` → `0[rXt][tYs]`.

## Question 3

The language `L` = {`ss` | `s` is a string of `a`'s and `b`'s} is not a context-free language. In order to 
prove that `L` is not context-free we need to show that for every integer `n`, there is some string `z` 
in `L`, of length *at least* `n`, such that no matter how we break `z` up as `z` = `uvwxy`, subject to 
the constraints `|uvw| ≤ n` and `|uw| > 0`, there is some `i ≥ 0` such that `uv^iwx^iy` is not in `L`.
Let us focus on a particular `z` = `abaaabaa` and assume `n=8`. It turns out that this is a bad choice of `z`, 
since there are some ways to break `z` up for which we can find the desired `i`, and for others, we cannot. 
Identify from the list below the choice of `u`,`v`,`w`,`x`,`y` for which there is an `i` that makes `uv^iwx^iy` 
not be in `L`. We show the breakup of `abaaabaa` by placing four `|`'s among the `a`'s and `b`'s. The 
resulting five pieces (some of which may be empty), are the five strings. For instance, `ab|a||aabaa|` 
means `u=ab`, `v=a`, `w=ε`, `x=aabaa`, and `y=ε`.

This is easy to solve, based on the given choices we have to *remove* the `v` and `x` string blocks and find
the one choice that is not comprised out of *both* `a`'s and `b`'s.

Now the tricky part is to note that the resulting string `uwy` has to abide by `L` rules; hence we need to have 
`ss` which is two consecutive identical strings.

### Answer

In my instance I had the following options to select from:

 1. `a|ba|aa|ba|a`
 2. `a|b|aaaba|a|`
 3. `a|ba|a|ab|aa`
 4. `aba|a|ab|a|a`
 
Let's examine all of our options, one by one:

 1. `a|ba|aa|ba|a` → `a|aa|a` → `aaaa`, `s` = `aa` thus `aa|aa` so it **IS** in `L`
 2. `a|b|aaaba|a|` → `a|aaaba|` → `aaaaba`, we **can not** split into two identical `s`'s so it **IS NOT** in `L` 
 3. `a|ba|a|ab|aa` → `a|a|aa` → `aaaa`, `s` = `aa` thus `aa|aa` so it **IS** in `L`
 4. `aba|a|ab|a|a` → `aba|a|ba` → `abaaba`, `s` = `aba` thus `aba|aba` so it **IS** in `L`
 
The only option that is valid in this regard is **option 2**: `a|b|aaaba|a|` as `u=a`, `v=b`, `w=aaaba`, `x=a`, 
and `y=ε`, thus removing `v` and `x` string blocks from `z` then we are left with `a|aaaba|` and is 
transformed into `aaaaba` which as we said before cannot be split into two identical `s`'s and due 
to the fact that it cannot be in `L`.

## Question 4

Apply the `CYK` algorithm to the input `ababaa` and the grammar `G`:

 `S` → `AB` | `BC`

 `A` → `BA` | `a`

 `B` → `CC` | `b`

 `C` → `AB` | `a`
 
Compute the table of entries `Xij` = the set of non-terminals that derive positions `i` through `j`, 
inclusive, of the string `ababaa`. Then, identify a true assertion about one of the `Xij`'s in the 
list below. 

### Algorithm run

We need to create a triangular matrix based on the algorithm rules; this results in the following matrix:

|     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|
| `X_{16} = {S}` |     |     |     |     |     |
| `X_{15} = {A, B}` | `X_{26} = {A, S}` |     |     |     | |
|  `X_{14} = {B}`   |   `X_{25} = {}`   | `X_{36} = {S, A}` |     |     | |
|  `X_{13} = {B}`   | `X_{24} = {A, S}` |   `X_{35} = {B}`  |   `X_{46} = {}`   |                   |      |
| `X_{12} = {S, C}` | `X_{23} = {A, S}` | `X_{34} = {A, C}` | `X_{45} = {A, S}` |   `X_{55} = {B}`  |      |
| `X_{11} = {A, C}` |   `X_{22} = {B}`  | `X_{33} = {A, C}` |   `X_{44} = {B}`  | `X_{55} = {A, C}` | `X_{66} = {A, C}` |


### Answer

In my instance I had the following options to select from:

 1. `X_{36}` = `{S,A,C}`
 2. `X_{15}` = `{S,C}`
 3. `X_{15}` = `{B}`
 4. `X_{26}` = `{S,A}`

## Question 5

Let `G1` be a context-free grammar with start symbol `S1`, and no other non-terminals whose name begins with `S.` 
Similarly, let `G2` be a context-free grammar with a start symbol `S2`, and no other non-terminals whose name 
begins with `S.*` that is `S1` and `S2` appear on the right side of no productions. Also, no nonterminal appears 
in both `G1` and `G2`. We wish to combine the symbols and productions of `G1` and `G2` to form a new grammar `G`, 
whose language is the *union* of the languages of `G1` and `G2`. The start symbol of `G` will be `S`. All productions 
and symbols of `G1` and `G2` will be symbols and productions of `G`. Which of the following sets of productions, 
added to those of `G`, is guaranteed to make `L(G)` be `L(G1) union L(G2)`?

### Answer

In my instance I had the following options to select from:

 1. `S` → `S1`, `S1` → `S2`
 2. `S` → `S1`, `S1` → `S2`, `S2` → `ε`
 3. `S` → `S1S3`, `S3` → `S2` | `ε`
 4. `S` → `S1S2` | `S2S1`
 
This easily answered as **option 1**: `S` → `S1`, `S1` → `S2`  provides the correct link between `L(G1)` and 
`L(G2)`; this also happens because by definition we know that `S1` never appears on the right side of the derivation, 
hence we can confidently say that this is the correct answer.

## Question 6

Let `L` be the language of the grammar `G`:

 `S` → `AB`
 
 `A` → `aAb` | `aA` | `ε`
 
 `B` → `bBa` | `c`

The operation `min(L)` returns those strings in `L` such that no proper prefix is in `L`. Determine the language 
`min(L)` and identify in the list below the one string that is in `min(L)`.

In order to find the `min(L)` we need to find a general form of `L`, with a bit of effort we can deduce that `L` has
the following general pattern:

```
L = (a^i)(b^j)c(a^k)
```

Now we need to find a relationship between `i`, `j`, and `k` that satisfies `min(L)`. We also observe that `L` always
 needs to have a `c` thus we can deduce that `k` will be equal to the number of `b`'s required to produce `k` `a`'s 
 from the `B` → `bBa` production rule. Additionally, we can also deduce that the number of `b`'s left must be equal to
 the number of `a`'s which will be produced by `A` → `aAb` production rule.

This leads us to the following restrictions on `i`, `j`, and `k` but first, we break up `j` into two variables
`j_l` and `j_r` with the following relation: `j` = `j_l` + `j_r` that show the number of `b`'s required by `A` and `B`
production rules respectively.

Thus in order for a string to be in `L` the following must hold: 

 1. `i` = `j_l` if and only if `j_l` > 0
 2. `k` = `j_r` if and only if `k` > 0

### Answer

In my instance I had the following options to select from:

 1. `aaaabca`
 2. `aabbbbca`
 3. `abbbcaa`
 4. `aaabbbbc`


Let's examine all of the options one by one, starting with `aaaabca`. The only seemingly valid subset would be 
`aaaabc`, let's check it:

 `S` → `AB` → `aAB` → `aAbB` → `aaAbB` → `aaaAbB` → `aaaabB` → `aaaabc`, so it is a valid in `L`.
 
Let's move to the second one, `aabbbbca`. Again the only seemingly valid subset would be `aabbbbc`, but we see that the
initial string is not even in `L`, so we reject it.

Moving on to the third option, `abbbcaa`. The only two strings that could be a valid prefix strings are `abbbca` and
`abbbc`. Which both are not valid strings in `L` while the initial string is *valid*, so this is the **correct** answer.

Checking (for sanity) the last string `aaabbbbc` is pretty straightforward as again it's not a valid in `L`

Thus the correct answer based on what was said previously is **option 3**: `abbbcaa`