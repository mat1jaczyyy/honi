# Dominik Matijaca

import math

map = {}
map[2] = ["a", "b", "c"]
map[3] = ["d", "e", "f"]
map[4] = ["g", "h", "i"]
map[5] = ["j", "k", "l"]
map[6] = ["m", "n", "o"]
map[7] = ["p", "q", "r", "s"]
map[8] = ["t", "u", "v"]
map[9] = ["w", "x", "y", "z"]

dict_len = int(input())
dictionary = []

for k in range(dict_len):
	dictionary.append(input())

num = [int(k) for k in list(input())]
count = 0

for k in dictionary:
	if len(k) == len(num):
		match = 0
		for i in range(len(k)):
			if k[i] in map[num[i]]:
				match += 1
		if match == len(num):
			count += 1

print(count)	