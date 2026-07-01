import re
from itertools import combinations

total = 0
with open("/Users/deevnareddy/Projects/advent-code'25/level10/input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        lights = re.search(r'\[(.*?)\]', line).group(1)
        n = len(lights)
        target = 0
        for i, ch in enumerate(lights):
            if ch == '#':
                target |= (1 << i)

        buttons = []
        for m in re.finditer(r'\((.*?)\)', line):
            mask = 0
            for idx in m.group(1).split(','):
                mask |= (1 << int(idx))
            buttons.append(mask)

        best = None
        for r in range(len(buttons) + 1):
            found = False
            for combo in combinations(buttons, r):
                x = 0
                for b in combo:
                    x ^= b
                if x == target:
                    best = r
                    found = True
                    break
            if found:
                break

        total += best

print(total)