n, d, g = [int(i) for i in input().split()]

c = 0

for k in range(n):
	i = int(input())
	if d <= i <= g:
		c += 1

print(n-c)