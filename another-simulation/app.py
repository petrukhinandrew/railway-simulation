import threading
from time import sleep
from enum import Enum

from config import InitConfig
from model import ModelBuilder
from view import ViewFactory
from logger import Logger, LoggingLevel


class AppState(Enum):
    INITIALISING = 0,
    RUNNING = 1,
    PAUSED = 2,
    SHUTDOWN = 3


class App:
    def __init__(self, args):
        self.logger = Logger(LoggingLevel.DEBUG)
        self.logger.log("Logger set up. Initialising app")

        self.state = AppState.INITIALISING
        self.init_config = InitConfig(args).get_config()
        self.logger.log("Config read correctly.")

        self.timer = threading.Thread(target=self.update, name="model")
        self.update_freq = 20  # amount of updates per minute

        self.model = ModelBuilder.new(self.init_config)
        self.logger.log("Model set up.")

        self.view = ViewFactory.new(self.init_config, self, self.model)
        self.logger.log("View set up.")

    def start(self):
        self.state = AppState.RUNNING
        self.logger.log("Starting app. Mode switched to RUNNING")

        self.timer.start()
        self.view.start()

    def resume(self):
        self.state = AppState.RUNNING

        self.model.resume()

        self.logger.log("Mode switched to RUNNING")

    def pause(self):
        if self.state != AppState.RUNNING:
            raise Exception('App is not running')

        self.state = AppState.PAUSED

        self.logger.log("Mode switched to PAUSED")

    def shutdown(self):
        self.state = AppState.SHUTDOWN
        self.logger.log("Mode switched to SHUTDOWN")

        self.model.shutdown()
        self.logger.log("Model shutdown")

        self.logger.log("Exiting app.")

    def update(self):
        while self.state != AppState.SHUTDOWN:
            if self.state == AppState.RUNNING:
                self.model.update()
                self.view.update()
                sleep(60 / self.update_freq)
