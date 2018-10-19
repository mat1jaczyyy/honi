# Dominik Matijaca

a = [int(i) for i in input()]
b = [int(i) for i in input()]

while len(a) < len(b):
	a.insert(0, -1)
while len(b) < len(a):
	b.insert(0, -1)
	
for k in range(len(a)):
	if a[k] != -1 and b[k] != -1:
		if a[k] < b[k]:
			a[k] = -1
		if a[k] > b[k]:
			b[k] = -1

c = ""
d = ""

for i in a:
	if i != -1:
		c += str(i) 
for i in b:
	if i != -1:
		d += str(i)

if c == "": c = "YODA"
if d == "": d = "YODA"

if c != "YODA":
	print(int(c))
else:
	print(c)

if d != "YODA":
	print(int(d))
else:
	print(d)