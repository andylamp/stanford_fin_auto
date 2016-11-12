# Week 4, Question 5

Let `G1` be a context-free grammar with start symbol `S1`, and no other non-terminals whose name begins with `S.` 
Similarly, let `G2` be a context-free grammar with a start symbol `S2`, and no other non-terminals whose name 
begins with `S.*` that is `S1` and `S2` appear on the right side of no productions. Also, no nonterminal appears 
in both `G1` and `G2`. We wish to combine the symbols and productions of `G1` and `G2` to form a new grammar `G`, 
whose language is the *union* of the languages of `G1` and `G2`. The start symbol of `G` will be `S`. All productions 
and symbols of `G1` and `G2` will be symbols and productions of `G`. Which of the following sets of productions, 
added to those of `G`, is guaranteed to make `L(G)` be `L(G1) union L(G2)`?

# Answer

In my instance I had the following options to select from:

 1. `S` → `S1`, `S1` → `S2`
 2. `S` → `S1`, `S1` → `S2`, `S2` → `ε`
 3. `S` → `S1S3`, `S3` → `S2` | `ε`
 4. `S` → `S1S2` | `S2S1`
 
This easily answered as **option 1**: `S` → `S1`, `S1` → `S2`  provides the correct link between `L(G1)` and 
`L(G2)`; this also happens because by definition we know that `S1` never appears on the right side of the derivation, 
hence we can confidently say that this is the correct answer.
