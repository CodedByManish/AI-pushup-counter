import math


def calculate_angle(p1, p2, p3):
    """
    Calculate the angle between three points.
    The points should be in the form of (x, y).
    """
    a = math.dist(p2, p3)
    b = math.dist(p1, p3)
    c = math.dist(p1, p2)

    # Using the cosine rule to calculate the angle
    angle = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    return math.degrees(angle)


def normalize_coordinates(points):
    """
    Normalize the coordinates to the range [0, 1].
    The points should be a list of (x, y) tuples.
    """
    min_x = min(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)

    normalized = [((p[0] - min_x) / (max_x - min_x), (p[1] - min_y) / (max_y - min_y)) for p in points]
    return normalized


def vector_magnitude(vector):
    """
    Calculate the magnitude of a vector.
    The vector should be a tuple (x, y).
    """
    return math.sqrt(vector[0]**2 + vector[1]**2)


def dot_product(v1, v2):
    """
    Calculate the dot product of two vectors.
    Vectors should be tuples (x, y).
    """
    return v1[0] * v2[0] + v1[1] * v2[1]


def cross_product(v1, v2):
    """
    Calculate the cross product of two vectors in 2D.
    Vectors should be tuples (x, y).
    """
    return v1[0] * v2[1] - v1[1] * v2[0]
