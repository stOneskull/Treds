from world import World
from map import Map


class God:
    def __init__(self):
        self.eye = 0
        self.world = World()
        self.cards = {}

    def make_menu(self):
        pass

    def make_card(self):
        pass

    def make_map(self):
        self.map = Map(self.world.rooms)
        self.map.window.mainloop()