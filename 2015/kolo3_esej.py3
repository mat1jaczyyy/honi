# Dominik Matijaca

import string, itertools

i = str.split(input())
a = int(i[0])
b = int(i[1])

if b % 2 == 0:
	w = max(a, b // 2)
else:
	w = max(a, (b // 2) + 1)

c = 0
r = 1
words = (''.join(i) for i in itertools.product(string.ascii_lowercase, repeat = r))
t = next(words)
for k in range(w - 1):
	c += 1
	try:
		t += " " + next(words)
	except StopIteration:
		r += 1
		words = (''.join(i) for i in itertools.product(string.ascii_lowercase, repeat = r))
		t += " " + next(words)
	
print(t)