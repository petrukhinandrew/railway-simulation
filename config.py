from enum import Enum


class GenerationMode(Enum):
    AUTO = 0,
    MANUAL = 1


class ViewMode(Enum):
    GRAPHICS = 1,
    CONSOLE = 0


class Config:
    def __init__(self, args):
        self.generation_mode = GenerationMode.AUTO
        self.view_mode = ViewMode.CONSOLE

        self.__parse_args(args)

    def __parse_args(self, args):
        flags = ''.join([token[1:] if token[0] == '-' else '' for token in args])

        self.view_mode = ViewMode.GRAPHICS if 'G' in flags else ViewMode.CONSOLE
        self.generation_mode = GenerationMode.MANUAL if 'M' in flags else GenerationMode.AUTO       

    def get_config(self):
        return {'view_mode': self.view_mode, 'generation_mode': self.generation_mode}