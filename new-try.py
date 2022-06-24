import random
    
class simulation:
    def __init__(self):
        self.station_counter = 0
        self.route_counter = 0
        self.independent_routes_amount = 0
        self.dependent_routes_amount = 0
        
        self.routes = list()
        self.generate_routes()

        self.train_velocity = 1


    def generate_routes(self):
        self.independent_routes_amount = random.randint(3, 5)
        for _ in range(self.independent_routes_amount):
            self.routes.append(route(self, False))
        self.dependent_routes_amount = random.randint(1, 3)
        for _ in range(self.dependent_routes_amount):
            self.routes.append(route(self, True))


    def init_stations_schedules(self):
        for r in self.routes:
            for s in range(1, len(r.stations)):
                r.stations[s-1].new_connection(r.stations[s], r.schedule.start_time, r.schedule.interval)
            for s in range(len(r.stations) - 1, 1, -1):
                r.stations[s-1].new_connection(r.stations[s], r.schedule.start_time, r.schedule.interval)
        

class station:
    def __init__(self, tag: int, sim):
        self.tag = tag
        self.connection = []
        self.sim = sim


    def new_connection(self, t, b,e,i):
        timetable = []
        dist = random.randint(1, 3)
        dt = 0
        while b + dist // self.sim.train_velocity +  dt * i < e:
            timetable.append(b + dist // self.sim.train_velocity + dt * i)
            dt += 1
        self.connection.append([t,timetable, dist])
        
class time_stamp:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes


    @staticmethod 
    def random_start_time_stamp():
        return time_stamp(random.choice([5,6,7], random.choice([11, 13, 19, 22, 48, 52, 35, 58])))


class schedule:
    def __init__(self, start_time, interval):
        self.start_time = start_time
        self.interval = interval
    

class route: 
    def __init__(self, sim, is_dependent):

        self.stations = list()
        self.sim = sim
        self.tag = self.sim.route_counter
        self.sim.route_counter += 1
        self.is_dependent = is_dependent
        self.schedule = schedule(time_stamp.random_start_time_stamp, random.randint(7, 20))

        if self.is_dependent:
            self.generate_dependent()
        else:
            self.generate_independent()


    def generate_independent(self):
        stations_on_route = random.randint(6, 10)
        for _ in range(stations_on_route):
            self.stations.append(station(self.sim.station_counter, self.sim))
            self.sim.station_counter += 1


    def generate_dependent(self):
        for _ in range(random.randint(1, 2)):
            self.stations.append(station(self.sim.station_counter, self.sim))
            self.sim.station_counter += 1
        for i in range(self.sim.independent_routes_amount):
            self.stations.append(random.choice(self.sim.routes[i].stations))
        for _ in range(random.randint(1, 2)):
            self.stations.append(station(self.sim.station_counter, self.sim))
            self.sim.station_counter += 1


    def display_route(self):
        print(self.tag, end=" ")

        if self.is_dependent:
            print(">> ", end="")
        else:
            print("vv ", end="")
            
        for st in self.stations:
            print(st.tag, end=" ")
        print()

s = simulation()

        
for r in s.routes:
    r.display_route()
