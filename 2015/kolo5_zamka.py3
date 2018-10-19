l = int(input())
d = int(input())
x = int(input())

for i in range(l, d + 1):
	if sum([int(k) for k in str(i)]) == x:
		print(i)
		break

for i in range(d, l - 1, -1):
	if sum([int(k) for k in str(i)]) == x:
		print(i)
		break