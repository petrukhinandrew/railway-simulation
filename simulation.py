from queue import Queue
from random import randint
import stat

from station import Station
from route import Route


class SimulationUI:
    @staticmethod
    def print_stations(stations: list) -> None:
        for station in stations:
            print(str(station.id) + " -> ", end="")
            for adjacent_station in station.adjacent_stations:
                print(adjacent_station.id, end=" ")
            print()
        print()

    @staticmethod
    def print_distances(distances: list) -> None:
        for station_from in range(len(distances)):
            for station_to in range(len(distances)):
                print(distances[station_from][station_to], end=" ")
            print()
        print()

    @staticmethod
    def print_routes(routes: list) -> None:
        for route in routes:
            print(route.id, end=" : ")
            for station in route.stations:
                print(station.id, end=" ")
            print()
        print()

    @staticmethod
    def print_routes_with_distances(routes: list, distances: list) -> None:
        for route in routes:
            previous_station = None
            for station in route.stations:
                if previous_station != None:
                    print(
                        "-- " + str(distances[previous_station.id][station.id]) + " --> ", end="")
                print("_", end="")
                print(station.id, end="_ ")
                previous_station = station
            print()
        print()


class Simulation:
    def __init__(self) -> None:
        self.stations = self.generate_stations()
        self.distances = self.generate_distances(self.stations)
        self.routes = [Route(target.id, self.stations, target) for target in filter(
            lambda station: len(station.adjacent_stations) == 1, self.stations[1:])]
        SimulationUI.print_stations(self.stations)
        SimulationUI.print_distances(self.distances)
        SimulationUI.print_routes(self.routes)
        SimulationUI.print_routes_with_distances(self.routes, self.distances)

    @staticmethod
    def generate_stations() -> list:  # building bfs-tree
        stations = []
        number_of_stations_generated = 0
        generating = True
        stations_queue = Queue()

        root = Station(number_of_stations_generated)
        stations.append(root)
        number_of_stations_generated += 1
        stations_queue.put(root)

        while number_of_stations_generated < 21 and generating:
            current_station = stations_queue.get()
            for i in range(randint(1, 3)):
                new_station = Station(number_of_stations_generated)
                new_station.adjacent_stations.append(current_station)
                number_of_stations_generated += 1

                current_station.adjacent_stations.append(new_station)
                stations.append(new_station)
                stations_queue.put(new_station)
            if number_of_stations_generated > 10 and randint(0, 10) > 7:
                generating = False
        return stations

    @staticmethod
    def generate_distances(stations: list) -> list:
        def dfs(s: Station, dist: list) -> None:
            for unvisited_station in s.adjacent_stations[1:]:
                new_dist = randint(1, 5)
                dist[s.id][unvisited_station.id] = new_dist
                dist[unvisited_station.id][s.id] = new_dist
                dfs(unvisited_station, dist)

        distances = [[0 for _ in range(len(stations))]
                     for _ in range(len(stations))]

        root = stations[0]
        for unvisited_station in root.adjacent_stations:
            new_dist = randint(1, 5)
            distances[root.id][unvisited_station.id] = new_dist
            distances[unvisited_station.id][root.id] = new_dist
            dfs(unvisited_station, distances)

        return distances

    @staticmethod
    def init_schedules(routes: list, distances: list):
        pass


sim = Simulation()
