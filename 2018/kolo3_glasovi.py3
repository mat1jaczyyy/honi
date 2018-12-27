n, k = [int(i) for i in input().split()]
m = n // k

if n % k == 0:
    m += 1

for i in range(int(input())):
    a, b = [int(i) // k for i in input().split()]
    if a == b and a < m and b < m:
        print("DA")
    else:
        print("NE")