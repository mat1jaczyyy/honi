n = int(input())
b = [int(input()) for i in range(n)]

c = 0
for i in range(n):
	if b[i] >= i + 1:
		c += 1

print(c)