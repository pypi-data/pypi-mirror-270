from .grammar_ import stringify

axiom = [
    lambda A: {
        'ATOM': 'axiom 0',
        'TYPE': {
            'op': '->',
            'left': A,
            'right': A
        }
    },
    lambda A, B: {
        'ATOM': 'axiom 1',
        'TYPE': {
            'op': '->',
            'left': A,
            'right': {
                'op': '->',
                'left': B,
                'right': A
            }
        }
    },
    lambda A, B, C: {
        'ATOM': 'axiom 2',
        'TYPE': {
            'op': '->',
            'left': {
                'op': '->',
                'left': A,
                'right': {
                    'op': '->',
                    'left': B,
                    'right': C
                }
            },
            'right': {
                'op': '->',
                'left': {
                    'op': '->',
                    'left': A,
                    'right': B
                },
                'right': {
                    'op': '->',
                    'left': A,
                    'right': C
                }
            }
        }
    }
]

def FV(x, cl):
    if stringify(cl['TYPE']) == x:
        return True
    if 'ATOM' in cl:
        return False
    return FV(x, cl['left']) or FV(x, cl['right'])

def define_lambda(x, cl):
    if stringify(cl['TYPE']) == x:
        return axiom[0](x)
    isAtom = 'ATOM' in cl
    if not isAtom and not FV(x, cl['left']):
        if stringify(cl['right']['TYPE']) == x:
            return cl['left']
        if not FV(x, cl['right']):
            isAtom = True
    return {
        'TYPE': {
            'op': '->',
            'left': x,
            'right': cl['TYPE']
        },
        'left': axiom[1](cl['TYPE'], x),
        'right': cl
    } if isAtom else {
        'TYPE': {
            'op': '->',
            'left': x,
            'right': cl['TYPE']
        },
        'left': {
            'TYPE': {
                'op': '->',
                'left': {
                    'op': '->',
                    'left': x,
                    'right': cl['right']['TYPE']
                },
                'right': {
                    'op': '->',
                    'left': x,
                    'right': cl['left']['TYPE']['right']
                }
            },
            'left': axiom[2](x, cl['right']['TYPE'], cl['left']['TYPE']['right']),
            'right': define_lambda(x, cl['left'])
        },
        'right': define_lambda(x, cl['right'])
    }

def iks(_lambda):
    match None if isinstance(_lambda, str) else _lambda['op']:
        case 'lambda':
            return define_lambda(_lambda['left'], iks(_lambda['right']))
        case 'apply':
            left = iks(_lambda['left'])
            right = iks(_lambda['right'])
            return {
                'TYPE': left['TYPE']['right'],
                'left': left,
                'right': right
            }
        case _:
            return {
                'ATOM': 'FV',
                'TYPE': _lambda
            }
