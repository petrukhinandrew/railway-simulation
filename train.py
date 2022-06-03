# has route
# accidents happens to the train even if they are happened with the road

from route import Route


class Train:
    def __init__(self, id: int, route: Route) -> None:
        self.accident = None
        self.id = id
        self.route = route
