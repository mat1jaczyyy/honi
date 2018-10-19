n, m = [int(i) for i in input().split()]

c = 0
for _ in range(n):
	c += int(not bool(int(input()) % m))
print(c)
