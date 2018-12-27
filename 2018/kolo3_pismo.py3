input()
a = [int(i) for i in input().split()]

sol = 2147483647
for i in range(len(a) - 1):
    sol = min(abs(a[i] - a[i+1]), sol)

print(sol)