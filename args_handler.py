from enum import Enum


class ViewMode(Enum):
    GRAPHICS = 1,
    CONSOLE = 0


class Config:
    def __init__(self, args):
        self.view_mode = ViewMode.CONSOLE
        self.parse_args(args)

    def parse_args(self, args):
        print(args)

    def get_view_config(self):
        return {'mode': self.view_mode}

    def get_model_config(self):
        return {}
    