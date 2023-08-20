
import tkinter as tk

class GUIApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack()

    def draw_particle(self, x, y, radius):
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="blue")

# Create a Tkinter window and attach the GUIApp
root = tk.Tk()
app = GUIApp(root)
root.mainloop()
