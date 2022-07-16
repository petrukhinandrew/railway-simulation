import threading
from config import ViewMode


class ViewFactory:
    def new(config):
        if config['view_mode'] == ViewMode.GRAPHICS:
            return GraphicsView(config)
        elif config['view_mode'] == ViewMode.CONSOLE:
            return ConsoleView(config)
        else:
            raise Exception('no other view yet implemented')


class ViewInterface:
    def __init__(self, config):
        pass

    def start(self):
        pass

    def shutdown(self):
        pass

    def update(self):
        pass


class GraphicsView(ViewInterface):
    def __init__(self, config):
        super().__init__(config)


class ConsoleView(ViewInterface):
    def __init__(self, config):
        self.model = None
        self.controller_timer = None

    def start(self):
        self.controller_timer = threading.Thread(target=self.__controller)
        self.controller_timer.start()

    def __controller(self):
        while True:
            command = input()
            print(command)

    def shutdown(self):
        return super().shutdown()

    def update(self):
        pass
