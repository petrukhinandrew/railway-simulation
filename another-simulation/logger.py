from enum import Enum
import sys
import datetime


class LoggingLevel(Enum):
    INFO = 0,
    WARNING = 1,
    DEBUG = 2


class Logger:
    def __init__(self, level=LoggingLevel.DEBUG, stream=sys.stdout):
        self.level = level
        self.stream = stream
        self.setup()

    def setup(self):
        self.__log("Started logging. " + str(datetime.datetime.now()))

    def shutdown(self):
        self.__log("Ended logging. " + str(datetime.datetime.now()))

    def __log(self, msg):
        print(LoggingLevel.INFO.name, ':', msg, file=self.stream)

    def log(self, msg, level=0):
        # if level <= self.level:
        self.__log(msg)
