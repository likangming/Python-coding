myself = {'apples': 3, 'bananas': 6, 'pear': 32, 'peach': 2, 'grape': 12}
she = ['orange', 'jujube', 'orange', 'tomato', 'orange']


def addtoinvendory(a, b):
    d1 = {}
    for i in b:
        d1[i] = b.count(i)
    for k, v in d1.items():
        if k in a.keys():
            a[k] = a[k] + v
        else:
            a[k] = v
    return a


def invendory(inven):
    print('Invendory:')
    total = 0
    for k, v in inven.items():
        print('-', k, v)
        total = total + v
    print('Total:', total)


myself = addtoinvendory(myself, she)
invendory(myself)
