import argparse
import numpy as np
import os
import time

from dec6 import (
    Grid,
    Guard
)

# -----------------------------------------------
def get_input(input_path):

    with open(input_path, 'r') as f:
        text = f.read()
    
    # text = """
    # ....#.....
    # .........#
    # ..........
    # ..#.......
    # .......#..
    # ..........
    # .#..^.....
    # ........#.
    # #.........
    # ......#...
    # """

    return text

# -----------------------------------------------
def parse_grid(text):
    lines = text.strip().replace(' ','').splitlines()
    grid = [list(l) for l in lines]
    return np.array(grid)

# -----------------------------------------------
def part_1(text, animated):

    grid_arr = parse_grid(text)
    grid = Grid(grid_arr)
    guard = Guard(grid)

    x, y = guard.get_position()

    while guard.in_grid:
        if animated:
            os.system('clear')
            print('\n',guard.grid.grid)
            time.sleep(0.2)
        # print(guard.x, guard.y) 
        guard.move()

    n_pos = len(guard.visited)
    print(f"Part 1: Distinct locations visited = {n_pos}")
    
    return guard.grid

# -----------------------------------------------
import sys
def part_2(text, orig_grid):

    grid_arr = parse_grid(text)
    imax, jmax = grid_arr.shape

    print('\nRunning part 2:')
 
    stuck_pos = set()
    for i in range(imax):

        if i % 10 == 0:
            print(f'  >> Testing obs. on row {i}/{imax}...')

        for j in range(jmax):
            if orig_grid.grid[i][j] != 'X':
                continue
            if (grid_arr[i][j] != '.') :
                continue

           # make new grid
            nga = grid_arr.copy()
            nga[i][j] = '#'
            ng = Grid(nga)

            # run guard test
            guard = Guard(ng)
            while guard.in_grid and (not guard.is_stuck):
                guard.move()            
            if guard.is_stuck:
                stuck_pos.add((j,i))

    print(f"Part 2: Number of obstacle positions = {len(stuck_pos)}")

    return 

# -----------------------------------------------
def main(a):
    input_path = './dec6/input.txt'
    text = get_input(input_path)

    completed_grid = part_1(text, a)
    part_2(text, completed_grid)

# -----------------------------------------------
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-a',
        action='store_true',
        help="Enable animation."
    )
    args = parser.parse_args()

    
    main(args.a)
