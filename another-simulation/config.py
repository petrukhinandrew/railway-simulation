from enum import Enum


class RoutesType(Enum):
    STRAIGHT = 0,
    WEB = 1


class GenerationMode(Enum):
    AUTO = 0,
    MANUAL = 1


class ViewMode(Enum):
    GRAPHICS = 1,
    CONSOLE = 0


class InitConfig:
    def __init__(self, args):
        flags = self.__get_flags_from_args(args)

        self.generation_mode = self.__generation_mode(flags)
        self.view_mode = self.__view_mode(flags)
        self.routes_type = self.__routes_type(flags)

    def __get_flags_from_args(self, args):
        tokens = [token[1:] if token[0] == '-' else '' for token in args]
        return ''.join(tokens)

    def __generation_mode(self, flags):
        if 'M' in flags:
            return GenerationMode.MANUAL
        else:
            return GenerationMode.AUTO

    def __view_mode(self, flags):
        if 'G' in flags:
            return ViewMode.GRAPHICS
        else:
            return ViewMode.CONSOLE

    def __routes_type(self, flags):
        if 'W' in flags:
            return RoutesType.WEB
        else:
            return RoutesType.STRAIGHT

    def get_config(self):
        config = {}
        config['view_mode'] = self.view_mode
        config['generation_mode'] = self.generation_mode
        config['routes_type'] = self.routes_type

        return config
