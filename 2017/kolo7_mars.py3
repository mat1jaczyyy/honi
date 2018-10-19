m, g = [int(i) for i in input().split()]
x, y = [int(i) for i in input().split()]

c = g*12 + m - x + y

print(c % 12, c // 12)
