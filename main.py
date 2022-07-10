import sys

from model.simulation_builder import SimulationBuilder
from view.view_builder import ViewBuilder
from config import Config


if __name__ == "__main__":
    config = Config(sys.argv)
    sim = SimulationBuilder.new_simulation(config.get_config())
    app = ViewBuilder.new_view(sim, config.get_config())
    app.run()
