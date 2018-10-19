import sys

class Pt:
	def __init__(self, arr):
		self.k, self.c = arr
	
	def __str__(self):
		return "{" + str(self.k) + ", " + str(self.c) + "}"
	
	def __repr__(self):
		return self.__str__()
	
	def __lt__(self, b):
		return self.k > b.k

n = int(input())
v = [Pt([int(k) for k in input().split()]) for i in range(5)]

v.sort()

for i in v:
	if i.c <= n:
		print(i.k)
		sys.exit()