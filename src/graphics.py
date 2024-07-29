import pygame
import sys
from game import Game

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAX_TICK_RATE = 60
DEFAULT_TICK_RATE = 10

class Graphics:
    """
    Class that handles the graphics and user input in Conway's Game of Life
    """

    def __init__(self, board_size: tuple[int, int], cell_size: int, tick_rate: int = DEFAULT_TICK_RATE):
        pygame.init()
        pygame.font.init()
        self.__cell_size = cell_size
        self.__board_size = board_size
        self.__game = Game(board_size, cell_size)
        self.__screen_size = (board_size[0] * cell_size, board_size[1] * cell_size)
        self.__screen = pygame.display.set_mode(self.__screen_size)
        self.__clock = pygame.time.Clock()
        self.__tick_rate = tick_rate
        self.__font = pygame.font.SysFont(None, 24)
        pygame.display.set_caption("Conway's Game of Life")

    def draw_cells(self):
        for x in range(self.__board_size[0]):
            for y in range(self.__board_size[1]):
                color = WHITE if self.__game.board[x, y] == 1 else BLACK # alive cell is white, dead cell is black
                pygame.draw.rect(self.__screen, color, (x * self.__cell_size, y * self.__cell_size, self.__cell_size, self.__cell_size)) # draw cell

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.__game.start_stop() # toggle game running state
                elif event.key == pygame.K_r:
                    self.__game.reset() # reset game state
                    self.__tick_rate = DEFAULT_TICK_RATE
                elif event.key == pygame.K_LEFT: 
                    if self.__tick_rate > 1: 
                        self.__tick_rate -= 1 # decrease tick rate
                elif event.key == pygame.K_RIGHT:
                    if self.__tick_rate < 60:
                        self.__tick_rate += 1 # increase tick rate
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.__game.running: # toggle cell state if game is not running
                    x, y = event.pos
                    self.__game.toggle_cell(x // self.__cell_size, y // self.__cell_size)

    def draw_ui(self):
        status = "Running" if self.__game.running else "Stopped"
        generation_text = self.__font.render(f'Generation: {self.__game.generation}', True, WHITE)
        status_text = self.__font.render(f'Status: {status}', True, WHITE)
        tick_rate_text = self.__font.render(f'Tick Rate: {self.__tick_rate}', True, WHITE)
        tutorial_text = self.__font.render("Press SPACE to Start/Stop, R to Reset, LEFT/RIGHT to Change Tick Rate", True, WHITE)
        self.__screen.blit(generation_text, (10, 15))
        self.__screen.blit(status_text, (200, 15))
        self.__screen.blit(tick_rate_text, (self.__screen_size[0] - 150, 15))

        if not self.__game.running:
            self.__screen.blit(tutorial_text, (self.__screen_size[0] // 2 - tutorial_text.get_width() // 2, self.__screen_size[1] - 30))


    def update(self):
        if self.__game.running:
            self.__game.next_generation()
            self.__clock.tick(self.__tick_rate) # generations per second

    def render(self):
        self.__screen.fill(BLACK)
        self.draw_cells()
        self.draw_ui()
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
