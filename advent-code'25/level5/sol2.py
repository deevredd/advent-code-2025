data = open("/Users/deevnareddy/Projects/advent-code'25/level5/input.txt").read().strip('\n').split('\n\n')
ranges = sorted(tuple(map(int, l.split('-'))) for l in data[0].splitlines())
total = 0
cur_s = cur_e = None
for s, e in ranges:
    if cur_s is None:
        cur_s, cur_e = s, e
    elif s <= cur_e + 1:
        cur_e = max(cur_e, e)
    else:
        total += cur_e - cur_s + 1
        cur_s, cur_e = s, e
total += cur_e - cur_s + 1
print(total)