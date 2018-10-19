# Dominik Matijaca

import string

def r(i):
	while i < 0:
		i += 26
	while i > 25:
		i += -26
	return i

q = int(input())

cmds = {}
for k in range(q):
	cmd = input().split()
	if len(cmd) == 2:
		cmds[int(cmd[1]) - 1] = cmd[0]
	if len(cmd) == 3:
		cmds[int(cmd[1]) - 1] = cmd[2]

s = [i for i in string.ascii_lowercase]
count = [0 for i in range(26)]
smjer = 1
n = 0

for k in range(max(list(cmds.keys())) + 1):
	count[r(n)] += 1
	if k in cmds:
		if cmds[k] == "SMJER":
			smjer = -smjer
		else:
			print(count[s.index(cmds[k])])
	n += smjer