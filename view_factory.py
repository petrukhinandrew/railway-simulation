from args_handler import ViewMode
from gui import GUI
from cli import CLI


class ViewFactory:    
    def new_view(sim, config):
        if config['mode'] == ViewMode.CONSOLE:
            return CLI(sim)
        elif config['mode'] == ViewMode.GRAPHICS:
            return GUI(sim)
        else:
            raise RuntimeError("Bad view mode given.")
