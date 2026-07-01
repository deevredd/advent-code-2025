data = open("/Users/deevnareddy/Projects/advent-code'25/level5/input.txt").read().strip('\n').split('\n\n')
ranges = [tuple(map(int, l.split('-'))) for l in data[0].splitlines()]
ids = [int(l) for l in data[1].splitlines()]
print(sum(any(a <= i <= b for a, b in ranges) for i in ids))