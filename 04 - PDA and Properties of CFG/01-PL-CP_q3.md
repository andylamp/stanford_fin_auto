# Week 4, Question 3

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

# Answer

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