import tkinter as tk
import simulation


class RouteWrapper:
    def __init__(self, route):
        self.route = route
        self.checkpoints = []

        
class CheckpointWrapper:
    def __init__(self, checkpoint, x, y):
        self.checkpoint = checkpoint
        self.x = x
        self.y = y
        self.radius = 5 if self.checkpoint.is_checkpoint else 10
        self.color = "green" if self.checkpoint.is_checkpoint else "red"


class TrainWrapper:
    def __init__(self, train, route_wrapper, x, y):
        self.train = train
        self.route_wrapper = route_wrapper
        self.x = x
        self.y = y
        self.radius = 5

        
class GUI:
    def __init__(self, sim):
        self.sim = sim

        self.root = tk.Tk()
        self.root.title("Railway simulation")
        self.root.geometry('1280x720')

        self.canvas = tk.Canvas(self.root, bg="white", width=1280, height=720)
        self.canvas.pack()
        self.setup_canvas()

        self.routes = []
        self.trains = []
        
        # option to move circles. how to store them?
        
        # self.train = self.canvas.create_oval(40, 40, 50, 50, fill="blue")
        # self.canvas.move(self.train, -10, -10) # relative movement

        self.setup_routes()
        self.display_all_routes_as_straight()

        self.tick()
        self.tick()
        self.root.mainloop()


        
    def setup_canvas(self):
        self.canvas.create_line(900, 0, 900, 720, fill="black", width=5)
        self.canvas.create_line(1070, 50, 1070, 250, fill="black", width=5)
        self.canvas.create_text(985, 75, text="Tuda")
        self.canvas.create_text(1175, 75, text="Suda")
        self.current_route_tag = self.canvas.create_text(1070, 25, text="Route Tag")
        # self.canvas.configure(self.current_route_tag, text="new route tag, look!")


    def setup_routes(self):
        for route in range(len(self.sim.routes)):
            self.setup_route(self.sim.routes[route], route)


    def display_straight_route(self, route, index):
        line_length = 20
        for checkpoint in range(len(route.checkpoints)):
            if checkpoint != len(route.checkpoints) - 1:
                self.canvas.create_line(100 * (index + 1), 50 + checkpoint * line_length, 100 * (index + 1), 50 + (checkpoint + 1) * line_length, fill="black", width=5)
            new_checkpoint = route.checkpoints[checkpoint]
            self.canvas.create_oval(new_checkpoint.x - new_checkpoint.radius, new_checkpoint.y - new_checkpoint.radius, new_checkpoint.x + new_checkpoint.radius, new_checkpoint.y + new_checkpoint.radius, fill=new_checkpoint.color)

        
    def display_all_routes_as_straight(self):
        for route in range(len(self.routes)):
            self.display_straight_route(self.routes[route], route)

        
    def setup_route(self, route, index):
        line_length = 20
        new_route = RouteWrapper(route)
        self.routes.append(new_route)
        for checkpoint in range(len(route.checkpoints)):
            new_checkpoint = CheckpointWrapper(route.checkpoints[checkpoint], 100 * (index + 1),  50 + checkpoint * line_length)
            new_route.checkpoints.append(new_checkpoint)


    def find_route_wrapper_by_route(self, route):
        for route_wrapper in self.routes:
            if route_wrapper.route == route:
                return route_wrapper

                
    def display_train(self, route, train):
        route_wrapper = self.find_route_wrapper_by_route(route)
        index = train.current_checkpoint
        x = route_wrapper.checkpoints[index].x
        y = route_wrapper.checkpoints[index].y
        r = 5
        color = "blue"
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=color)


    def display_trains(self):
        for route in self.sim.routes:
            for train in route.trains_on_the_go:
                self.display_train(route, train)

            
    def tick(self):
        self.sim.tick()
        self.display_all_routes_as_straight()
        self.display_trains()
        