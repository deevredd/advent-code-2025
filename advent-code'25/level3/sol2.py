def best_subseq(s, k):
    stack = []
    to_remove = len(s) - k
    for c in s:
        while stack and to_remove > 0 and stack[-1] < c:
            stack.pop()
            to_remove -= 1
        stack.append(c)
    return ''.join(stack[:k])

total = 0
for line in open("/Users/deevnareddy/Projects/advent-code'25/level3/input.txt"):
    line = line.strip()
    if not line:
        continue
    total += int(best_subseq(line, 12))
print(total)