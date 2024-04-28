from functools import reduce
from .grammar_ import stringify

def output(step):
    space = len(str(len(step)))
    width = reduce(lambda a, b: max(a, len(b['TYPE'])), step, 0)
    return [
        f"#{1+i}".rjust(space)+'  '+step[i]['TYPE'].ljust(width)+'  '+step[i]['reason']
        for i in range(len(step))
    ]

def answer(premise, cl):
    history = {}
    step = []

    def _answer(cl):
        TYPE_ = stringify(cl['TYPE'])
        if TYPE_ in history: return
        match cl['ATOM'] if 'ATOM' in cl else None:
            case 'axiom 0':
                reason = 'theorem'
            case 'axiom 1':
                reason = 'axiom 1'
            case 'axiom 2':
                reason = 'axiom 2'
            case 'FV':
                if isinstance(premise[TYPE_], str):
                    reason = 'premise'
                else:
                    op = premise[TYPE_]['op']
                    reason = op if op.startswith('axiom ') else 'premise'
            case _:
                _answer(cl['right'])
                _answer(cl['left'])
                p1 = '#'+str(1+history[stringify(cl['right']['TYPE'])])
                p2 = '#'+str(1+history[stringify(cl['left']['TYPE'])])
                p3 = '#'+str(1+len(step))
                reason = f"{p2}={p1}->{p3}"
        history[TYPE_] = len(step)
        step.append({
            'TYPE': TYPE_,
            'reason': reason
        })

    _answer(cl)
    return output(step)
