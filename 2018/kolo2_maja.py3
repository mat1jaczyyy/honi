from itertools import product
import sys

n, m, a, b, k = [int(i) for i in sys.stdin.readline().split()]
c = [[int(i) for i in sys.stdin.readline().split()] for i in range(n)]

a += -1
b += -1

sol = 0

for i in product([-1000000007, -1, 1, 1000000007], repeat=k):
    if sum(i) == 0:
        subsol = 0
        ca = a
        cb = b
        for j in i:
            if -1 <= j <= 1:
                cb += j
            else:
                ca += j // 1000000007
            try:
                subsol += c[ca][cb]
            except IndexError:
                break
        if subsol > sol:
            sol = subsol

print(sol)