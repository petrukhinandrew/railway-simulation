import sys
from config import InitConfig
from app import App

if __name__ == "__main__":
    app = App(sys.argv)
    app.run()
