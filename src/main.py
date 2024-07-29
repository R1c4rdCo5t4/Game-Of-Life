from graphics import Graphics

def main():
    board_size = (50, 30)
    cell_size = 20
    graphics = Graphics(board_size, cell_size)
    graphics.run()

if __name__ == '__main__':
    main()