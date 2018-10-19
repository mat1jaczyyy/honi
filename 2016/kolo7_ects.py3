u, p = [int(i) for i in input().split()]

if p < 30:
	print(8400)
elif p < 55:
	print((u-p)*140)
else:
	print(0)
