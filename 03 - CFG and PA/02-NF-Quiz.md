# Week 3, Quiz 2, Normal Forms

## Question 1

Let the grammar `G` of `L` be the one below:

`S` → `AB` | `CD`

`A` → `BC` | `a`

`B` → `AC` | `C`

`C` → `AB` | `CD`

`D` → `AC` | `d`

1. Find all generating symbols
2. Eliminate all *useless productions*
3. In the resulting grammar, eliminate all symbols that are **not** reachable.

Then select from your given statements in gradiance the one that is 
**false**.

### Find all generating symbols

Recall that a grammar symbol is a generating one if there is a derivation of at 
*least* one terminal string that starts with that particular symbol. In our
grammar we have *two* generating symbols as is shown below.

 * `a` and `d` are discovered as they are terminal symbols.
 * `A` is discovered as a generating symbol because `A` → `a` and `a` 
is a *terminal symbol*.
 * `D` is discovered as a generating symbol because `D` → `d` and `d`
 is a *terminal symbol*.

### Eliminate all *useless productions*

This a two step process, first we eliminate the useless unit productions and then
we eliminate the useless productions from the resulting grammar.

#### Eliminate unit productions

To do that we first have to create two distinct sets which have the following 
properties:

 1. Set `p1` has all unit productions
 2. Set `p2` has all of productions in our grammar that are **not** unit productions.


We see that this grammar does not have any unit production that is not towards a 
generating symbol, yet.

#### Eliminate useless productions

We start the recursive *discovery* algorithm which has the following steps:

 1. Discover all terminal symbols
  * For this grammar we have the following terminal symbols: `a`, `d`
 2. Discover immediate productions of symbols that produce the already discovered ones
  * We discover `A` because `A` → `a`, and `D` because `D` → `d`.
  
Nothing more can be added.

Thus our final grammar becomes:

`A` → `a`

`D` → `d`

All other states are removed because they could not be added to the set using the 
recursive discovery algorithm.

### Answer

In my instance I had the following options to select from:

 1. `B` is reachable
 2. `D` is not reachable
 3. `B` → `C` is useless
 4. `a` is not reachable
 

In this question we have to select the option that is **FALSE**, which is based on the
previous statements **option 1**: "`B` is reachable".

## Question 2

Let the grammar `G` of `L` be the one below:

`S` → `AB` | `CD`

`A` → `BG` | `0`

`B` → `AD` | `e`

`C` → `CD` | `1`

`D` → `BB` | `E`

`E` → `AF` | `B1`

`F` → `EG` | `0C`

`G` → `AG` | `BD`

### Find the nullable symbols

First let's find the symbols that are *immediately* nullable:

 * `B` is nullable (`B` → `e`)
 
Then using this we can easily see that `D` =>* `e`

 * `D` is nullable (`D` → `BB` =>* `e`)
 
Now we must find the combination of these that lead to nullable states.

 * `G` is nullable (`G` → `BD` → `e`, due to `B`, `D`, already nullable)
 * `A` is nullable (`A` → `BG`, due to `B`, `G` already nullable)
 * `S` is nullable (`S` → `AB`, due to `A`, `B` already nullable)
 
No other symbols can be nullable based on our given grammar `G`, thus the set
of nullable symbols is the following `N` = {`A`, `B`, `D`, `G`, `S`}.


### Answer

In my instance I had the following options to select from:

 1. `C` is nullable
 2. `A` is not nullable
 3. `B` is not nullable
 4. `F` is nullable
 
 
From those we had to select the option that was **TRUE**, given the previous statements
we can easily see that the correction is **option 2**: `A` is not nullable.

## Question 3

Let the grammar `G` of `L` be the one below:

`S` → `A` | `B` | `2`

`A` → `C0` | `D`

`B` → `C1` | `E`

`C` → `D` | `E` | `3`

`D` → `E0` | `S`

`E` → `D1` | `S`

