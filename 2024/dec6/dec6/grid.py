import numpy as np

class Grid:
    def __init__(self, grid_arr: np.array):
        self.grid = grid_arr
        self.xmax = self.grid.shape[1]
        self.ymax = self.grid.shape[0]

        self.guard = None
        self.obstacles = set()

        for y, row in enumerate(self.grid):
            for x, item in enumerate(row):
                if item == '^':
                    self.guard = (x,y)
                if  item == '#':
                    self.obstacles.add((x,y))

        # print(self.obstacles)
    

    def in_grid(self, x: int, y: int):
        x_ok = (0 <= x < self.xmax)
        y_ok = (0 <= y < self.ymax)
        if x_ok and y_ok:
            return True
        return False
    
    def update_guard(self, x, y, gdir):
        ix, iy = self.guard
        
        if (ix, iy) != (x, y):
            self.grid[iy][ix] = 'X'
            self.guard = (x, y)
        
        leg = {
            'N' : '^',
            'E' : '>',
            'W' : '<',
            'S' : 'v'
        }
        self.grid[y][x] = leg[gdir]
                
    
        
