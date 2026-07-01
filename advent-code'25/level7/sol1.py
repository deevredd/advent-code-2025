grid = [l.rstrip('\n') for l in open("/Users/deevnareddy/Projects/advent-code'25/level7/input.txt") if l.strip('\n') != '']
R, C = len(grid), len(grid[0])
srow = next(r for r, row in enumerate(grid) if 'S' in row)
scol = grid[srow].index('S')
active = {scol}
splits = 0
for r in range(srow + 1, R):
    nxt = set()
    for c in active:
        if 0 <= c < C and grid[r][c] == '^':
            splits += 1
            if c - 1 >= 0: nxt.add(c - 1)
            if c + 1 < C: nxt.add(c + 1)
        else:
            nxt.add(c)
    active = nxt
print(splits)