n = int(input())
w = input().split()

c = 0
for i in w:
	if i.istitle() and (i.isalpha() or (i[:-1].isalpha() and (i[-1] == "." or i[-1] == "?" or i[-1] == "!"))):
		c += 1
	if i[-1] == "." or i[-1] == "?" or i[-1] == "!":
		print(c)
		c = 0