# Dominik Matijaca

input_1 = [int(k) for k in input().split()]
n = input_1[0]
m = input_1[1]

x = []
for j in range(m):
	input_2 = [k for k in input().split()]
	x.append(input_2)

def listNumbers(n, s):
	nums = []
	for k in range(1, s + 1):
		nums.append(k)
	arr = []
	
	if n > 1:
		lower_arr = listNumbers(n - 1, s)
		for k in lower_arr:
			arr.append(k)
			for i in range(s):
				arr.append(str(nums[i]) + k)
	
	if n == 1:
		for k in range(s):
			arr.append(str(nums[k]))
	
	return arr

def dupes(s):
	arr = []
	[arr.append(i) for i in s if not arr.count(i)]
	return arr

pizze = list(set(listNumbers(n, n)))
pizze.sort()
for k in range(len(pizze)):
	pizze[k] = [pizze[k][i] for i in range(len(pizze[k]))]
	pizze[k] = list(set(pizze[k]))
	pizze[k].sort()
pizze = dupes(pizze)

final = [k for k in pizze]
for k in x:
	deletion = []
	for i in range(len(final)):
		if (k[0] in pizze[i]):
			if (k[1] in pizze[i]):
				deletion.append(i)
	for d in deletion:
		del final[d]
		for z in range(len(deletion)):
			deletion[z] += -1

print(len(final) + 1)