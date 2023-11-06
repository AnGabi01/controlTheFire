import pygame.image


class Lake:
    def __init__(self):
        file_name = "lake.png"
        try:
            self.map = pygame.image.load(file_name)
            if self.map is None:
                raise Exception(print("Błąd podczas pobierania " + file_name))
        except Exception as e:
            print(f"Wystąpił błąd: {e}")




