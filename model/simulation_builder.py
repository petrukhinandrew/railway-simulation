from model.auto_simulation import AutoSimulation
from model.manual_simulation import ManualSimulation
from config import GenerationMode

class SimulationBuilder:
    def new_simulation(config):
        if config['generation_mode'] == GenerationMode.AUTO:
            return AutoSimulation(config)
        elif config['generation_mode'] == GenerationMode.MANUAL:
            return ManualSimulation(config)
        else:
            raise NotImplementedError()
