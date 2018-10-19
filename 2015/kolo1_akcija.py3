# HONI 1. kolo 2015-2016
# Zadatak: AKCIJA
# Dominik Matijaca

n = int(input())

c = []
for k in range(n):
	c.append(int(input()))

c.sort()

pay = 0
for k in range(len(c) - (len(c) % 3)):
	if k % 3 != 0:
		pay += c[k]

for k in c[(len(c) - (len(c) % 3)):len(c)]:
	pay += k

print(pay)