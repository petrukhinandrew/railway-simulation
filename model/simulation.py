import random
from model.route import Route
from model.accident import Accident


class Simulation:
    def __init__(self, config):
        self.routes = []
        self.current_tick = -1
        self.config = config
        self.setup_routes()

    def init_check(self):
        self.display_routes()
        random_route = random.choice(self.routes)
        random_checkpoint = random.randint(0, len(random_route.checkpoints) - 1)
        random_route.display_timetable_by_index(random_checkpoint)

    def setup_routes(self):
        number_of_routes = random.randint(4, 7)
        for route_number in range(number_of_routes):
            self.routes.append(Route(route_number))

    def display_routes(self):
        for route_index in range(len(self.routes)):
            print("Route: " + str(route_index))
            self.routes[route_index].display_stations()

    def tick(self):
        self.current_tick += 1
        for route in self.routes:
            route.tick(self.current_tick)
        accident_chance = random.randint(1, 20)
        if accident_chance > 15:
            train_found = False
            while not train_found:
                route = random.choice(self.routes)
                train = random.choice(route.trains_on_the_go)
                if not train.in_accident:
                    train_found = True
                    train.in_accident = True
                    train.accident = Accident(random.randint(1, 4))