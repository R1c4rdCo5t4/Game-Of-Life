from board import Board

class Game:
    """
    Game class that represents the game logic in Conway's Game of Life
    """
    def __init__(self, board_size: tuple[int, int], cell_size: int):
        self.__board = Board(board_size, cell_size)
        self.__running = False
        self.__generation = 0

    def start_stop(self):
        self.__running = not self.__running

    def next_generation(self):
        self.__board.next_generation()
        self.__generation += 1

    def reset(self):
        self.__board.reset()
        self.__generation = 0
        self.__running = False

    def toggle_cell(self, x: int, y: int):
        self.__board.toggle_cell(x, y)

    @property
    def running(self) -> bool:
        return self.__running
    
    @property
    def generation(self) -> int:
        return self.__generation
    
    @property
    def board(self) -> Board:
        return self.__board

    
