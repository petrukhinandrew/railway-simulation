import threading
from config import ViewMode
from enum import Enum


class RunningState(Enum):
    INITIALISING = 0,
    RUNNING = 1,
    PAUSED = 2,
    SHUTDOWN = 3


class ViewFactory:
    def new(config, app, model):
        if config['view_mode'] == ViewMode.GRAPHICS:
            return GraphicsView(config, app, model)
        elif config['view_mode'] == ViewMode.CONSOLE:
            return ConsoleView(config, app, model)
        else:
            raise Exception('no other view yet implemented')


class ViewInterface:
    def __init__(self, config, app, model):
        pass

    def start(self):
        pass

    def shutdown(self):
        pass

    def update(self):
        pass


class GraphicsView(ViewInterface):
    def __init__(self, config, app, model):
        super().__init__(config)


class ConsoleView(ViewInterface):
    def __init__(self, config, app, model):
        self.model = model
        self.app = app
        self.logger = self.app.logger
        self.state = RunningState.INITIALISING
        self.controller_timer = threading.Thread(target=self.__controller)

    def start(self):
        self.state = RunningState.RUNNING
        self.controller_timer.start()

    def __controller(self):
        while self.state != RunningState.SHUTDOWN:
            command = input().strip()
            self.logger.log("-> " + command)
            if command == "pause":
                self.__init_pause()
            elif command == "resume":
                self.__init_resume()
            elif command == "shutdown":
                self.__init_shutdown()
            else:
                self.__unknown_command(command)

    def __init_pause(self):
        self.app.pause()

    def __init_resume(self):
        self.app.resume()

    def __init_shutdown(self):
        self.state = RunningState.SHUTDOWN
        self.app.shutdown()

    def __unknown_command(self, command):
        # print("Unknown command: " + command)
        self.logger.log("unknown command: " + command)

    def pause(self):
        pass

    def shutdown(self):
        return super().shutdown()

    def update(self):
        pass
