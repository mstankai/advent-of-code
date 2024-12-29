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

        moved = False
        while not moved:
            
            dx, dy = self.get_move()
            nx, ny = self.x + dx, self.y + dy
 
            if (nx,ny) in self.grid.obstacles:
                self.turn()
                continue

            self.grid.update_guard(nx, ny, self.dir)

            if not self.grid.in_grid(nx, ny):
                self.in_grid = False
                return

            self.x, self.y = nx, ny
            self.n_moves += 1
            
            self.log_visited()
            self.log_move()

            is_stuck = (
                ( (self.x, self.y, self.dir) in self.moves )
                and ( self.moves[(self.x, self.y, self.dir)] > 1 )
            )

            if is_stuck:
                self.is_stuck = True

            moved = True

    def set_dir(self, new_dir):
        ok_dirs = self.move_map.keys()
        if new_dir not in ok_dirs:
            self.dir = new_dir
        else:
            raise ValueError(f"Invalid direction: {new_dir}, must be one of {ok_dirs}")

    def turn(self):
        turns = {
            'N': 'E',
            'E': 'S',
            'S': 'W',
            'W': 'N'
        }
        self.dir = turns[self.dir]
        return
    