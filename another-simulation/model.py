from enum import Enum
import random
from config import RoutesType


class CheckpointType(Enum):
    SECONDARY = 0,
    PRIMARY = 1


class ModelBuilder:
    def new(config):
        model = Model()
        model.routes = RoutesGenerator.generate(config["routes_type"])
        return model


class Model:
    def __init__(self):
        self.routes = []

    def start(self):
        pass

    def update(self):
        pass

    def shutdown(self):
        pass


class Route:
    def __init__(self) -> None:
        self.checkpoints = []
        self.trains = []

    # insert checkpoint before index to self.checkpoints
    def insert_primary_checkpoint(self, index):
        self.checkpoints.append(index, Checkpoint(CheckpointType.PRIMARY))

    def insert_secondary_checkpoint(self, index):
        self.checkpoints.insert(index, Checkpoint(CheckpointType.SECONDARY))

    def insertn_secondary_checkpoints(self, index, n):
        for _ in range(n):
            self.insert_secondary_checkpoint(index)


class Checkpoint:
    def __init__(self, type):
        self.type = type


class RoutesGenerator:
    def generate(self, type):
        self.number_of_routes = random.randint(4, 7)
        self.routes = []

        if type == RoutesType.WEB:
            self.__web_gen()
        elif type == RoutesType.STRAIGHT:
            self.__straight_gen()
        else:
            raise Exception("Unknown routes type")

        return self.routes

    def __web_gen(self):
        raise Exception("Not yet implemented")

    def __straight_gen(self):
        for _ in range(self.number_of_routes):
            cur_route = Route()
            cur_route_number_of_stations = random.randint(4, 7)

            for _ in range(1, cur_route_number_of_stations):
                cur_route.insert_primary_checkpoint(0)
                gap_size = random.randint(2, 4)
                cur_route.insertn_secondary_checkpoints(0, gap_size)
            cur_route.insert_primary_checkpoint(0)

            self.routes.append(cur_route)
