p = 0

for i in range(5):
	p += int(input()) % 2

if p == 0:
	print("savrsena")
else:
	print("normalna")