a0, b0 = [int(i) for i in input().split()]
ac1, ac2 = [int(i) for i in input().split()]
bc1, bc2 = [int(i) for i in input().split()]

if a0 > b0:
	print(min(ac1, ac2))
elif a0 < b0:
	print(min(bc1, bc2))
else:
	print(min(ac1, ac2, bc1, bc2))