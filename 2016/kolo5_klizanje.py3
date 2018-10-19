import sys

n, m = [int(i) for i in sys.stdin.readline().split()]
a, b = [int(i) for i in sys.stdin.readline().split()]

sys.stdout.write(str(min(n + m, a + b)) + "\n")