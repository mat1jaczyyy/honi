n = int(input())

e = [False for i in range(26)]
arr = []

for k in range(n):
	i = input()
	for j in range(97, 123):
		if chr(j) in i:
			e[j - 97] = True
	arr += [i]

s = ""
for k in range(26):
	if e[k]:
		s += chr(k + 97)

order = [int(i) for i in input().split()]

def code(x, key, r):
	a = []
	for k in x:
		s = ""
		for c in k:
			s += key[r.index(c)]
		a += [s]
	return a

from itertools import permutations
from sys import exit

for whytupleomg in permutations(s):
	p = ''.join(whytupleomg)
	coded = code(arr, p, s)
	
	after = []
	for i in order:
		after += [coded[i-1]]
	
	coded.sort()
	
	if coded == after:
		print("DA")
		g = ""
		for k in range(26):
			if chr(k + 97) not in p:
				g += chr(k + 97)
			else:
				g += p[s.index(chr(k + 97))]
		print(g)
		exit()
print("NE")