from config import ViewMode
from view.gui import GUI
from view.cli import CLI


class ViewFactory:    
    def new_view(sim, config):
        if config['mode'] == ViewMode.CONSOLE:
            return CLI(sim)
        elif config['mode'] == ViewMode.GRAPHICS:
            return GUI(sim)
        else:
            raise RuntimeError("Bad view mode given.")
