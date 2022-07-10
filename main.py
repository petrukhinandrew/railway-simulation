import sys

from model.auto_simulation import Simulation
from view.view_factory import ViewFactory
from config import Config


if __name__ == "__main__":
    config = Config(sys.argv)
    sim = AutoSimulation(config.get_config())
    app = ViewFactory.new_view(sim, config.get_config())
    app.run()
