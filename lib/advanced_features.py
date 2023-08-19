
from math_utils import Vector2D

class Constraint:
    def __init__(self, particle1, particle2, stiffness):
        self.particle1 = particle1
        self.particle2 = particle2
        self.stiffness = stiffness

    def apply(self):
        # Calculate the vector between the two particles
        delta = self.particle2.position - self.particle1.position

        # Find the current distance
        distance = delta.magnitude()
        
        # Find the difference from the rest distance
        difference = distance - self.rest_distance

        # Calculate the force magnitude
        force_magnitude = self.stiffness * difference

        # Calculate the force vector
        force = delta.normalized() * force_magnitude

        # Apply the force to each particle
        self.particle1.apply_force(-force)
        self.particle2.apply_force(force)

# Example usage
if __name__ == "__main__":
    p1 = Particle([0, 0], [0, 0])
    p2 = Particle([1, 0], [0, 0])
    
    constraint = Constraint(p1, p2, 1)
    constraint.apply()
