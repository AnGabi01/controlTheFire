from map_staff.Road import Road
from map_staff.Lake import Lake
# from map_staff.Humidity import Humidity
from map_staff.Forest import Forest


class GameMap:
    def __init__(self):
        self.road = Road()
        self.lake = Lake()
        self.forest = Forest()
        self.width, self.height = self.road.map.get_width(), self.road.map.get_height()

