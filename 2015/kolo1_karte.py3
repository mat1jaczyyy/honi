# HONI 1. kolo 2015-2016
# Zadatak: KARTE
# Dominik Matijaca

exit = 0

s = input()
s_arr = []

for k in range(len(s) // 3):
	s_arr.append(s[k*3:(k*3)+3])
	
s_arr.sort()

for k in range(1, len(s_arr)):
	for i in range(k):
		if s_arr[k] == s_arr[i]:
			print("GRESKA")
			exit = 1

if exit != 1:
	p = 13
	k = 13
	h = 13
	t = 13		
	for i in s_arr:
		if i[0] == "P":
			p += -1
		if i[0] == "K":
			k += -1
		if i[0] == "H":
			h += -1
		if i[0] == "T":
			t += -1

	print(str(p) + " " + str(k) + " " + str(h) + " " + str(t))