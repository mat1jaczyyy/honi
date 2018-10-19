c = 0
for _ in range(int(input())):
	k = [bool(int(i)) for i in input().split()]
	c += int(k[0] and k[1])
print(c)
