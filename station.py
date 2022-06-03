class Station():
    def __init__(self, id: int, is_central: bool = False, is_remote: bool = False) -> None:
        self.id: int = id
        self.adjacent_stations: list = list()
        self.is_central: bool = is_central
        self.is_remote: bool = is_remote

    def is_central() -> bool:
        return self.is_central

    def is_remote() -> bool:
        return self.is_remote
