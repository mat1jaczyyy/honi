a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

c = []

for i in b:
	if not a[0] <= i <= a[1]:
		c += [i]

print(min(c))