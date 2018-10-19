# HONI 1. kolo 2015-2016
# Zadatak: RELATIVNOST
# Dominik Matijaca

nc = input().split(" ")
n = int(nc[0])
c = int(nc[1])

a_str = input()
b_str = input()

a = a_str.split(" ")
b = b_str.split(" ")
for k in range(n):
	a[k] = int(a[k])
	b[k] = int(b[k])
	
q = int(input())
for k in range(q):
	p_str = input().split(" ")
	a[int(p_str[0]) - 1] = int(p_str[1])
	b[int(p_str[0]) - 1] = int(p_str[2])

print(0)