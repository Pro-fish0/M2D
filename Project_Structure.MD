
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
- **gui/**: Contains files related to the Graphical User Interface (GUI).
- **Agent_creature/**: Contains the basic implementation of agent creature behavior and simulation.

## lib/ Directory
- **__init__.py**: Makes the folder a Python package.
- **math_utils.py**: Basic mathematical utilities like dot product, vector magnitude, and normalization.
- **core_physics.py**: Basic particle system with mass, position, and velocity.
- **collision_detection.py**: Basic collision detection and resolution between particles.
- **advanced_features.py**: Basic constraints between particles.
- **creature_simulation.py**: Basic simulation of creature behavior.

## Agent_creature/ Directory
- **__init__.py**: Makes the folder a Python package.
- **math_utils.py**: (To be implemented)
- **core_physics.py**: (To be implemented)
- **Simulation.py**: Basic implementation of agent creature behavior and simulation.

## gui/ Directory
- **__init__.py**: Makes the folder a Python package.
- **gui_app.py**: Basic GUI for visualizing the simulation.
