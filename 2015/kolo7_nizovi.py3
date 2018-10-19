level = 0
j = 0
for char in input():
	if char == "{":
		if j == 1:
			print(" " * level, end = "")
		print(char)
		level += 2
		j = 1
	elif char == ",":
		print(char)
		print(" " * level, end = "")
	elif char == "}":
		level += -2
		if j == 0:
			print()
		print(" " * level, end = "")
		print(char, end = "")
		j = 0
	else:
		if j == 1:
			print(" " * level, end = "")
		print(char, end = "")
		j = 0