
import math

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return self / mag

# Example usage
if __name__ == "__main__":
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    v3 = v1 + v2  # Vector addition
    print("Vector Addition:", v3.x, v3.y)

    v4 = v1 - v2  # Vector subtraction
    print("Vector Subtraction:", v4.x, v4.y)

    dot_product = v1.dot(v2)  # Dot product
    print("Dot Product:", dot_product)

    magnitude = v1.magnitude()  # Magnitude
    print("Magnitude:", magnitude)

    normalized = v1.normalize()  # Normalization
    print("Normalized:", normalized.x, normalized.y)
