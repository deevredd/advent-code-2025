grid = [l.rstrip('\n') for l in open("/Users/deevnareddy/Projects/advent-code'25/level7/input.txt") if l.strip('\n') != '']
R, C = len(grid), len(grid[0])
srow = next(r for r, row in enumerate(grid) if 'S' in row)
scol = grid[srow].index('S')
active = {scol: 1}
for r in range(srow + 1, R):
    nxt = {}
    for c, cnt in active.items():
        if 0 <= c < C and grid[r][c] == '^':
            for nc in (c - 1, c + 1):
                if 0 <= nc < C:
                    nxt[nc] = nxt.get(nc, 0) + cnt
        else:
            nxt[c] = nxt.get(c, 0) + cnt
    active = nxt
print(sum(active.values()))