
def detect_collision(particle1, particle2, radius1, radius2):
    # Calculate the distance between the two particles
    dx = particle1.position[0] - particle2.position[0]
    dy = particle1.position[1] - particle2.position[1]
    distance = (dx ** 2 + dy ** 2) ** 0.5

    # Check for collision based on radii
    return distance < (radius1 + radius2)

# Add more collision detection features here...
