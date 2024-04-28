from .grammar import match_expr
from .grammar_ import stringify
from .deduce import deduce
from .lambda_ import LAMBDA
from .combinator import iks
from .answer import answer

def prove(proposition):
    try:
        premise, conclusion = match_expr(proposition)
    except Exception as e:
        return repr(e)

    proof = deduce({
        'priority': [0, 0, 0, 0],
        'premise': {
            stringify(p): p
            for p in premise
        },
        'used': set(),
        'conclusion': conclusion,
        '_lambda': None,
        '_apply': None
    })
    if proof is None:
        return 'not True'
    cl = iks(LAMBDA(proof._lambda, proof._apply))
    return answer(proof.premise, cl)
