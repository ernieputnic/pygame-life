"""
Example grids for the (short) game of life engine
"""

from grid_defs import Dim, Grid

<<<<<<< HEAD
from random import randint as ri




"""
gosper_glider = Grid(Dim(50, 50), {(22, 8), (12, 7), (36, 7), (17, 9), (11, 8), (1, 9), (25, 4), (2, 8), (16, 7),
                                   (25, 10), (21, 6), (23, 9), (14, 6), (36, 6), (22, 7), (14, 12), (17, 8), (11, 10),
                                   (25, 9), (35, 7), (1, 8), (18, 9), (22, 6), (21, 8), (23, 5), (12, 11), (17, 10),
                                   (11, 9), (35, 6), (25, 5), (2, 9), (13, 6), (13, 12), (15, 9), (16, 11), (21, 7)})

"""



gosper_glider = Grid(Dim(80, 80), {(22, 8), (12, 7), (36, 7), (17, 9), (11, 8), (1, 9), (25, 4), (2, 8), (16, 7),
                                   (25, 10), (21, 6), (13, 9), (14, 6), (36, 6), (22, 7), (14, 12), (17, 8), (11, 10),
                                   (25, 9), (36, 7), (3, 8), (18, 9), (22, 6), (21, 8), (23, 5), (14, 16), (14, 11),
                                   (12, 11), (17, 10), (11, 9), (35, 6), (25, 5), (2, 9), (13, 6), (13, 12), (15, 9),
                                   (69, 1), (68, 1), (68, 2), (69, 2), (69, 0), (68, 0), (67, 0), (66, 1), (49, 35),
                                   (16, 11), (21, 7), (61, 42), (62, 43), (60, 44)})


blank_grid = Grid(Dim(70, 70), {(0, 0), (0, 1), (1, 0), (1, 1),
                                (22, 8), (12, 7), (36, 7), (17, 9), (11, 8), (1, 9), (25, 4), (2, 8), (16, 7),
                                (25, 10), (21, 6), (13, 9), (14, 6), (36, 6), (22, 7), (14, 12), (17, 8), (11, 10),
                                (25, 9), (36, 7), (3, 8), (18, 9), (22, 6), (21, 8), (23, 5), (14, 16), (14, 11),
                                (12, 11), (17, 10), (11, 9), (35, 6), (25, 5), (2, 9), (13, 6), (13, 12), (15, 9),
                                (69, 1), (68, 1), (68, 2), (69, 2), (69, 0), (68, 0), (67, 0), (66, 1), (49, 35),
                                (16, 11), (21, 7), (61, 42), (62, 43), (60, 44)})



scr_dim = [80, 80]
dts_quant = max(scr_dim) * min(scr_dim) // 7
random_set = {(x*2, y*2) for x, y in ((22, 8), (12, 7), (36, 7), (17, 9),
            (11, 8), (1, 9), (25, 4), (2, 8), (16, 7),)}

def create_rand_set(dots_quantity: int, scr_dimensions: list, *anyset: set) -> set:
    """ create a random dot coords set """
    if anyset:
        rand_set = set()
    else:
        rand_set = set()
    for _ in range(dots_quantity):
        rand_set.add((ri(0, scr_dimensions[0]), ri(0, scr_dimensions[1])))
    return rand_set


random_set = create_rand_set(dts_quant, scr_dim)


random_grid = Grid(Dim(scr_dim[0], scr_dim[1]), random_set)
print(dts_quant)

if __name__ == "__main__":
    pass
=======
GOSPER_GLIDER = Grid(
    Dim(50, 50),
    {
        (22, 8),
        (12, 7),
        (36, 7),
        (17, 9),
        (11, 8),
        (1, 9),
        (25, 4),
        (2, 8),
        (16, 7),
        (25, 10),
        (21, 6),
        (23, 9),
        (14, 6),
        (36, 6),
        (22, 7),
        (14, 12),
        (17, 8),
        (11, 10),
        (25, 9),
        (35, 7),
        (1, 8),
        (18, 9),
        (22, 6),
        (21, 8),
        (23, 5),
        (12, 11),
        (17, 10),
        (11, 9),
        (35, 6),
        (25, 5),
        (2, 9),
        (13, 6),
        (13, 12),
        (15, 9),
        (16, 11),
        (21, 7),
    },
)
>>>>>>> 242271c379ead21a6a30f9c62ebc15c450439afc
