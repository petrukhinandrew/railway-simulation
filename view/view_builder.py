from config import ViewMode
from view.gui import GUI
from view.cli import CLI


class ViewBuilder:    
    def new_view(sim, config):
        if config['view_mode'] == ViewMode.CONSOLE:
            return CLI(sim)
        elif config['view_mode'] == ViewMode.GRAPHICS:
            return GUI(sim)
        else:
            raise RuntimeError("Bad view mode given.")
