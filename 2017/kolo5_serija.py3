h = int(input())
m = int(input()) + int(input())
h += m // 60
m %= 60
print(h, m)
