s = input()
for _ in range(int(input())):
	a, b, c, d = [int(i) for i in input().split()]
	if b - a != d - c:
		print("NE")
	else:
		x = [0] * 26
		y = [0] * 26
		for i in range(a - 1, b):
			x[ord(s[i]) - 97] += 1
		for i in range(c - 1, d):
			y[ord(s[i]) - 97] += 1
		print("DA" if x == y else "NE")