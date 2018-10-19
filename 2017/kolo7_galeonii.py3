h = 0
r = 0

for _ in range(int(input())):
	a = [int(i) for i in input().split()]
	
	if a[0]*17*29 + a[1]*17 + a[2] > a[3]*17*29 + a[4]*17 + a[5]:
		h += a[0] + a[3]
	else:
		r += a[0] + a[3]

print(h, r)
