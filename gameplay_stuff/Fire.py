from map_staff.Forest import Forest
from gameplay_stuff.Tree import Tree
from gameplay_stuff.Wind import Wind

import random


class Fire:
    def __init__(self, forest: Forest, x: int = 310, y: int = 190, windX = [1, 3], windY = [0, 1]):
        self.forest = forest
        self.width = self.forest.map.get_width()
        self.height = self.forest.map.get_height()
        self.burning_trees = []
        self.smoked_trees = []
        self.foam_trees = []
        self.set_fire(x, y)
        self.wind = Wind(windX, windY)

    def append_burning_tree(self, tree: Tree):
        self.burning_trees.append(tree)


    def set_fire(self, x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                    self.forest.trees[y+dy][x+dx].set_on_fire()
                    self.append_burning_tree(self.forest.trees[y+dy][x+dx])

    def spread(self):
        new_burning_trees = self.burning_trees.copy()
        for burning_tree in self.burning_trees:
            if burning_tree.keep_burning():  # funkcja zwraca True jesli drzewo płonie, można więc zmienić mape ognia
                wind_x, wind_y = self.wind.random_strength()
                new_burning_trees = self.spread_close_fire(burning_tree, new_burning_trees)
                if wind_x != 0 and wind_y != 0:
                    new_burning_trees = self.spread_wind_fire(burning_tree, wind_x, wind_y, new_burning_trees)
            else:
                self.smoked_trees.append(burning_tree)
                new_burning_trees.remove(burning_tree)

        self.burning_trees = new_burning_trees



    def maybe_make_fire_here(self, accident, possibility, trees_array, new_burning_trees_list):
        if accident < possibility:
            random_int = random.randint(0, len(trees_array)-1)
            trees_array[random_int].set_on_fire()
            new_burning_trees_list.append(trees_array[random_int])
        return new_burning_trees_list

    def spread_close_fire(self, tree, new_fire_map):
        neighbor_trees_on_fire = 0
        n_neighbor_trees = 0
        trees_array = []
        i = tree.position_x
        j = tree.position_y
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= i + dx < self.width and 0 <= tree.position_y + dy < self.height:
                    if self.forest.trees[dx+i][dy+j] is not None:
                        trees_array.append(self.forest.trees[dx+i][dy+j])
                        n_neighbor_trees += 1
                        if self.forest.trees[dx+i][dy+j].is_burning():
                            neighbor_trees_on_fire += 1

        # set trees on fire
        if neighbor_trees_on_fire == n_neighbor_trees:
            return new_fire_map  # skip

        accident = random.random()
        if neighbor_trees_on_fire >= 3:
            new_fire_map = self.maybe_make_fire_here(accident, 0.8, trees_array, new_fire_map)
            new_fire_map = self.maybe_make_fire_here(accident, 0.4, trees_array, new_fire_map)
        else:
            new_fire_map = self.maybe_make_fire_here(accident, 0.4, trees_array, new_fire_map)
            new_fire_map = self.maybe_make_fire_here(accident, 0.2, trees_array, new_fire_map)

        # napewno podpal jedno losowe drzewo
        new_fire_map = self.maybe_make_fire_here(accident, 10,  trees_array, new_fire_map)

        return new_fire_map

    def spread_wind_fire(self, tree, wind_x, wind_y,  new_fire_map):
        neighbor_trees_on_fire = 0
        n_neighbor_trees = 0
        trees_array = []
        i = tree.position_x
        j = tree.position_y
        for dx in [wind_x-1, wind_x, wind_x+1]:
            for dy in [wind_y-1, wind_y, wind_y+1]:
                if 0 <= i + dx < self.width and 0 <= tree.position_y + dy < self.height:
                    if self.forest.trees[dx+i][dy+j] is not None:
                        trees_array.append(self.forest.trees[dx+i][dy+j])
                        n_neighbor_trees += 1
                        if self.forest.trees[dx+i][dy+j].is_burning():
                            neighbor_trees_on_fire += 1

        # set trees on fire
        if neighbor_trees_on_fire == n_neighbor_trees:
            return new_fire_map  # skip

        #set trees on fire
        if neighbor_trees_on_fire == n_neighbor_trees:
            return new_fire_map  # skip
        accident = random.random()
        if neighbor_trees_on_fire >= 3:
            new_fire_map = self.maybe_make_fire_here(accident, 0.2, trees_array, new_fire_map)
            new_fire_map = self.maybe_make_fire_here(accident, 0.1, trees_array,  new_fire_map)
        else:
            new_fire_map = self.maybe_make_fire_here(accident, 0.1, trees_array,  new_fire_map)
            new_fire_map = self.maybe_make_fire_here(accident, 0.05, trees_array, new_fire_map)

        return new_fire_map

    def place_foam_on_tree(self, x, y):
        if 0 < x < self.width and 0 < y < self.height:
            tree = self.forest.trees[x][y]
            if isinstance(tree, Tree):
                tree.set_on_foam()
                self.foam_trees.append(tree)

    def place_foam(self, x1, y1, x2, y2, thickness):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        if dx > dy:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            for x in range(x1, x2 + 1):
                y = int(y1 + (x - x1) * (y2 - y1) / (x2 - x1))
                for i in range(-thickness // 2, thickness // 2 + 1):
                    #array[y + i, x] = black
                    self.place_foam_on_tree(x, y+i)
        else:
            if y1 > y2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            for y in range(y1, y2 + 1):
                x = int(x1 + (y - y1) * (x2 - x1) / (y2 - y1))
                for i in range(-thickness // 2, thickness // 2 + 1):
                    #array[y, x + i] = black
                    self.place_foam_on_tree(x+i, y)