### Find all unit pairs

Recall that a *unit pair* (`X`, `Y`) of a context-free grammar (CFG) is a pair where
the following conditions hold:

 1. `X`, `Y` are variables (non-terminals) of the grammar
 2. There exists a derivation from `X` =>* `Y` that uses *only* unit productions.

Terminal symbols are the following: `0`, `1`, `2`, `3`.

Thus we have:

`S` → `A`, thus (`S`, `A`) 

`S` → `B`, thus (`S`, `B`)

`A` → `D`, thus (`A`, `D`), and due to transitivity (`S`, `D`), (`A`, `A`), (`A`, `B`), (`A`, `E`), (`A`, `S`)

`B` → `E`, thus (`B`, `E`), and due to transitivity (`S`, `E`), (`B`, `A`), (`B`, `B`), (`B`, `E`), (`B`, `D`), (`B`, `S`)

`C` → `D`, thus (`C`, `D`), and due to transitivity (`C`, `A`), (`C`, `B`), (`C`, `S`)

`C` → `E`, thus (`C`, `E`)

`D` → `S`, thus (`D`, `S`), and due to transitivity (`D`, `A`), (`D`, `B`), (`D`, `E`)

`E` → `S`, thus (`E`, `S`), and due to transitivity (`E`, `A`), (`E`, `B`), (`E`, `E`)

and due to identity (`S`, `S`), (`A`, `A`), (`B`, `B`), (`C`, `C`), (`D`, `D`), (`E`, `E`)
 
So finally the `X` =>* {`Y1`, `Y2`...`Yn`} are:

`S`: {`S`, `A`, `B`, `D`, `E`}

`A`: {`A`, `B`, `D`, `E`, `S`}

`B`: {`B`, `A`, `E`, `D`, `S`}

`C`: {`C`, `A`, `B`, `D`, `E`, `S`}

`D`: {`D`, `A`, `B`, `E`, `S`}

`E`: {`E`, `A`, `B`, `E`, `S`}

### Answer

In my instance I had the following options to select from:

 1. (`D`, `C`)
 2. (`C`, `S`)
 3. (`S`, `S`)
 4. (`B`, `B`)
 

In this question we have to select the option that is **NOT** a unit pair, which is 
based on the previous statements **option 1**: "`B` is reachable".

## Question 4

Let the grammar `G` of `L` be the one below:

`S` → `A` | `B` | `2`

`A` → `C0` | `D`

`B` → `C1` | `E`

`D` → `E0` | `S`

`E` → `D1` | `S`

### Eliminate all unit productions

To do that we first have to create two distinct sets which have the following 
properties:

 1. Set `p1` has all unit productions
 2. Set `p2` has all of productions in our grammar that are **not** unit productions.

Thus, `p1` is comprised out of the following unit productions:

`p1`:

`S` → `A`, `B`, `D`, `E`

`A` → `D`, `S`, `A`, `B`, `E`

`B` → `E`, `S`, `A`, `B`, `D`

`C` → `D`, `S`, `A`, `B`, `D`, `E`

`D` → `S`, `A`, `B`, `D`, `E`

`E` → `S`, `A`, `B`, `D`, `E`

`p2`:

`A` → `C0`

`B` → `C1`

`C` → `3`

`D` → `E0`

`E` → `D1`

`S` → `2`

Now on `p1` we have to remove those rules that exist

Now we have to construct the new rules that follow using `p1` left-side symbols against the 
right-side symbols of `p2` using transitivity.

For `S`: `S` → `C0`, `S` → `C1`, `S` → `E0`, `S` → `D1`

For `A`: `A` → `E0`, `A` → `2`, `A` → `C1`, `A` → `D1`

For `B`: `B` → `D1`, `B` → `2`, `B` → `C0`, `B` → `E0`

For `C`: `C` → `C0`, `C` → `E0`, `C` → `D1`, `C` → `2`, `C` → `C1`

