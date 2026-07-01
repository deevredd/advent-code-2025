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
def count_paths(node, has_dac, has_fft):
    if node == "dac":
        has_dac = True
    if node == "fft":
        has_fft = True
    if node == "out":
        return 1 if (has_dac and has_fft) else 0
    return sum(count_paths(n, has_dac, has_fft) for n in graph.get(node, []))

print(count_paths("svr", False, False))