import sys
from config import InitConfig
from app import App

if __name__ == "__main__":
    init_config = InitConfig(sys.argv)
    app = App(init_config)
    app.run()
