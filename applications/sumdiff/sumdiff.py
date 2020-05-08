"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

val_map = dict()

for i, a in enumerate(q):
    for b in q[i:]:
        val = f(a) + f(b)
        if val_map.get(val):
            val_map[val].add((a, b))
        else:
            val_map[val] = {(a, b)}
        val_map[val].add((b, a))


q = list(reversed(q))
for i, c in enumerate(q):
    for d in q[i+1:]:
        val = f(c) - f(d)
        sums = val_map.get(val)
        if sums:
            for pair in sums:
                print(f"f({pair[0]}) + f({pair[1]}) = f({c}) - f({d})")
