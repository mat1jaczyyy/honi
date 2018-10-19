adut = {'A': 11,
		'K': 4,
		'Q': 3,
		'J': 20,
		'T': 10,
		'9': 14,
		'8': 0,
		'7': 0}

obic = {'A': 11,
		'K': 4,
		'Q': 3,
		'J': 2,
		'T': 10,
		'9': 0,
		'8': 0,
		'7': 0}

n, b = [i for i in input().split()]
c = 0

for k in range(int(n)):
	for i in range(4):
		x = input()
		if x[1] == b:
			c += adut[x[0]]
		else:
			c += obic[x[0]]

print(c)