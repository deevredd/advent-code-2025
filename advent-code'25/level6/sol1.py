lines = [l.rstrip('\n') for l in open("/Users/deevnareddy/Projects/advent-code'25/level6/input.txt") if l.strip('\n') != '']
width = max(len(l) for l in lines)
lines = [l.ljust(width) for l in lines]
op_row = lines[-1]
num_rows = lines[:-1]

groups, cur = [], []
for c in range(width):
    if op_row[c] == ' ' and all(nr[c] == ' ' for nr in num_rows):
        if cur:
            groups.append(cur); cur = []
    else:
        cur.append(c)
if cur:
    groups.append(cur)

total = 0
for g in groups:
    op = next(op_row[c] for c in g if op_row[c] in '+*')
    nums = [int(s) for s in (''.join(nr[c] for c in g).strip() for nr in num_rows) if s]
    val = sum(nums) if op == '+' else __import__('math').prod(nums)
    total += val
print(total)