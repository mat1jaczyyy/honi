from collections import deque
import sys

n = int(sys.stdin.readline())
v = [0] 

for i in sys.stdin.readline().split():
    v.append(int(i))

e = [[] for i in range(n + 1)]

for i in range(n - 1):
    _ = [int(_) for _ in sys.stdin.readline().split()]
    e[_[0]].append(_[1])
    e[_[1]].append(_[0])

sol = 0
sol_single = 0

for i in range(1, n + 1):
    x = [-1] * (n + 1)
    x[i] = v[i]
    sol_single += v[i]
    q = deque([i])

    while len(q):
        c = q.popleft()
        for nn in e[c]:
            if x[nn] == -1:
                x[nn] = x[c] ^ v[nn]
                sol += x[nn]
                q.append(nn)

print(sol // 2 + sol_single)