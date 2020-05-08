import math
import random

lookup = dict()

def slowfun(x, y):
    v = lookup.get((x, y))
    if v:
        return v
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    lookup[(x,y)] = v
    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
