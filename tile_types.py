from typing import Tuple

import numpy as np

graphic_dt = np.dtype( #dtype creates a data type which numpy can use, behaves similar to a struct
    [
        ("ch", np.int32), #character represented in int form
        ("fg", "3B"), #foreground color represented in 3 unsigned bytes (rgb color codes)
        ("bg", "3B"), #background color represented in 3 unsigned bytes (rgb color codes)
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", np.bool), #true if can walk over tile
        ("transparent", np.bool), #true if this tile doesn't block FOV
        ("dark", graphic_dt), #Graphics for when tile is not in FOV
    ]
)


def new_tile(
    *, #enforces use of keywords, so that parameter order doesn't matter
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int,int,int], Tuple[int,int,int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255,255,255), (50,50,150)),
)

wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255,255,255), (0,0,100)),
)