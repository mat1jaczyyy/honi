days = ["ponedjeljak", "utorak", "srijeda", "cetvrtak", "petak", "subota", "nedjelja"]

s = int(input())
a = int(input())
b = int(input())
d = days.index(input()) - a

while s > 0:
	d += a
	s += -b

print(days[d % 7])