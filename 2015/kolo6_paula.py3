c = 0

for k in range(int(input())):
	if 40 <= sum([int(i) for i in input().split()]) <= 50:
		c += 1

if c == k + 1:
	print("PAULA")
else:
	print(k + 1 - c)