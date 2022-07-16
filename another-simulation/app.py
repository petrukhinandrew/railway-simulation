import threading
from time import sleep
from enum import Enum

from config import InitConfig
from model import ModelFactory
from view import ViewFactory
from logger import Logger, LoggingLevel


class AppState(Enum):
    INITIALISING = 0,
    RUNNING = 1,
    PAUSED = 2


class App:
    def __init__(self, args):
        self.init_config = InitConfig(args).get_config()

        self.logger = Logger(LoggingLevel.DEBUG)
        self.timer = None
        self.update_freq = 30  # amount of updates per minute

        self.model = ModelFactory.new(self.init_config)
        self.view = ViewFactory.new(self.init_config)
        self.link_model_and_view()

        self.state = AppState.INITIALISING

    def start(self):
        if self.timer is None:
            self.timer = threading.Thread(target=self.update, name="model")
        else:
            raise Exception("App is already working")
        self.timer.start()
        self.view.start()
        self.state = AppState.RUNNING

    def pause(self):
        if self.state != AppState.RUNNING:
            raise Exception('App is not running')
        self.state = AppState.PAUSED

    def shutdown(self):
        if self.state == AppState.INITIALISING:
            raise Exception('App is already shutdown')

        self.timer.join()
        while (self.timer.is_alive()):
            sleep(0.1)

        self.state = AppState.INITIALISING

    def update(self):
        while True:
            if self.state == AppState.RUNNING:
                self.model.update()
                self.view.update()
                self.logger.log("Tick!")
                sleep(60 / self.update_freq)

    def link_model_and_view(self):
        self.model.view = self.view
        self.view.model = self.model
