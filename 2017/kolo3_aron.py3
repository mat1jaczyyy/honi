prev = ""
c = 1
for i in range(int(input())):
	x = input()
	if x != prev:
		c += 1
	prev = x
print(c)