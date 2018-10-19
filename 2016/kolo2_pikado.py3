n = int(input())
s, k = [int(i) for i in input().split()]

def check(n, s, k):
	if s * k == n:
		if k != 2:
			return False
	if s * k > n:
		return False
	if n - (s * k) == 1:
		return False
	return True

x = n
if check(n, s, k):
	x = n - (s * k)

def grade(x, n):
	if x == n:
		return "Lose"
	if x > 0:
		return "Dobro"
	if x == 0:
		return "Odlicno"

print(grade(x, n))