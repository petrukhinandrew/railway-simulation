from enum import Enum


class ViewMode(Enum):
    GRAPHICS = 1,
    CONSOLE = 0


class Config:
    def __init__(self, args):
        self.view_mode = ViewMode.CONSOLE
        self.__parse_args(args)

    def __parse_args(self, args):
        if "-G" in args:
            self.view_mode = ViewMode.GRAPHICS
        if "-C" in args:
            self.view_mode = ViewMode.CONSOLE
            
    def get_view_config(self):
        return {'mode': self.view_mode}

    def get_model_config(self):
        return {}