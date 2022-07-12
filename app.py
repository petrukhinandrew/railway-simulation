from model.model_builder import ModelBuilder
from view.view_builder import ViewBuilder


class App:
    def __init__(self, init_config):
        self.simulation = ModelBuilder.new_simulation(init_config.get_config())
        self.view = ViewBuilder.new_view(self.simulation, init_config.get_config())

    def run(self):
        self.view.run()