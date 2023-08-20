
import math

def dot_product(vec1, vec2):
    return sum(x*y for x, y in zip(vec1, vec2))

def magnitude(vec):
    return math.sqrt(sum(x*x for x in vec))

def normalize(vec):
    mag = magnitude(vec)
    assert mag > 0, "Cannot normalize a zero-length vector"
    return [x/mag for x in vec]

# Add more math utility functions here...
