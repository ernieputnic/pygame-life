"""
    Pygame of life module. Contains the short engine
    to simluate the grid of life.
"""

import sys
# import time

from random import randint as ri
from collections import defaultdict
from copy import deepcopy

import pygame


# from example_grids import gosper_glider
from example_grids import random_grid

from grid_defs import Grid, Neighbours

G_FPS = 10

def get_neighbours(grid: Grid, x: int, y: int) -> Neighbours:
    """
        Gets the neighbour states for a particular cell in
        (x, y) on the grid.
    """
    offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    possible_neighbours = {(x + x_add, y + y_add) for x_add, y_add in offsets}
    alive = {(pos[0], pos[1]) for pos in possible_neighbours if pos in grid.cells}
    return Neighbours(alive, possible_neighbours - alive)


def update_grid(grid: Grid) -> Grid:
    """
        Given a grid, this function returns the next iteration
        of the game of life.
    """
    new_cells = deepcopy(grid.cells)
    undead = defaultdict(int)

    for x, y in grid.cells:
        alive_neighbours, dead_neighbours = get_neighbours(grid, x, y)
        if len(alive_neighbours) not in [2, 3]:
            new_cells.remove((x, y))

        for pos in dead_neighbours:
            undead[pos] += 1

    for pos, _ in filter(lambda elem: elem[1] == 3, undead.items()):
        new_cells.add((pos[0], pos[1]))

    return Grid(grid.dim, new_cells)


def draw_grid(screen: pygame.Surface, grid: Grid) -> None:
    """
        This function draws the game of life on the given
        pygame.Surface object.
    """
    cell_width = screen.get_width() / grid.dim.width
    cell_height = screen.get_height() / grid.dim.height
    border_size = 2

    
    for (x, y) in grid.cells:
        colour = (ri(40, 255), ri(40, 255), ri(40, 255))
        # colour = (ri(20, 235), ri(20, 235), ri(20, 235))
        # colour = (180, ri(100, 255), 100)

        pygame.draw.rect(screen, colour, (x * cell_width + border_size, y * cell_height +
                                               border_size, cell_width - border_size, cell_height - border_size))
        # print(colour)




def drawFPS(screen: pygame.Surface, clock: pygame.time.Clock) -> None:
    """
    draw FPS
    """
    
    font = pygame.font.SysFont('arial', 24)
    fps = clock.get_fps()

    # Format the FPS as a string
    fps_text = f"{fps:.2f} FPS"

    # Render the FPS text
    fps_surface = font.render(fps_text, True, (255, 255, 255))

    # Get the rect of the FPS text
    fps_rect = fps_surface.get_rect()

    # Position the FPS text at the top left corner
    fps_rect.topleft = (40, 20)
    # fps_rect.topright = (10, 10)

    # Blit the FPS text on the screen
    screen.blit(fps_surface, fps_rect)

    # Update the display
    # pygame.display.flip()   





def main():
    # grid = gosper_glider
    grid = random_grid
    
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()

    while True:
        if pygame.QUIT in [e.type for e in pygame.event.get()]:
            sys.exit(0)
        
        screen.fill((0, 0, 0))
        draw_grid(screen, grid)
        grid = update_grid(grid)
        drawFPS(screen, clock)
        pygame.display.flip()
        # time.sleep(0.01)
        clock.tick(G_FPS)



if __name__ == "__main__":
    main()

