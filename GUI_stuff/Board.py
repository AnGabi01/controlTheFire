import pygame
from map_staff.GameMap import GameMap
from gameplay_stuff.Fire import Fire
from Firefighter_stuff.Plane import Plane
import GUI_stuff.Colors as Colors


HUMIDITY_VIEW = "humidity"
SIMULATION_VIEW = "simulation"


class Board:
    def __init__(self, game_map: GameMap):
        self.game_map = game_map
        self.fire = Fire(self.game_map.forest)
        self.pixel_size = 1
        self.ps = self.pixel_size
        window_name = "Fire simulator"
        pygame.display.set_caption(window_name)
        self.screen = pygame.display.set_mode((self.game_map.width * self.ps, self.game_map.height * self.ps))

    def draw_map(self):
        fire_pixel = pygame.image.load("fire_pixel.png")
        dust_pixel = pygame.image.load("dust_pixel.png")
        road = self.game_map.road.map
        self.screen.blit(road, (0, 0))
        lake = self.game_map.lake.map
        self.screen.blit(lake, (0, 0))
        forest = self.game_map.forest.map
        self.screen.blit(forest, (0, 0))
        for tree in self.fire.burning_trees:
            self.screen.blit(fire_pixel, (tree.position_x, tree.position_y))
        for tree in self.fire.foam_trees:
            self.screen.blit(fire_pixel, (tree.position_x, tree.position_y))
            pygame.draw.rect(self.screen, tree.color(), (tree.position_x, tree.position_y, 1, 1))
        # for tree in self.fire.smoked_trees:
        #     self.screen.blit(dust_pixel, (tree.position_x, tree.position_y))

    def draw_plane(self, plane: Plane):
        # Utwórz powierzchnię pygame na podstawie obrazu
        image = plane.return_picture()
        image = pygame.transform.scale(image, (image.get_width()*self.ps, image.get_height()*self.ps))
        self.screen.blit(image, (plane.position_x*self.ps, plane.position_y*self.ps))
        pygame.display.flip()

    def draw_plane_path(self, path):
        pygame.draw.lines(self.screen, Colors.PATH , False, path, 2)