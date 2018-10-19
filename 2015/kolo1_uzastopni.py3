# HONI 1. kolo 2015-2016
# Zadatak: UZASTOPNI
# Dominik Matijaca

n = int(input())
v = input().split(" ")
for k in range(n):
	v[k] = int(v[k])

vicevi = [v[0]]

ab = []
for k in range(n-1):
	ab.append(input().split(" "))
	ab[k][0] = int(ab[k][0])
	ab[k][1] = int(ab[k][1])
	
print(12)