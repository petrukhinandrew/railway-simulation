import sys

from model.simulation import Simulation
from view.view_factory import ViewFactory
from config import Config


if __name__ == "__main__":
    config = Config(sys.argv)
    sim = Simulation(config.get_model_config())
    app = ViewFactory.new_view(sim, config.get_view_config())
    app.run()
