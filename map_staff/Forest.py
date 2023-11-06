from gameplay_stuff.Tree import Tree
import pygame.image

class Forest():
    def __init__(self):
        file_name = "forest.png"
        try:
            self.map = pygame.image.load(file_name)
            if self.map is None:
                raise Exception(print("Błąd podczas pobierania " + file_name))
        except Exception as e:
            print(f"Wystąpił błąd: {e}")

        #a Teraz Drzewka
        self.trees = []
        for i in range(self.map.get_width()):
            self.trees.append([])
            for j in range(self.map.get_height()):
                if self.map.get_at((i, j)).a == 0:
                    self.trees[i].append(None)
                else:
                    self.trees[i].append(Tree(i, j))

        self.burning_trees = []



