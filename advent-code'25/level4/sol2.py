grid = [list(line.rstrip('\n')) for line in open("/Users/deevnareddy/Projects/advent-code'25/level4/input.txt") if line.strip('\n') != '']
R, C = len(grid), len(grid[0])
total = 0
while True:
    to_remove = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '@':
                n = sum(
                    1 for dr in (-1, 0, 1) for dc in (-1, 0, 1)
                    if (dr, dc) != (0, 0)
                    and 0 <= r+dr < R and 0 <= c+dc < C
                    and grid[r+dr][c+dc] == '@'
                )
                if n < 4:
                    to_remove.append((r, c))
    if not to_remove:
        break
    for r, c in to_remove:
        grid[r][c] = '.'
    total += len(to_remove)
print(total)