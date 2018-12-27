import sys
n, e = [int(i) for i in input().split()]

d = {'o': 1, 'x': 0}
a = []

for i in range(n):
    a.append([])
    for c in input():
        a[i].append(d[c])

def flip_row(x):
    global b, n
    for i in range(n):
        b[x][i] = 1 - b[x][i]

def flip_column(x):
    global b, n
    for i in range(n):
        b[i][x] = 1 - b[i][x]

b = []
for i in range(2**n):
    for j in range(2**n):
        b = []

        for k in range(n):
            b.append(a[k].copy())
        
        for k in range(n):
            if 2**k & i:
                flip_row(k)
            if 2**k & j:
                flip_column(k)
        
        c = 0
        for x in range(n):
            for y in range(n):
                c += b[x][y]

        if c <= e:
            print("DA")
            sys.exit()

print("NE")