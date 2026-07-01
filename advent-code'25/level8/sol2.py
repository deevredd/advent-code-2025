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

edges.sort()

# Union-Find
parent = list(range(n))
size = [1] * n
components = n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

for _, u, v in edges:
    ru, rv = find(u), find(v)
    if ru != rv:
        if size[ru] < size[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        size[ru] += size[rv]
        components -= 1

        if components == 1:
            print(points[u][0] * points[v][0])
            break