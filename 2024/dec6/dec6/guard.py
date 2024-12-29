from .grid import Grid

class Guard:
    def __init__(self, grid_obj):
        """
        Initialize a guard at a certain position on the grid.
        Allways initialized heading North.

        Args:
            grid (Grid): starting grid of the guard
        """
        self.grid = grid_obj

        x, y = self.grid.guard

        self.x = x
        self.y = y
        self.dir = 'N'

        self.visited = [(x,y)]
        self.moves = {(x,y,self.dir): 1}

        self.move_map = {
            'N': (0, -1),
            'S': (0, 1),
            'E': (1, 0),
            'W': (-1, 0)
        }

        self.n_moves = 0

        self.in_grid = True
        self.is_stuck = False


    def get_move(self):
        return self.move_map[self.dir]
    
    def get_position(self):
        return self.x, self.y

    def log_move(self):
        k = (self.x, self.y, self.dir) 
        if k not in self.moves.keys():
            self.moves[k] = 1
        else:
            self.moves[k] += 1

    def log_visited(self):
        if (self.x, self.y) not in self.visited:
            self.visited.append((self.x, self.y))

    def move(self):
        if (not self.in_grid):
            print("Guard.move(): guard not on grid, no more moves.")
            return
        if self.is_stuck:
            print("Guard.move(): guard is stuck, no more moves.")
            return

        dx, dy = self.get_move()
        x = self.x + dx
        y = self.y + dy
 
        if (x,y) in self.grid.obstacles:
            # print('Turning!: x,y = ',x,y)
            self.turn()
            self.move()
            return

        self.x = x
        self.y = y
        self.n_moves += 1

        self.grid.update_guard(x,y,self.dir)

        self.set_in_grid()
        if not self.in_grid:
            return         
        
        self.log_visited()
        self.log_move()

        self.set_is_stuck()


    def set_dir(self, new_dir):
        ok_dirs = self.move_map.keys()
        if new_dir not in ok_dirs:
            self.dir = new_dir
        else:
            raise ValueError(f"Invalid direction: {new_dir}, must be one of {ok_dirs}")

    def set_in_grid(self):
        self.in_grid = self.grid.in_grid(self.x, self.y)

    def set_is_stuck(self):
        if not self.in_grid: 
            self.is_stuck = False
        k =  (self.x, self.y, self.dir)
        v = self.moves[k]
        self.is_stuck = (v > 1)

    def turn(self):
        turns = {
            'N': 'E',
            'E': 'S',
            'S': 'W',
            'W': 'N'
        }
        self.dir = turns[self.dir]
        return
    
    




    
