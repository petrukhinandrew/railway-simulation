from config import InitConfig
from model.model_builder import ModelBuilder
from view.view_builder import ViewBuilder


class App:
    def __init__(self, args):
        self.init_config = InitConfig(args)
        self.simulation = ModelBuilder.new_simulation(self.init_config.get_config())
        self.view = ViewBuilder.new_view(self.simulation, self.init_config.get_config())

    def run(self):
        self.view.run()