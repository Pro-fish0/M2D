
from math_utils import Vector2D

class Creature:
    def __init__(self, position, velocity):
        self.position = Vector2D(*position)
        self.velocity = Vector2D(*velocity)
        self.energy = 100  # Starting energy for the creature

    def move(self):
        self.position += self.velocity
        self.energy -= 1  # Energy decreases as the creature moves

    def eat(self, food):
        self.energy += food.energy_value  # Energy increases when the creature eats food

class Food:
    def __init__(self, position, energy_value=10):
        self.position = Vector2D(*position)
        self.energy_value = energy_value

# Example usage
if __name__ == "__main__":
    creature = Creature([0, 0], [1, 0])
    food = Food([5, 5])
    
    # Simulate creature movement and eating behavior
    for _ in range(100):
        creature.move()
        if creature.position == food.position:
            creature.eat(food)
