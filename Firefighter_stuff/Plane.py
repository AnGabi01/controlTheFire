import pygame
import math
from gameplay_stuff.Fire import Fire


class Plane:
    def __init__(self, fire: Fire):
        self.fire = fire
        self.speed = 8
        self.destination_x = 400
        self.destination_y = 200
        self.position_x = 300
        self.position_y = 100
        self.angle = 0
        self.set_destination(400, 200)
        try:
            self.picture = pygame.image.load("plane.png")
            if self.picture is None:
                raise Exception(print("Błąd podczas pobierania plane.png"))
        except Exception as e:
            print(f"Wystąpił błąd: {e}")


    def return_picture(self):
        return pygame.transform.rotate(self.picture, self.angle)

    def set_destination(self, x, y):
        self.destination_x = x
        self.destination_y = y
        angle = math.degrees(math.atan2(self.destination_x - self.position_x, self.destination_y - self.position_y))
        if angle < 0:
            angle += 360
        self.angle = angle

    def move(self, path):
        self.set_destination(path[0][0], path[0][1])
        dx, dy = self.destination_x - self.position_x, self.destination_y - self.position_y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance > self.speed:
            direction_x, direction_y = dx / distance, dy / distance
            self.position_x += direction_x * self.speed
            self.position_y += direction_y * self.speed
        else:
            if len(path) > 1:
                self.fire.place_foam(x1=path[0][0], x2=path[1][0], y1=path[0][1], y2=path[1][1], thickness=5)
            path.pop(0)



