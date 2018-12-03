import sys

n = int(sys.stdin.readline())
p = []

maxx = 0
maxy = 0

for i in range(n):
    p.append([int(j) for j in sys.stdin.readline().split()])
    maxx = max(maxx, p[-1][0] + p[-1][2])
    maxy = max(maxy, p[-1][1] + p[-1][3])

b = [[0] * maxx for i in range(maxy)]
o = []

for i in range(n - 1, -1, -1):
    hit = False
    for y in range(p[i][1], p[i][1] + p[i][3]):
        for x in range(p[i][0], p[i][0] + p[i][2]):
            if b[y][x] == 1:
                hit = True
            b[y][x] = 1
    if hit:
        o.append("NE\n")
    else:
        o.append("DA\n")

for i in range(n - 1, -1, -1):
    sys.stdout.write(o[i])