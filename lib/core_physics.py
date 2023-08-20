
class Particle:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def apply_force(self, force):
        acceleration = [f / self.mass for f in force]
        self.velocity = [v + a for v, a in zip(self.velocity, acceleration)]

    def update_position(self, time_step):
        self.position = [p + v * time_step for p, v in zip(self.position, self.velocity)]

# Add more core physics features here...
