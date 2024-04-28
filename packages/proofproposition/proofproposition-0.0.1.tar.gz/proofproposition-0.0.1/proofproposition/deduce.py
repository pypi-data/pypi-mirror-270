from queue import PriorityQueue
from copy import deepcopy
from .grammar_ import *
from .lambda_ import *

class Expr:
    def __init__(self, expr):
        self.priority = expr['priority']
        self.premise = expr['premise']
        self.used = expr['used']
        self.conclusion = expr['conclusion']
        self._lambda = expr['_lambda']
        self._apply = expr['_apply']

    def __lt__(self, other):
        for i in range(4):
            if self.priority[i] != other.priority[i]:
                return self.priority[i] < other.priority[i]
        return False

def get_op(p):
    return None if isinstance(p, str) else p['op']

def deduce(p):
    queue = PriorityQueue()
    queue.put(Expr(p))
    while not queue.empty():
        expr = queue.get()
        if isinstance(expr.conclusion, list):
            if not expr.conclusion:
                expr.used.remove(target)
                return expr
            r = deduce({
                'priority': deepcopy(expr.priority),
                'premise': deepcopy(expr.premise),
                'used': deepcopy(expr.used),
                'conclusion': expr.conclusion.pop(0),
                '_lambda': None,
                '_apply': None
            })
            if r is None:
                continue
            expr.priority = r.priority
            for s in r.premise:
                if s in expr.premise:
                    continue
                if get_op(r.premise[s]) in ['axiom '+str(i) for i in range(3, 11)]:
                    expr.premise[s] = r.premise[s]
            expr._apply = APPLY(expr._apply, LAMBDA(r._lambda, r._apply))
            queue.put(expr)
        else:
            while get_op(expr.conclusion) == '->':
                s = stringify(expr.conclusion['left'])
                expr.priority[0] += 1
                if s not in expr.premise:
                    expr.premise[s] = expr.conclusion['left']
                    expr.used = set()
                expr.conclusion = expr.conclusion['right']
                expr._lambda = LAMBDA(expr._lambda, {
                    'op': 'lambda',
                    'left': s
                })
            target = stringify(expr.conclusion)
            if target in expr.used:
                continue
            match get_op(expr.conclusion):
                case '*':
                    axiom5(expr)
                case '+':
                    axiom6(expr)
                    axiom7(expr)
                case _:
                    axiom9(expr)
                    axiom10(expr)
            for s in expr.premise.copy():
                match get_op(expr.premise[s]):
                    case '*':
                        axiom3(expr.premise, s)
                        axiom4(expr.premise, s)
                    case '+':
                        axiom8(expr.premise, s, expr.conclusion)
            for s in expr.premise:
                q = find(expr.premise[s], expr.conclusion)
                if q is None:
                    continue
                r = Expr({
                    'priority': deepcopy(expr.priority),
                    'premise': deepcopy(expr.premise),
                    'used': deepcopy(expr.used),
                    'conclusion': q,
                    '_lambda': deepcopy(expr._lambda),
                    '_apply': deepcopy(expr.premise[s])
                })
                r.used.add(target)
                r.priority[0] += 1
                match get_op(r.premise[s]):
                    case 'axiom 3':
                        r.priority[1] += 1
                    case 'axiom 4':
                        r.priority[1] += 1
                    case 'axiom 5':
                        r.priority[1] += 1
                    case 'axiom 6':
                        r.priority[1] += 1
                    case 'axiom 7':
                        r.priority[1] += 1
                    case 'axiom 8':
                        r.priority[1] += 1
                    case 'axiom 9':
                        r.priority[2] += 1
                    case 'axiom 10':
                        r.priority[3] += 1
                queue.put(r)
    return None
