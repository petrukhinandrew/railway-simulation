# from tkinter import *
import tkinter as tk
import simulation


class GUI:
    def __init__(self, sim):
        self.sim = sim

        self.root = tk.Tk()
        self.root.title("Railway simulation")
        self.root.geometry('1280x720')

        self.canvas = tk.Canvas(self.root, bg="white", width=1280, height=720)
        self.canvas.pack()
        self.setup_canvas()
        self.train = self.canvas.create_oval(40, 40, 50, 50, fill="blue")
        self.canvas.move(self.train,    150, 150)
        self.display_all_routes_as_straight()
        self.root.mainloop()


        
    def setup_canvas(self):
        self.canvas.create_line(900, 0, 900, 720, fill="black", width=5)


    def display_all_routes_as_straight(self):
        for route in range(len(self.sim.routes)):
            self.display_straight_route(self.sim.routes[route], route)

            
    def display_straight_route(self, route, index):
        line_length = 20
        for checkpoint in range(len(route.checkpoints)):
            if checkpoint != len(route.checkpoints) - 1:
                self.canvas.create_line(100 * (index + 1), 50 + checkpoint * line_length, 100 * (index + 1), 50 + (checkpoint + 1) * line_length, fill="black", width=5)
                self.canvas.create_oval(100 * (index + 1) - 5, 50 + checkpoint * line_length - 5, 100 * (index + 1) + 5, 50 + checkpoint * line_length + 5, fill="green")
            if not route.checkpoints[checkpoint].is_checkpoint:
                self.canvas.create_oval(100 * (index + 1) - 10, 50 + checkpoint * line_length - 10, 100 * (index + 1) + 10, 50 + checkpoint * line_length + 10, fill="red")
        
    def display_route(self):
        self.canvas.create_line(50, 50, 50, 600, fill="black", width=5)
        self.canvas.create_oval(40, 40, 60, 60, fill="red") # currently ovals, could be buttons further
