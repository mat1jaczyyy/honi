from math import ceil
from sys import stdout
n, k, m = [int(i) for i in input().split()]

i = ceil(m / k) - 1
nt = 2 * n - 2
ci = i % nt

if ci == 0:
	stdout.write(str(ceil(i / nt) * k + (m - i * k)) + " ")
else:
	stdout.write(str(ceil(i / nt) * k) + " ")

if ci < n - 1:
	s2 = 2 * (i // nt)
	s1 = (s2 + 1) * k
	s2 *= k

	for j in range(1, ci):
		stdout.write(str(s1) + " ")

	if ci != 0:
		stdout.write(str(s2 + (m - i * k)) + " ")

	for j in range(ci + 1, n - 1):
		stdout.write(str(s2) + " ")
else:
	s1 = 2 * (i // nt) + 1
	s2 = (s1 + 1) * k
	s1 *= k

	for j in range(1, nt - ci):
		stdout.write(str(s1) + " ")

	if ci != n - 1:
		stdout.write(str(s1 + (m - i * k)) + " ")

	for j in range(nt - ci + 1, n - 1):
		stdout.write(str(s2) + " ")

if ci == n - 1:
	stdout.write(str(ceil((i - n + 1) / nt) * k + (m - i * k)) + "\n")
else:
	stdout.write(str(ceil((i - n + 1) / nt) * k) + "\n")
