n, m = [int(i) for i in input().split()]
a = [input() for i in range(n)]

k = []
for i in range(n):
    for j in [i for i, ch in enumerate(a[i]) if ch == '#']:
        k.append([i, j])

sol = 0

for i in range(n):
    for j in range(m):
        for h in range(i + 1, n + 1):
            for w in range(j + 1, m + 1):
                valid = True
                for _ in k:
                    if i <= _[0] < h and j <= _[1] < w:
                        valid = False
                        break
                if valid:
                    sol += ((h - i) * (w - j))

print(sol)