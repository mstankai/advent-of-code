import re
import sys
import numpy as np

def get_input(input_path: str):

    with open(input_path, 'r') as f:
        text = f.read()
    # text = """
    # ............
    # ........0...
    # .....0......
    # .......0....
    # ....0.......
    # ......A.....
    # ............
    # ............
    # ........A...
    # .........A..
    # ............
    # ............
    # """
    
    return text

# -----------------------------------------------
def parse_grid(text: str):
    lines = text.strip().replace(' ','').splitlines()
    grid = [list(l) for l in lines]
    return np.array(grid)

# -----------------------------------------------
def get_antennas(grid: np.array):
    unique_symbols = np.unique(grid)
    antennas = {}
    for s in unique_symbols:
        if s == '.' : continue       
        antennas[str(s)] = np.transpose(np.where(grid == s))
    return antennas

# -----------------------------------------------
def plot_nodes(antinodes: set, grid: np.array): # for debug
    antinode_array = np.array([(int(x), int(y)) for x, y in antinodes])
    n_rows, n_cols = antinode_array[:, 0], antinode_array[:, 1]
    example = grid.copy()
    example[n_rows, n_cols] = '#'
    print(example)

# -----------------------------------------------
def part_1(grid: np.array, antennas: dict):
    r_max, c_max = grid.shape

    all_antinodes = set()
    for a_name, coords in antennas.items():
        n_antennas = len(coords)

        for i in range(n_antennas):
            for j in range(i+1, n_antennas, 1):
                c1, c2 = coords[i], coords[j]
                u = c2 - c1
                nodes = [c1 - u, c2 + u]

                for n in nodes:
                    if (0 <= n[0] < r_max) and (0 <= n[1] < c_max):
                        all_antinodes.add(tuple(n))

    print(f"Part 1: number of unique antinodes = {len(all_antinodes)}")

# -----------------------------------------------
def part_2(grid: np.array, antennas: dict):
    r_max, c_max = grid.shape

    all_antinodes = set()
    for a_name, coords in antennas.items():
        n_antennas = len(coords)

        for i in range(n_antennas):
            for j in range(i+1, n_antennas, 1):
                c1, c2 = coords[i], coords[j]
                u = c2 - c1

                in_grid = True
                plus = True
                n = c1

                while in_grid:
                    if (0 <= n[0] < r_max) and (0 <= n[1] < c_max):
                        in_grid = True
                        all_antinodes.add(tuple(n))
                    elif plus: # look at negative direction
                        in_grid = True
                        plus = False
                        n = c1
                    else: 
                        in_grid = False
                    
                    # get next node
                    if plus:
                        n = n + u
                    else:
                        n = n - u

    print(f"Part 2: number of unique antinodes = {len(all_antinodes)}")


# -----------------------------------------------
def main():
    input_path = './dec8/input.txt'
    text = get_input(input_path)
    grid = parse_grid(text)
    antennas = get_antennas(grid)
    part_1(grid, antennas)
    part_2(grid, antennas)

# -----------------------------------------------
if __name__ == "__main__":
    main()
