total = 0
for line in open("/Users/deevnareddy/Projects/advent-code'25/level3/input.txt"):
    line = line.strip()
    if not line:
        continue
    best = 0
    n = len(line)
    for i in range(n):
        for j in range(i + 1, n):
            val = int(line[i] + line[j])
            if val > best:
                best = val
    total += best
print(total)