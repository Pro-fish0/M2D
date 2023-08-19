
# Project Structure for M2D (2D Physics Engine)

## Table of Contents
1. [Introduction](#introduction)
2. [Root Directory](#root-directory)
3. [Lib Directory](#lib-directory)
4. [GUI Directory](#gui-directory)

## Introduction
This document describes the file and folder structure for the M2D project, a 2D Physics Engine. 

## Root Directory
### Files
- `README.MD`: Contains overall documentation and usage examples.
- `Project_Structure.MD`: This file, explaining the structure of the project.
- `main.py`: The entry point for running the physics simulation.
- `requirements.txt`: Lists the Python package dependencies.

### Folders
- `lib/`: Holds the core logic and algorithms for the physics engine.
- `gui/`: Contains files related to the Graphical User Interface.

## Lib Directory
- `__init__.py`: Makes the folder a Python package.
- `math_utils.py`: Basic mathematical operations and utilities.
- `core_physics.py`: Core physics algorithms, including particle systems and forces.
- `collision_detection.py`: Algorithms for detecting and resolving collisions.
- `advanced_features.py`: More advanced features like constraints and joints.
- `creature_simulation.py`: Algorithms for simulating creature behavior.

## GUI Directory
- `__init__.py`: Makes the folder a Python package.
- `gui_app.py`: Code related to the GUI for visualizing the physics simulations.
