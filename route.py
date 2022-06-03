from queue import Queue
from random import randint

from station import Station


class Route:
    def __init__(self, id: int, stations: list, target: Station) -> None:
        self.id = id
        self.stations = self.generate_route(stations, target)
        self.schedule = list()

    @staticmethod
    def generate_route(stations: list, target: Station) -> list:
        route = list()
        current_station = target
        route.append(current_station)
        while current_station != stations[0]:
            current_station = current_station.adjacent_stations[0]
            route.append(current_station)
        return route
        
    
