import re
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

# from collections import deque

total = 0
with open("/Users/deevnareddy/Projects/advent-code'25/level10/input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        targets = list(map(int, re.search(r'\{(.*?)\}', line).group(1).split(',')))
        n = len(targets)

        buttons = []
        for m in re.finditer(r'\((.*?)\)', line):
            idxs = [int(x) for x in m.group(1).split(',')]
            col = [0] * n
            for i in idxs:
                col[i] = 1
            buttons.append(col)

        A = np.array(buttons).T  # n x num_buttons
        b = np.array(targets)
        num_buttons = len(buttons)

        c = np.ones(num_buttons, dtype=int)
        constraints = LinearConstraint(A, b, b)
        bounds = Bounds(0, np.inf)
        integrality = np.ones(num_buttons, dtype=int)

        res = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)
        total += round(res.fun)

print(total)