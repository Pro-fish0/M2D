
from lib.core_physics import Particle
from lib.math_utils import Vector2D

def main():
    # Initialize a particle at position (0, 0) with velocity (1, 0)
    p = Particle([0, 0], [1, 0])
    
    # Define gravity force vector
    gravity = Vector2D(0, -9.81)
    
    # Time step in seconds
    dt = 0.1  
    
    # Simulate the particle's motion for 100 time steps
    for i in range(100):
        # Apply gravitational force to the particle
        p.apply_force(gravity * p.mass)
        
        # Update particle's state
        p.update(dt)
        
        # Print particle's state
        print(f"Time: {i * dt}s, Position: {p.position.x}, {p.position.y}")

if __name__ == "__main__":
    main()
