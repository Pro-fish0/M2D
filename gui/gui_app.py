
import tkinter as tk
from lib.math_utils import Vector
from lib.core_physics import Particle

class SimulationApp:
    def __init__(self, master):
        self.master = master
        master.title("M2D - 2D Physics Simulation")
        
        self.canvas = tk.Canvas(master, width=800, height=600, bg="white")
        self.canvas.pack()
        
        self.particle = Particle(Vector(50, 50), 10, Vector(1, 1))
        
        self.update_simulation()
        
    def update_simulation(self):
        self.canvas.delete("all")  # Clear previous drawings
        
        # Update particle position
        self.particle.update()
        
        # Draw the particle
        x, y = self.particle.position.x, self.particle.position.y
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")
        
        self.master.after(50, self.update_simulation)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationApp(root)
    root.mainloop()
