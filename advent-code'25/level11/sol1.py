from functools import lru_cache

graph = {}
with open("/Users/deevnareddy/Projects/advent-code'25/level11/input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        name, rest = line.split(':')
        graph[name.strip()] = rest.split()

@lru_cache(maxsize=None)
def count_paths(node):
    if node == "out":
        return 1
    return sum(count_paths(n) for n in graph.get(node, []))

print(count_paths("you"))