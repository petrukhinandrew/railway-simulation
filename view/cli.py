from view.view_interface import ViewInterface


class CLI(ViewInterface):
    def __init__(self, sim):
        self.sim = sim

    def run(self):
        print("RUNNING!")