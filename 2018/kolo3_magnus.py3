a = ["H", "O", "N", "I"]
c = 0

sol = 0
for i in input():
    if i == a[c]:
        c = (c + 1) % 4
        if c == 0:
            sol += 1

print(sol)