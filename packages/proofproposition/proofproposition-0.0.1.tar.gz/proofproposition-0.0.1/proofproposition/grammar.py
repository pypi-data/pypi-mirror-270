import tatsu
from functools import reduce

GRAMMAR = """
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
"""
parser = tatsu.compile(GRAMMAR)

def L2R(result, element):
    return {
        'op': element[0],
        'left': result,
        'right': element[1]
    } if len(element) == 2 else result

def match_imply(ast):
    if isinstance(ast, str):
        return ast
    match len(ast):
        case 1:
            return ast[0]
        case 2:
            return reduce(L2R, [
                (_ast[0], match_imply(_ast[1]))
                for _ast in ast[1]
            ], match_imply(ast[0]))
        case 3:
            return match_imply(ast[1])

def match_premise(ast):
    match len(ast):
        case 0:
            return []
        case 2:
            return [match_imply(ast[0])] + [
                match_imply(_ast[1])
                for _ast in ast[1]
            ]

def match_expr(codes):
    ast = parser.parse(codes)
    if len(ast) == 2:
        premise = []
        conclusion = ast[1]
    else:
        premise = ast[0]
        conclusion = ast[2]
    return match_premise(premise), match_imply(conclusion)
