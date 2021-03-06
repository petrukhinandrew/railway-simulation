import tkinter as tk
from view.view_interface import ViewInterface


class RouteWrapper:
    def __init__(self, route):
        self.route = route
        self.checkpoints = []

        
class CheckpointWrapper:
    def __init__(self, checkpoint, x, y):
        self.checkpoint = checkpoint
        self.x = x
        self.y = y
        self.radius = 5 if self.checkpoint.is_checkpoint else 12
        self.color = "green" if self.checkpoint.is_checkpoint else "red"


class GUI(ViewInterface):
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
        self.canvas.itemconfig(self.current_route_tag, text="new route tag, look!")
        self.tick_delay = 500

        self.setup_routes()
        self.display_all_routes_as_straight()

        self.load_timetable(self.sim.routes[0], 3)
        self.display_timetable()
        
    def run(self):
        self.root.after(self.tick_delay, self.tick)
        self.root.mainloop()

    def setup_canvas(self):
        self.canvas.create_line(900, 0, 900, 720, fill="black", width=5)
        self.canvas.create_line(1070, 50, 1070, 300, fill="black", width=5)
        self.canvas.create_line(1070, 350, 1070, 600, fill="black", width=5)

        self.canvas.create_text(985, 75, font="Times 20 bold", text="Tuda")
        self.canvas.create_text(1175, 75, font="Times 20 bold", text="Suda")
        self.current_route_tag = self.canvas.create_text(1090, 25, font="Times 24 bold", text="Route Tag")
        
        self.current_route_displayign = None
        self.current_route_static_timetable_straight = []
        self.static_timetable_straight_text = self.canvas.create_text(985, 200, font="Times 15 bold", text="")
        
        self.current_route_static_timetable_reversed = []
        self.static_timetable_reversed_text = self.canvas.create_text(1175, 200, font="Times 15 bold", text="")

        self.current_route_upcoming_trains_straight = []
        # self.dynamic_timetable_straight_text = self.canvas.create_text(985, 150, font="Times 15 bold", text="") # wrong x and y

        self.current_route_upcoming_trains_reversed = []


    def load_timetable(self, route, checkpoint_index):
        self.current_route_static_timetable_straight, self.current_route_static_timetable_reversed = route.load_planned_timetable_by_index(checkpoint_index)
        self.current_route_upcoming_trains_straight, self.current_route_upcoming_trains_reversed = route.load_upcoming_trains_schedule_by_index(checkpoint_index)
        self.current_route_displayign = route


    def display_timetable(self):
        self.canvas.itemconfig(self.static_timetable_straight_text, text="\n".join(map(str, self.current_route_static_timetable_straight)))
        self.canvas.itemconfig(self.static_timetable_reversed_text, text="\n".join(map(str, self.current_route_static_timetable_reversed)))
        self.canvas.itemconfig(self.current_route_tag, text="Station: " + str(self.current_route_displayign.number))

    def setup_routes(self):
        for route in range(len(self.sim.routes)):
            self.setup_route(self.sim.routes[route], route)


    def display_straight_route(self, route, index):
        line_length = 20
        for checkpoint in range(len(route.checkpoints)):
            if checkpoint != len(route.checkpoints) - 1:
                self.canvas.create_line(100 * (index + 1), 50 + checkpoint * line_length, 100 * (index + 1), 50 + (checkpoint + 1) * line_length, fill="black", width=11)
            new_checkpoint = route.checkpoints[checkpoint]
            # self.canvas.create_oval(new_checkpoint.x - new_checkpoint.radius, new_checkpoint.y - new_checkpoint.radius, new_checkpoint.x + new_checkpoint.radius, new_checkpoint.y + new_checkpoint.radius, fill=new_checkpoint.color)
            if not route.route.checkpoints[checkpoint].is_checkpoint:
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
        color = "blue" if train.is_going_straight else "green" if not train.in_accident else "yellow"

        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=color)


    def display_trains(self):
        for route in self.sim.routes:
            for train in route.trains_on_the_go:
                self.display_train(route, train)

            
    def tick(self):
        self.sim.tick()
        self.display_all_routes_as_straight()
        self.display_trains()
        self.root.after(self.tick_delay, self.tick)