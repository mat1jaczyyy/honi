import sys

n = int(sys.stdin.readline())

row = [[] for i in range(n)]
col = [[] for i in range(n)]

i = 0
for l in [int(_) for _ in sys.stdin.readline().split()]:
    if l != -1:
        row[i].append(l)
        col[l].append(i)
    i += 1

i = 0
for r in [int(_) for _ in sys.stdin.readline().split()]:
    if r != -1:
        if len(row[i]):
            r = n - r - 1
            if r > row[i][0]:
                row[i].append(r)
                col[r].append(i)
            elif r < row[i][0]:
                print("NE")
                sys.exit()
        else:
            print("NE")
            sys.exit()
    else:
        if len(row[i]):
            print("NE")
            sys.exit()
    i += 1

i = 0
for u in [int(_) for _ in sys.stdin.readline().split()]:
    if u != -1:
        if len(col[i]):
            if u < col[i][0]:
                if len(row[u]):
                    row[u].sort()
                    if i < row[u][0] or i > row[u][-1]:
                        print("NE")
                        sys.exit()
                    else:
                        col[i].append(u)
                        row[u].append(i)
                else:
                    print("NE")
                    sys.exit()
            elif u > col[i][0]:
                print("NE")
                sys.exit()
        else:
            if len(row[u]):
                if i < row[u][0] or i > row[u][-1]:
                    print("NE")
                    sys.exit()
                else:
                    col[i].append(u)
                    row[u].append(i)
            else:
                print("NE")
                sys.exit()
    else:
        if len(col[i]):
            print("NE")
            sys.exit()
    i += 1

i = 0
for d in [int(_) for _ in sys.stdin.readline().split()]:
    if d != -1:
        if len(col[i]):
            d = n - d - 1
            if d > col[i][-1]:
                if len(row[d]):
                    if i < row[d][0] or i > row[d][-1]:
                        print("NE")
                        sys.exit()
                    else:
                        col[i].append(d)
                        row[d].append(i)
                else:
                    print("NE")
                    sys.exit()
            elif d < col[i][-1]:
                print("NE")
                sys.exit()
        else:
            print("NE")
            sys.exit()
    else:
        if len(col[i]):
            print("NE")
            sys.exit()
    i += 1

print("DA")