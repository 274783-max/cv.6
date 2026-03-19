


circle_1 = {"x": x1, "y": y1, "r": r1}
circle_2 = {"x": x2, "y": y2, "r": r2}

def radius_sum(r1, r2):
    rad = r1 + r2
    return rad

def euclid_distance(x1, y1, x2, y2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    return d

def has_intersection(circle_1, circle_2):
    if d > rad:
        sec = 0
    else d == rad:
        sec = 1
    elif d < rad:
        sec = 2
    return sec

# {"intersects": True, "intersections_count": 2}