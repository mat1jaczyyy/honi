n = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

x.sort()
y.sort()

o = "DA"
for i in range(n):
	if x[i] > y[i]:
		o = "NE"
		break

print(o)
