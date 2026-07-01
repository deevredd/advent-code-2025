import pathlib

input_path = pathlib.Path(__file__).parent / "input.txt"
data = input_path.read_text(encoding="utf-8").strip()

points = []
for line in data.splitlines():
    if not line:
        continue
    x, y = line.split(",")
    points.append((int(x), int(y)))

part_1 = 0

for a in points:
    for b in points:
        if a == b:
            continue

        area = (abs(a[0] -  b[0]) + 1) * (abs(a[1] - b[1]) + 1)

        part_1 = max(part_1, area) 

print(part_1)     