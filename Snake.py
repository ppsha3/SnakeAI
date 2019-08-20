from pygame import draw
from Colours import *

class Snake():

    def reset(self):

        self.length = 4
        self.position = board.getPosition(5,5)


    def __init__(self, window, board):

        self.window = window
        self.board = board
        self.x_coord = 10
        self.y_coord = 11

        self.body = (
            self.board.getPosition(x_coord, y_coord),
            self.board.getPosition(x_coord, y_coord + 1),
            self.board.getPosition(x_coord, y_coord + 2),
            self.board.getPosition(x_coord, y_coord + 3)
        )

    def move(self):
        pass

    def renderSnake(self):

        for i in range(0, len(self.body)):

            draw.rect(
                self.window.gameDisplay,
                colours['grey'],
                (self.body[i],
                (self.board.grid_size, self.board.grid_size))
            )
