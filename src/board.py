
class Board:
    """
    Board class that represents the game board in Conway's Game of Life
    """

    def __init__(self, board_size: tuple[int, int], cell_size: int):
        self.__board_size = board_size
        self.__cell_size = cell_size
        self.__cells = self.empty_cells()

    def toggle_cell(self, x: int, y: int):
        self.__cells[x][y] = 1 - self.__cells[x][y] # toggle cell state

    def reset(self):
        self.__cells = self.empty_cells()

    def next_generation(self):
        new_cells = self.empty_cells()
        # compute each cell's next state in the next state of the board
        for x in range(self.__board_size[0]):
            for y in range(self.__board_size[1]):
                new_cells[x][y] = self._next_cell_state(x, y)
        self.__cells = new_cells

    def _next_cell_state(self, x: int, y: int) -> int:
        alive_neighbours = self._count_alive_neighbours(x, y)
        if self.__cells[x][y] == 1: # alive cell
            return 1 if alive_neighbours in (2, 3) else 0 # cell dies if it has less than 2 or more than 3 alive neighbours
        else: # dead cell
            return 1 if alive_neighbours == 3 else 0 # cell is born if it has exactly 3 alive neighbours
        
    def _count_alive_neighbours(self, x: int, y: int) -> int:
        neighbours = [(x + i, y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0)] # all 8 neighbours
        return sum(self.__cells[i % self.__board_size[0]][j % self.__board_size[1]] for i, j in neighbours) # count alive neighbours
    
    def empty_cells(self) -> list[list[int]]:
        return [[0 for _ in range(self.__board_size[1])] for _ in range(self.__board_size[0])] # empty cells list
    
    @property
    def size(self) -> tuple[int, int]:
        return self.__board_size
    
    @property
    def cell_size(self) -> int:
        return self.__cell_size

    def __getitem__(self, pos: tuple[int, int]) -> int:
        x, y = pos
        return self.__cells[x][y]

        