pos = 50
count = 0
for line in open("/Users/deevnareddy/Projects/advent-code'25/level1/input.txt"):
    line = line.strip()
    if not line:
        continue
    d, n = line[0], int(line[1:])
    a = pos
    if d == 'R':
        b = a + n
        c = b // 100 - a // 100
    else:
        b = a - n
        c = (a - 1) // 100 - (b - 1) // 100
    count += c
    pos = b % 100
print(count)