# Dominik Matijaca

q = int(input())
t = 0
for k in range(q):
	i = input()
	t += (int(i[0:-1]) ** int(i[-1]))

print(t)