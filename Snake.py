from pygame import draw
from Colours import *

class Snake():

    def reset(self):

        self.length = 4
        self.position = board.getPosition(5,5)


    def __init__(self, window, board):

        self.window = window
        self.board = board

        self.body = (
            self.board.getPosition(10,10),
            self.board.getPosition(10,11),
            self.board.getPosition(10,12),
            self.board.getPosition(10,13)
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
