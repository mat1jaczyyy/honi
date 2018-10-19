a = []

for i in range(int(input())):
	a.append(int(input()))

a.sort()

k = int(input())

c = 0
for i in a:
	if i <= k:
		c += 1
	else:
		break

print(c)
