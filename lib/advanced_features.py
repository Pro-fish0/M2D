
class Constraint:
    def __init__(self, particle1, particle2, rest_distance):
        self.particle1 = particle1
        self.particle2 = particle2
        self.rest_distance = rest_distance

    def enforce(self):
        # Calculate the current distance between particles
        dx = self.particle1.position[0] - self.particle2.position[0]
        dy = self.particle1.position[1] - self.particle2.position[1]
        current_distance = (dx ** 2 + dy ** 2) ** 0.5

        # Calculate the corrective force
        difference = self.rest_distance - current_distance
        force = [dx / current_distance * difference, dy / current_distance * difference]

        # Apply the corrective force
        self.particle1.apply_force(force)
        self.particle2.apply_force([-x for x in force])

# Add more advanced features like joints, springs, etc., here...
