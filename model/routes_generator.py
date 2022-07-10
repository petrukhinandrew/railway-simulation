from model.route import Route
from config import GenerationMode, RoutesType

class RoutesGenerator:
    def __init__(self):
        pass
    
    def new_routes(config):
        if config['routes_type'] == RoutesType.STRAIGHT:
            return RoutesGenerator.__straight_routes_mode()
        if config['routes_type'] == RoutesType.WEB:
            return RoutesGenerator.__web_routes_mode()

    def __straight_routes_mode(self):
        pass

    def __web_routes_mode(self):
        pass