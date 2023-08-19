
from math_utils import Vector2D

def detect_collision(particle1, particle2):
    # Calculate the distance between the two particles
    distance_vector = particle1.position - particle2.position
    distance = distance_vector.magnitude()
    
    # Assume each particle has a radius of 1 unit for simplicity
    # If the distance between particles is less than 2 units, they are colliding
    if distance < 2:
        return True
    return False

def resolve_collision(particle1, particle2):
    # For simplicity, we'll use a very basic collision resolution mechanism
    # Reverse the velocities of both particles
    particle1.velocity, particle2.velocity = particle2.velocity, particle1.velocity

# Example usage
if __name__ == "__main__":
    p1 = Particle([0, 0], [1, 0])
    p2 = Particle([1, 0], [-1, 0])
    
    if detect_collision(p1, p2):
        print("Collision detected. Resolving...")
        resolve_collision(p1, p2)
