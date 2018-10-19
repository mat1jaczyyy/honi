K = int(input())
Z = [int(i) for i in input().split()]

x = input().replace("?", str(Z[0]))

def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

for k in range(1, 50):
	repeat = True
	while repeat:
		repeat = False
		for lbracket in findOccurences(x, "("):
			rbrackets = findOccurences(x[lbracket:], ")")
			cb = 0
			for i in range(lbracket, len(x)):
				if x[i] == "(":
					cb += 1
				if x[i] == ")":
					cb += -1
				if cb == 0:
					break
			rbracket = i
			c = x[lbracket+1:rbracket].count('+') + x[lbracket+1:rbracket].count('*')
			if c == k:
				y = x[lbracket+1:rbracket]
				z = eval(y)
				y = y.replace("*", "+")
				if eval(y) > Z[k]:
					z = Z[k]
				x = x[:lbracket+1] + str(z) + x[rbracket:]
				repeat = True
				break
				
print(x[1:-1])