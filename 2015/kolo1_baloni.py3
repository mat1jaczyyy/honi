# HONI 1. kolo 2015-2016
# Zadatak: BALONI
# Dominik Matijaca

n = int(input())

h_str = input()
h = h_str.split(" ")

for k in range(len(h)):
	h[k] = int(h[k])

def strijela(m, i, h):
	m += -1
	broken = str(i) 
	
	found = 0
	if len(h) > i + 1:
		for k in range(i + 1, len(h)):
			if found == 0:
				if h[k] == m:
					found = 1
					broken += "," + strijela(m, k, h)
	
	return broken

s = 0

while h != []:
	s += 1
	u = strijela(max(h), h.index(max(h)), h)
	
	offset = 0
	for k in u.split(","):	
		del h[int(k) - offset]
		offset += 1

print(s)