
class Creature:
    def __init__(self, position, energy):
        self.position = position
        self.energy = energy

    def move(self, dx, dy):
        self.position[0] += dx
        self.position[1] += dy
        self.energy -= (abs(dx) + abs(dy))

    def eat(self, food_energy):
        self.energy += food_energy

# Add more creature behaviors like reproduction, death, etc., here...
