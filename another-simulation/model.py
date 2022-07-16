from config import GenerationMode


class ModelFactory:
    def new(config):
        if config['generation_mode'] == GenerationMode.AUTO:
            return AutoGeneratedModel(config)
        elif config['generation_mode'] == GenerationMode.MANUAL:
            return ManuallyGeneratedModel(config)
        else:
            raise Exception("no other generation type yet implemented")


class ModelInterface:
    def __init__(self, config):
        self.view = None

    def start(self):
        pass

    def shutdown(self):
        pass

    def update(self):
        pass


class AutoGeneratedModel (ModelInterface):
    def __init__(self, config):
        super().__init__(config)


class ManuallyGeneratedModel(ModelInterface):
    def __init__(self, config):
        super().__init__(config)
