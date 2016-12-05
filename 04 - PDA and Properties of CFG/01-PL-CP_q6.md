# Week 4, Question 6

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

# Answer

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
