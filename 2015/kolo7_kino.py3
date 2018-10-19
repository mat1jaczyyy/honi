n, k, p = [int(i) for i in input().split()]

if sum([int(input()) // p for i in range(n)]) < k:
	print("DA")
else:
	print("NE")