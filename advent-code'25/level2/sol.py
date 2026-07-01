data = open("/Users/deevnareddy/Projects/advent-code'25/level2/input.txt").read().strip()
ranges = []
for part in data.split(','):
    lo, hi = part.split('-')
    ranges.append((int(lo), int(hi)))

total = 0
max_len = max(len(str(hi)) for _, hi in ranges)

for lo, hi in ranges:
    for k in range(1, max_len // 2 + 1):
        low_half = 10**(k-1) if k > 1 else 1
        high_half = 10**k - 1
        mult = 10**k + 1
        for half in range(low_half, high_half + 1):
            cand = half * mult
            if cand < lo:
                continue
            if cand > hi:
                break
            total += cand

print(total)