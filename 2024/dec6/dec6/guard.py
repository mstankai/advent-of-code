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
        self.in_grid = True
        self.is_stuck = False

        self.visited = set()
        self.visited.add((x,y,self.dir))

        self.moves = {
            'N': (0, -1),
            'S': (0, 1),
            'E': (1, 0),
            'W': (-1, 0)
        }


    def get_move(self):
        return self.moves[self.dir]

    def turn(self):
        turns = {
            'N': 'E',
            'E': 'S',
            'S': 'W',
            'W': 'N'
        }
        self.dir = turns[self.dir]
        return

    def move(self):
        dx, dy = self.get_move()

        x = self.x + dx
        y = self.y + dy

        if (x,y) in self.grid.obstacles:
            # print('Turning!: x,y = ',x,y)
            self.turn()
            self.move()
            return

        if not self.grid.in_grid(x, y):
            self.in_grid = False   
            return         

        if (x, y, self.dir) in self.visited:
            self.is_stuck = True
            return
        
        self.x = x
        self.y = y

        self.visited.add((x,y, self.dir))
        self.grid.update_guard(x,y,self.dir)

    
    def set_dir(self, new_dir):
        ok_dirs = self.moves.keys()
        if new_dir not in ok_dirs:
            self.dir = new_dir
        else:
            raise ValueError(f"Invalid direction: {new_dir}, must be one of {ok_dirs}")
        
    def get_position(self):
        return self.x, self.y

    def get_visited(self):
        return { (t[0],t[1]) for t in self.visited}
        