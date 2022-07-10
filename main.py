import sys

import simulation
import view_interface
import args_handler

config = args_handler.Config(sys.argv)

sim = simulation.Simulation(config.get_model_config())

app = view_interface.ViewFactory(config.get_view_config())

app.run()
