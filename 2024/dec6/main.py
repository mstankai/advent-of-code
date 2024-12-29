import argparse
import numpy as np
import os
import time

from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm
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

    fresh_grid = parse_grid(text)
    grid = Grid(fresh_grid)
    guard = Guard(grid)

    x, y = guard.get_position()

    while guard.in_grid:
        if animated:
            os.system('clear')
            print('\n',guard.grid.grid)
            time.sleep(0.2)
        guard.move()

    n_pos = len(guard.visited)
    print(f"Part 1: Distinct locations visited = {n_pos}")
    
    return guard.grid.grid

# -----------------------------------------------

def simulate_obstacle_run(args):
    """
    Worker function to:
      1) Place an obstacle at (i, j).
      2) Run the Guard simulation.
      3) Return (j, i) if the guard is stuck, else None.
    """
    i, j, new_grid, completed_grid = args

    # make new grid
    nga = new_grid.copy()
    nga[i][j] = '#'
    ng = Grid(nga)

    # run guard test
    guard = Guard(ng)
    while guard.in_grid and (not guard.is_stuck):
        guard.move()            
    
    if guard.is_stuck:
        return (j,i)
    
    return None

# -----------------------------------------------
def part_2(text, completed_grid):

    fresh_grid = parse_grid(text)
    imax, jmax = fresh_grid.shape

    print('\nRunning part 2:')
    start_time = time.time()

    tasks = []
    for i in range(imax):
        for j in range(jmax):
            if (completed_grid[i][j] == 'X') and (fresh_grid[i][j] == '.'):
                tasks.append((i, j, fresh_grid, completed_grid))

    stuck_pos = set()

    with ProcessPoolExecutor() as executor:
        results = list(
            tqdm(
                executor.map(simulate_obstacle_run, tasks),
                total=len(tasks),
                desc=("Processing...")
            )
        )

        for r in results:
            if r is not None:
                stuck_pos.add(r)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Completed in {elapsed_time:.3f} seconds\n")
    print(f"Part 2: Number of obstacle positions = {len(stuck_pos)}")


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
