
from math_utils import Vector2D

class Particle:
    def __init__(self, position, velocity, mass=1.0):
        self.position = Vector2D(position[0], position[1])
        self.velocity = Vector2D(velocity[0], velocity[1])
        self.mass = mass
        self.forces = Vector2D()

    def apply_force(self, force):
        self.forces += force

    def update(self, dt):
        # Update velocity based on forces and time step (dt)
        acceleration = self.forces / self.mass
        self.velocity += acceleration * dt

        # Update position based on velocity and time step (dt)
        self.position += self.velocity * dt

        # Reset forces
        self.forces = Vector2D()

# Example usage
if __name__ == "__main__":
    p = Particle([0, 0], [1, 0])
    gravity = Vector2D(0, -9.81)

    dt = 0.1  # Time step in seconds
    for i in range(100):
        p.apply_force(gravity * p.mass)
        p.update(dt)
        print(f"Time: {i*dt}s, Position: {p.position.x}, {p.position.y}")
