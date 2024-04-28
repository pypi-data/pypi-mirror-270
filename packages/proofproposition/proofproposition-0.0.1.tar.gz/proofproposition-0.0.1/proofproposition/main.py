from argparse import ArgumentParser
from .prove import prove

description = '''
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
'''

def main():
    parser = ArgumentParser(description='[Propositional Logic]')
    parser.add_argument("proposition", type=str, help='input proposition here')
    args = parser.parse_args()
    if args.proposition == 'help':
        print(description)
    else:
        step = prove(args.proposition)
        if isinstance(step, list):
            for s in step:
                print(s)
        else:
            print(step)

if __name__ == '__main__':
    main()