For `D`: `D` → `2`, `D` → `C0`, `D` → `C1`, `D` → `D1` 

For `E`: `E` → `2`, `E` → `C0`, `E` → `C1`, `E` → `E0`

Now the final grammar based on the union of the `p2` and the above is:

`S` → `C0` | `C1` | `E0` | `D1` | `2`

`A` → `C0` | `E0` | `C1` | `D1` | `2`

`B` → `C1` | `D1` | `C0` | `E0` | `2`

`C` → `C0` | `E0` | `D1` | `C1` | `2` | `3`

`D` → `E0` | `C0` | `C1` | `D1` | `2`

`E` → `D1` | `C0` | `C1` | `E0` | `2`

In this answer there are *redundant* symbols, but their elimination was not part of this exercise -- I'll leave it
to you to do it.

### Answer

In my instance I had the following options to select from:

 1. `A` → `D0`
 2. `E` → `3`
 3. `A` → `3`
 4. `B` → `C0`
 

In this question we have to select the option that is part of the new grammar, which is 
based on the previous statements **option 4**: "`B` → `C0`".

## Question 5

Suppose we execute the Chomsky-normal-form conversion algorithm described in the videos. Let `A` → `BC0DE` 
be one of the productions of the given grammar, which has already been freed of `ε`-productions and unit 
productions. 

Suppose that in our construction, we introduce new variable `Xa` to derive a terminal `a`, and when we need 
to split the right side of a production, we use new variables `Y1`, `Y2`,...

### Replacing the production

Now assuming the Chomsky-Normal-Form (CNF) we use the following methodology to break up the relations:

 1. Get rid of useless symbols, ε-productions and unit productions (already done).
 2. Get rid of productions whose bodies are mixes of terminals, or consist of more than one terminal 
 (already done).
 3. Break up production bodies longer than `2`
 
In our case `A` → `BC0DE` is longer than `2`, so we can break it up. Using the defined rules we need to
introduce one variable for the terminal symbol `0`, called `Xa` and has the form `Xa` → `0`; we also need
three additional transitional states that serve the purpose of "chaining everything" together, 
which are the following:

`A` → `BY1`

`Y1` → `CY2`

`Y2` → `XaY3`

`Y3` → `DE`

### Answer

In my instance I had the following options to select from:

 1. `Y2` → `0Y3`
 2. `A` → `Y1B`
 3. `Y3` → `DE`
 4. `Y3` → `Y4D`
 
In this question we have to select the option that is correct based on the mixed body breakup rules, 
which based on the previous statements is **option 3**: "`Y3` → `DE`".

## Question 6

Let the grammar `G` of `L` be the one below:

`R` → `ST` | `UV`

`T` → `UV` | `W`

`V` → `XY` | `Z`

`X` → `YZ` | `T`

The above grammar `G`, is one whose variables and terminals are **NOT** named using the usual convention. 
Any of symbols `R` through `Z` could be either a variable or terminal; it is your job to figure out which is 
which, and which could be the start symbol.

### Finding Nemo (or... symbols)

Thing is, there is one big distinction that we can deduce the terminal symbols; a terminal symbol **cannot** be
a generating one; which means that it can only be on the right-side of the productions and never on the left.

From the given rules we can clearly see that `S`, `W`, `Y` and `Z` appear only on the right-side.

Additionally a starting symbol has to be on the left-side and maybe on the right-side depending on the grammar;
we can clearly see that `R`, `T`, `V` and `X` appear on the left-side and `T`, `V` and `X` appear on both sides.
We can deduce with certainty that `R` is a starting symbol.

### Answer

In my instance I had the following options to select from:

 1. `T` must be the start symbol
 2. `X` must be a terminal
 3. `S` must be a terminal
 4. `Z` could be either a variable or a terminal
 

In this question we have to select the option that holds true, which is 
based on the previous statements **option 3**: "`S` must be a terminal".
