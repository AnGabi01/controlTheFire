import pygame
from map_staff.GameMap import GameMap
from GUI_stuff.Board import Board
from Firefighter_stuff.Plane import Plane


# Główna pętla gry
def run():
    drawing = False
    path = []
    board = Board(GameMap())
    plane = Plane(board.fire)
    pygame.init()
    board.draw_map()
    running = True
    tik = 0
    max_tik = 5
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Lewy przycisk myszy
                    drawing = True
                    path = []  # Rozpocznij nową trasę

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Lewy przycisk myszy
                    drawing = False

            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    x, y = event.pos
                    path.append((x, y))

        #if tik == max_tik:
        board.draw_map()
        #    tik = 0
        #tik += 1
        board.fire.spread()

        if len(path) > 1:
            board.draw_plane_path(path)
        if len(path) > 0:
            plane.move(path)
        board.draw_plane(plane)

        pygame.display.flip()
        clock.tick(24)
    pygame.quit()


