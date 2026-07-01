from math import sqrt

# Read input
points = []
with open("/Users/deevnareddy/Projects/advent-code'25/level8/input.txt") as f:
    for line in f:
        points.append(tuple(map(int, line.strip().split(","))))

n = len(points)

# Generate all pairwise distances
edges = []
for i in range(n):
    x1, y1, z1 = points[i]
    for j in range(i + 1, n):
        x2, y2, z2 = points[j]
        d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
        edges.append((d2, i, j))

# Sort by distance
edges.sort()

# Disjoint Set Union (Union-Find)
parent = list(range(n))
size = [1] * n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

# Connect the 1000 shortest pairs
for _, u, v in edges[:1000]:
    union(u, v)

# Count component sizes
comp = {}
for i in range(n):
    r = find(i)
    comp[r] = comp.get(r, 0) + 1

sizes = sorted(comp.values(), reverse=True)

print(sizes[0] * sizes[1] * sizes[2])