pos = 50
count = 0
for line in open("/Users/deevnareddy/Projects/advent-code'25/level1/input.txt"):
    line = line.strip()
    if not line:
        continue
    d, n = line[0], int(line[1:])
    pos = (pos - n) % 100 if d == 'L' else (pos + n) % 100
    if pos == 0:
        count += 1
print(count)