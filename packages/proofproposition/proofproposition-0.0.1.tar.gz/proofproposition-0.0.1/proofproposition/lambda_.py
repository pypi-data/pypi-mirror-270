def LAMBDA(tree, m):
    if not tree:
        return m
    p = tree
    while 'right' in p:
        p = p['right']
    p['right'] = m
    return tree

def APPLY(tree, m):
    return {
        'op': 'apply',
        'left': tree,
        'right': m
    } if tree else m
