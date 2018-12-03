a = int(input())
sa = [int(input()) for i in range(a)]

b = int(input())
sb = [int(input()) for i in range(b)]

c = 0
d = {}
for i in sa:
    if i <= 1440:
        c += 1
    d[i] = 0

for i in sb:
    if i <= 1440:
        c += 1
    d[i] = 1

print(c)

state = -1
p = [0, 0]
sol = 0
for i in sorted(d.keys()):
    p[d[i]] += 1

    if state == -1:
        state = 1 - d[i]
    else:
        if d[i] == state:
            if p[state] > p[1 - state]:
                sol += 1
                state = 1 - state

print(sol) 