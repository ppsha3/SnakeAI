from Window import *
from Snake import *
from Board import *
import pygame

def createCube(x, y):

    x_coord, y_coord = board.getPosition(x, y)

    cube = pygame.draw.rect(
        window.gameDisplay,
        colours['black'],
        (x_coord, y_coord, board.grid_size, board.grid_size)
    )


def play():

    play = True
    while play:

        board.makeGrid()
        food = createCube(1,1)
        snake.renderSnake()
        # board.displayScore(snake)
        window.handleQuit(pygame.event.get())
        window.run(30)


window = Window(800, 600, 'Snake')
board = Board(window, grid_size=25)
snake = Snake(window, board)
# self.head = createCube(eyes)

play()
