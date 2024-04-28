# Install
`$ pip3 install -U proofproposition`

# Description
```
### BNF of Proposition:
    Expr
        = [Premise] '|-' Imply
        ;
    Premise
        = Imply {',' Imply}*
        ;
    Imply
        = Or {'->' Or}*
        ;
    Or
        = And {'+' And}*
        ;
    And
        = Atom {'*' Atom}*
        ;
    Atom
        = token
        | '(' Imply ')'
        ;
    token
        = /\w+/
        ;

### Axiom of Primal:
    1) A->(B->A)
    2) (A->(B->C))->((A->B)->(A->C))

### Axiom of Minimal:
    3) (A*B)->A
    4) (A*B)->B
    5) A->(B->(A*B))
    6) A->(A+B)
    7) B->(A+B)
    8) (A->C)->((B->C)->((A+B)->C))

### Axiom of Intuitionistic:
    9) False->A

### Axiom of Classical:
   10) ((A->False)->A)->A

### Theorem:
    |- A->A

### Rule of Inference:
     A, A->B
    ---------
        B
```

# Command
`$ proof "A |- B->A"`

# Contact us
<may.xiaoya.zhang@gmail.com>
