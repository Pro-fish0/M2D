
from lib.core_physics import Particle, apply_gravity
from lib.math_utils import Vector

# Initialize particles
particle1 = Particle(Vector(0, 0), 1, Vector(1, 0))
particle2 = Particle(Vector(5, 0), 1, Vector(-1, 0))

# Time step for the simulation
dt = 0.1

# Main simulation loop
for step in range(100):
    # Apply forces (e.g., gravity)
    apply_gravity([particle1, particle2], dt)
    
    # Update particles
    particle1.update(dt)
    particle2.update(dt)
    
    # Print current state
    print(f"Step {step+1}:")
    print(f"  Particle 1: Position = {particle1.position}, Velocity = {particle1.velocity}")
    print(f"  Particle 2: Position = {particle2.position}, Velocity = {particle2.velocity}")
