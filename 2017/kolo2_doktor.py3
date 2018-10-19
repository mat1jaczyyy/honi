n = int(input())
a = [int(i) for i in input().split()]

def value(x):
	r = 0
	for i in range(len(x)):
		if i+1 == x[i]:
			r += 1
	return r

c = value(a)
o = [0, 0]

for i in range(n):
	for j in range(1, n - i):
		b = value(a[:i] + a[i:i+j+1][::-1] + a[i+j+1:])
		if b > c:
			c = b
			o = [i, j]

print(a[o[0]], a[o[1]])