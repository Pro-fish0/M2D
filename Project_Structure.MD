
# Project Structure for M2D (2D Physics Engine)

## Introduction
This document describes the file and folder structure for the M2D project, a 2D Physics Engine.

## Root Directory
- **README.MD**: Contains overall documentation and usage examples.
- **Project_Structure.MD**: This file, explaining the structure of the project.
- **main.py**: The entry point for running the physics simulation.
- **requirements.txt**: Lists the Python package dependencies.

### Folders
- **lib/**: Holds the core logic and algorithms for the physics engine.
- **gui/**: Holds the Tkinter-based GUI for visualizing the simulation.
- **Agent_creature/**: Holds the AI agent creature model with movement, eating, and reproduction logic.

## lib/ Directory
- **__init__.py**: Makes the folder a Python package.
- **math_utils.py**: Basic mathematical utilities like dot product, vector magnitude, and normalization.
- **core_physics.py**: Basic particle system with mass, position, and velocity.
- **collision_detection.py**: Basic collision detection and resolution between particles based on their radii.
- **advanced_features.py**: Basic implementation of constraints like springs between particles.
- **creature_simulation.py**: Basic creature model with movement and eating behavior.
- **food_spawns.py**: Basic food spawn model with energy values and respawn logic.

## gui/ Directory
- **__init__.py**: Makes the folder a Python package.
- **gui_app.py**: Basic Tkinter-based GUI for visualizing the simulation.

## Agent_creature/ Directory
- **__init__.py**: Makes the folder a Python package.
- **Simulation.py**: Basic AI agent creature model with movement, eating, and reproduction logic.
