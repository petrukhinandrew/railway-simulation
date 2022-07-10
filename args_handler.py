from enum import Enum


class ViewMode(Enum):
    GRAPHICS = 1,
    CONSOLE = 0


class Config:
    def __init__(self, args):
        self.view_mode = ViewMode.CONSOLE
        print(args)
        
    def get_view_config(self):
        pass

    def get_model_config(self):
        pass
    