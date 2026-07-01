data = open("/Users/deevnareddy/Projects/advent-code'25/level2/input.txt").read().strip()
ranges = []
for part in data.split(','):
    lo, hi = part.split('-')
    ranges.append((int(lo), int(hi)))

def divisors_less_than(n):
    return [d for d in range(1, n) if n % d == 0]

total = 0
max_len = max(len(str(hi)) for _, hi in ranges)

for lo, hi in ranges:
    found = set()
    for L in range(2, max_len + 1):
        for k in divisors_less_than(L):
            m = L // k
            low_unit = 10**(k-1) if k > 1 else 1
            high_unit = 10**k - 1
            for unit in range(low_unit, high_unit + 1):
                s = str(unit) * m
                cand = int(s)
                if cand < lo:
                    continue
                if cand > hi:
                    break
                found.add(cand)
    total += sum(found)

print(total)