def f(n):
    j = 0
    a = []
    o = n
    while o > 0:
        a.append(o % 10)
        o = o // 10
    for i in a:
        if i > 2:
            j += 1
    if j == 0 and sum(a) % 10 == 0:
        return 1
    else:
        return 0


b = []
for i in range(1000000, 1300001):
    if f(i) == 1:
        b.append(i)


def h(u):
    a = []
    for i in range(1, u):
        if u % i == 0:
            a.append(i)
    return len(a)


print(b[9], h(b[9]))
print(b[19], h(b[19]))
print(b[29], h(b[29]))
print(b[39], h(b[39]))
print(b[49], h(b[49]))
