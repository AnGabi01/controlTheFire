import random
import GUI_stuff.Colors as Color

GREEN = 1
SMOKED = 0
BURNING = -1
FOAM = 2


class Tree:
    def __init__(self, position_x, position_y):
        self.__status = GREEN
        self.position_x = position_x
        self.position_y = position_y
        self.__burning_time = random.randint(10, 20)
        self.__burning_time_left = self.__burning_time

    def burning_time_left(self):
        return self.__burning_time_left

    def set_on_fire(self):
        if self.__status == GREEN:
            self.__status = BURNING

    def set_on_foam(self):
        self.__status = FOAM

    def keep_burning(self):
        if not self.__status == BURNING:
            return False
        else:
            self.__burning_time_left -= 1
            if self.__burning_time_left <= 0:
                self.__status = SMOKED
            return True

    def color(self):
        if self.__status == BURNING:
            return Color.BURNING_TREE
        if self.__status == GREEN:
            return Color.GREEN_TREE
        if self.__status == SMOKED:
            return Color.DUST
        if self.__status == FOAM:
            return Color.FOAM

    def is_burning(self):
        if self.__status == BURNING:
            return True
        return False

    def is_green(self):
        if self.__status == GREEN:
            return True
        return False

    def is_foam(self):
        if self.__status == FOAM:
            return True
        return False

