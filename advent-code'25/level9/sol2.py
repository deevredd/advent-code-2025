from itertools import combinations

def parse(input_str):
    return [tuple(map(int, l.split(','))) for l in input_str.split('\n') if l.strip()]

def edge_from_points(p1, p2):
    min_x, max_x = min(p1[0], p2[0]), max(p1[0], p2[0])
    min_y, max_y = min(p1[1], p2[1]), max(p1[1], p2[1])
    if min_x == max_x and min_y != max_y:
        return ('V', min_x, min_y, max_y)
    if min_y == max_y and min_x != max_x:
        return ('H', min_y, min_x, max_x)
    return None

def edge_contains(edge, point):
    px, py = point
    if edge[0] == 'H':
        _, y, x1, x2 = edge
        return py == y and x1 <= px <= x2
    else:
        _, x, y1, y2 = edge
        return px == x and y1 <= py <= y2

def edges_intersect(e1, e2):
    if e1[0] == e2[0]:
        return False
    h, v = (e1, e2) if e1[0] == 'H' else (e2, e1)
    _, hy, hx1, hx2 = h
    _, vx, vy1, vy2 = v
    return hx1 < vx < hx2 and vy1 < hy < vy2

def rect_corners(x1, y1, x2, y2):
    return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

def rect_edges(x1, y1, x2, y2):
    corners = rect_corners(x1, y1, x2, y2)
    result = []
    for i in range(4):
        e = edge_from_points(corners[i], corners[(i + 1) % 4])
        if e:
            result.append(e)
    return result

def rect_area(x1, y1, x2, y2):
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

class Polygon:
    def __init__(self, points):
        self.points = points
        self.edges = []
        n = len(points)
        for i in range(n):
            e = edge_from_points(points[i], points[(i + 1) % n])
            if e:
                self.edges.append(e)

    def contains_point(self, point):
        is_inside = False
        for edge in self.edges:
            if edge_contains(edge, point):
                return True
            if edge[0] == 'V':
                _, x, min_y, max_y = edge
                if min_y <= point[1] < max_y and point[0] < x:
                    is_inside = not is_inside
        return is_inside

    def intersect_rect(self, x1, y1, x2, y2):
        r_edges = rect_edges(x1, y1, x2, y2)
        for pe in self.edges:
            for re in r_edges:
                if edges_intersect(re, pe):
                    return True
        return False

    def contains_rect(self, x1, y1, x2, y2):
        corners = rect_corners(x1, y1, x2, y2)
        return all(self.contains_point(c) for c in corners) and not self.intersect_rect(x1, y1, x2, y2)


def get_largest_rect_area(input_str):
    points = parse(input_str)
    return max(rect_area(p1[0], p1[1], p2[0], p2[1]) for p1, p2 in combinations(points, 2))


def get_largest_rect_in_polygon_area(input_str):
    points = parse(input_str)
    polygon = Polygon(points)
    best = 0
    for p1, p2 in combinations(points, 2):
        x1, y1 = p1
        x2, y2 = p2
        if polygon.contains_rect(x1, y1, x2, y2):
            best = max(best, rect_area(x1, y1, x2, y2))
    return best


if __name__ == "__main__":
    with open("/Users/deevnareddy/Projects/advent-code'25/level9/input.txt") as f:
        data = f.read().strip()
    print("PART 1 =", get_largest_rect_area(data))
    print("PART 2 =", get_largest_rect_in_polygon_area(data))