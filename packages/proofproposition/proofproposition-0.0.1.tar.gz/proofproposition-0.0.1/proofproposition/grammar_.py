def stringify(p):
    if isinstance(p, str):
        return p
    if 'formula' not in p:
        op = p['op']
        if op in ['axiom '+str(i) for i in range(3, 11)]:
            op = '->'
        p['formula'] = '('+stringify(p['left'])+op+stringify(p['right'])+')'
    return p['formula']

def find(premise, conclusion):
    pstr = stringify(premise)
    cstr = stringify(conclusion)
    if len(pstr) < len(cstr):
        return None
    if pstr == cstr:
        return []
    if not isinstance(premise, str):
        op = premise['op']
        if op in ['axiom '+str(i) for i in range(3, 11)] or op == '->':
            p = find(premise['right'], conclusion)
            if isinstance(p, list):
                p.insert(0, premise['left'])
            return p
    return None

def axiom3(premise, s):
    _axiom3 = {
        'op': 'axiom 3',
        'left': premise[s],
        'right': premise[s]['left']
    }
    axiom3_ = stringify(_axiom3)
    if axiom3_ not in premise:
        premise[axiom3_] = _axiom3

def axiom4(premise, s):
    _axiom4 = {
        'op': 'axiom 4',
        'left': premise[s],
        'right': premise[s]['right']
    }
    axiom4_ = stringify(_axiom4)
    if axiom4_ not in premise:
        premise[axiom4_] = _axiom4

def axiom5(expr):
    _axiom5 = {
        'op': 'axiom 5',
        'left': expr.conclusion['left'],
        'right': {
            'op': '->',
            'left': expr.conclusion['right'],
            'right': expr.conclusion
        }
    }
    axiom5_ = stringify(_axiom5)
    if axiom5_ not in expr.premise:
        expr.premise[axiom5_] = _axiom5

def axiom6(expr):
    _axiom6 = {
        'op': 'axiom 6',
        'left': expr.conclusion['left'],
        'right': expr.conclusion
    }
    axiom6_ = stringify(_axiom6)
    if axiom6_ not in expr.premise:
        expr.premise[axiom6_] = _axiom6

def axiom7(expr):
    _axiom7 = {
        'op': 'axiom 7',
        'left': expr.conclusion['right'],
        'right': expr.conclusion
    }
    axiom7_ = stringify(_axiom7)
    if axiom7_ not in expr.premise:
        expr.premise[axiom7_] = _axiom7

def axiom8(premise, s, conclusion):
    _axiom8 = {
        'op': 'axiom 8',
        'left': {
            'op': '->',
            'left': premise[s]['left'],
            'right': conclusion
        },
        'right': {
            'op': '->',
            'left': {
                'op': '->',
                'left': premise[s]['right'],
                'right': conclusion
            },
            'right': {
                'op': '->',
                'left': premise[s],
                'right': conclusion
            }
        }
    }
    axiom8_ = stringify(_axiom8)
    if axiom8_ not in premise:
        premise[axiom8_] = _axiom8

def axiom9(expr):
    _axiom9 = {
        'op': 'axiom 9',
        'left': 'False',
        'right': expr.conclusion
    }
    axiom9_ = stringify(_axiom9)
    if axiom9_ not in expr.premise:
        expr.premise[axiom9_] = _axiom9

def axiom10(expr):
    _axiom10 = {
        'op': 'axiom 10',
        'left': {
            'op': '->',
            'left': {
                'op': '->',
                'left': expr.conclusion,
                'right': 'False'
            },
            'right': expr.conclusion
        },
        'right': expr.conclusion
    }
    axiom10_ = stringify(_axiom10)
    if axiom10_ not in expr.premise:
        expr.premise[axiom10_] = _axiom10
