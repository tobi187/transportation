from typing import List

import numpy as np


def calculate(initial_state: np.ndarray) -> List[np.ndarray]:
    print(initial_state)

    def check_for_same_number(field, curr_pos):
      try:
        pass
      except IndexError:
        pass

    for row in initial_state:
        for tile in row:
            
    return []

calculate(np.random.random_sample(size=(5, 5)))

"""
At least 3 tiles should be connected
In this scenario we start with a basic rule: If there are at least 3 tiles of the same color that adjoin each other, they get removed from the board.

The calculate function takes a 5x5 2D numpy array, search for tiles of the same color (1, 2, 3) that adjoin each other and remove them.
It returns a list of board states. For now you have to calculate only one state, so the returned list has the length 1
Given the following 5x5 2D numpy array as initial_state:
[ [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0],
  [1, 0, 1, 0, 0],
  [1, 0, 1, 0, 1] ]
The result of calculate should be:
[
  [ [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1] ]
]
The tiles can have 3 different colors, marked with 1, 2, 3. The tiles are connected if they share an edge, not diagonally. Following input:
[
  [ [0, 0, 2, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 2, 2, 0, 0],
    [1, 2, 2, 3, 3],
    [3, 1, 2, 3, 2] ]
]
should result in:
[
  [ [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [3, 1, 0, 0, 2] ]
]
This should work for any color and form!
Falling down
Tiles cannot fly around. So after removing tiles other tiles have to fall down. That means, there must not be a zero under a tile!

Given the following 5x5 2D numpy array as initial_state:
[ [0, 0, 0, 0, 0],
  [0, 2, 0, 0, 0],
  [0, 2, 3, 0, 0],
  [0, 1, 1, 2, 0],
  [0, 1, 1, 1, 0] ]
The result of calculate should contain the state after removing followed by a state after falling (if differs):
[
  [ [0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0],
    [0, 2, 3, 0, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0] ],
  [ [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0],
    [0, 2, 3, 2, 0] ]
]
If there are multiple tile groups that get destroyed, all groups are removed destroyed first and then the falling starts. So given:
[
  [ [0, 0, 1, 2, 0],
    [0, 0, 2, 3, 0],
    [0, 0, 2, 3, 0],
    [0, 1, 2, 3, 0],
    [0, 1, 1, 2, 3] ]
]
should result in:
[
  [ [0, 0, 1, 2, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 2, 3], ],
  [ [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 1, 2, 3] ]
]
This should work for any color and form!
Chain reaction!
Removing and falling of tiles can result in new tile groups, which have to be removed in the next iteration.

Given the following 5x5 2D numpy array as initial_state:
[ [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 1, 2, 0, 0],
  [0, 1, 1, 2, 0],
  [0, 1, 1, 1, 2], ]
The result of calculate should now return three states - one for each iteration. The last falling state is omitted, because it not differs from the state before:
[
  [ [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 2] ],
  [ [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 2, 2, 2] ],
  [ [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0] ],
]
The number of iterations can also be higher. Here another example:
[
  [ [0, 0, 0, 0, 0],
    [0, 3, 3, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 1, 1, 2, 3],
    [3, 1, 1, 1, 2] ]
]
It will result in five states:
[
  [ [0, 0, 0, 0, 0],
    [0, 3, 3, 0, 0],
    [0, 0, 2, 3, 0],
    [0, 0, 0, 2, 0],
    [3, 0, 0, 0, 2], ],
  [ [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 3, 3, 0],
    [3, 3, 2, 2, 2] ],
  [ [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 3, 3, 0],
    [3, 3, 0, 0, 0], ],
  [ [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [3, 3, 3, 3, 0] ],
  [ [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0] ]
]
This should work for any color and form!
"""