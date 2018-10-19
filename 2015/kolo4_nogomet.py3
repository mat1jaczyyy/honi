# Dominik Matijaca

import sys, math

def prosti():
	yield 2
	s = 3
	while True:
		found = True
		for k in range(2, s):
			if s % k == 0:
				found = False
				break
		if found == True:
			yield s
		s += 1

n = int(input())

p = prosti()
x = next(p)
while x <= math.sqrt(n):
	if n % x == 0:
		print(x)
		sys.exit()
	x = next(p)

print(n)