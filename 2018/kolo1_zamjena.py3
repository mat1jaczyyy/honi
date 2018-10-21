import sys
from collections import deque

n = int(input())
a = [i for i in input().split()]
b = [i for i in input().split()]

d = {}
e = {}

def fail():
    print("NE")
    sys.exit()

def update_graph(key):
    global d, e

    v = {key: True}
    q = deque(e[key])

    while len(q):
        c = q.popleft()
        v[c] = True
        d[c] = d[key]

        for nn in e[c]:
            if nn not in v:
                q.append(nn)

for i in range(n):
    try:
        a[i] = int(a[i])
        x = True
    except ValueError:
        x = False
    
    try:
        b[i] = int(b[i])
        y = True
    except ValueError:
        y = False
    
    if x and y:
        if a[i] != b[i]:
            fail()
    
    elif x:
        if b[i] not in d:
            d[b[i]] = a[i]
            e[b[i]] = []
            
        elif d[b[i]] == 0:
            d[b[i]] = a[i]
            update_graph(b[i])

        elif d[b[i]] != a[i]:
            fail()
    
    elif y:
        if a[i] not in d:
            d[a[i]] = b[i]
            e[a[i]] = []
            
        elif d[a[i]] == 0:
            d[a[i]] = b[i]
            update_graph(a[i])

        elif d[a[i]] != b[i]:
            fail()

    else:
        if a[i] not in d:
            d[a[i]] = 0
            e[a[i]] = []
            
        if b[i] not in d:
            d[b[i]] = 0
            e[b[i]] = []

        if a[i] in d and b[i] in d:
            if d[a[i]] != 0 and d[b[i]] != 0:
                if d[a[i]] != d[b[i]]:
                    fail()
            
            elif d[a[i]] != 0:
                d[b[i]] = d[a[i]]
                update_graph(b[i])
            
            elif d[b[i]] != 0:
                d[a[i]] = d[b[i]]
                update_graph(a[i])

        if b[i] not in e[a[i]]:
            e[a[i]].append(b[i])
        
        if a[i] not in e[b[i]]:
            e[b[i]].append(a[i])

print("DA")