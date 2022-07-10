from model.simulation_interface import SimulationInterface


class ManualSimulation(SimulationInterface):
    def __init__(self, config):
        raise NotImplementedError()

    def setup(self):
        pass

    def tick(self):
        pass