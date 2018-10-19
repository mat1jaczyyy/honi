x = int(input())
n = int(input())
p = [int(input()) for i in range(n)]

t = (n+1) * x - sum(p)

print(t)