import sys

from simulation import Simulation
from view_factory import ViewFactory
from args_handler import Config


config = Config(sys.argv)

sim = Simulation(config.get_model_config())

app = ViewFactory.new_view(sim, config.get_view_config())

app.run()
