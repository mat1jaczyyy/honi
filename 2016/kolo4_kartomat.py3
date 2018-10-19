n = int(input())
o = [input() for i in range(n)]
q = input()
t = "***ABCDEFGHIJKLMNOPQRSTUVWXYZ***"

l = []
for i in o:
	if i.startswith(q):
		l += [i[len(q) : len(q) + 1]]

for u in range(3, 29):
	if t[u] not in l:
		t = t[: u] + "*" + t[u + 1 :]

for k in range(0, 32, 8):
	print(t[k : k + 8])