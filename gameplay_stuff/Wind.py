import random


class Wind:
    def __init__(self, range_x, range_y):
        self.range_x = range_x
        self.range_y = range_y

    def random_strength(self):
        wind_x = random.randint(self.range_x[0], self.range_x[1])
        wind_y = random.randint(self.range_y[0], self.range_y[1])
        return wind_x, wind_y
