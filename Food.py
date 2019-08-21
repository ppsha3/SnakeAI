from pygame import draw
from random import randint
from Colours import *

class Food():

    def randomFood(self, snake):

        while [self.x, self.y] in snake.body:
            self.x = randint(0, self.board.grid_size + 1)
            self.y = randint(0, self.board.grid_size + 1)

        return [self.x, self.y]

    def __init__(self, board):

        self.board = board

        self.x = randint(0, self.board.grid_size + 1)
        self.y = randint(0, self.board.grid_size + 1)

    def drawFood(self, window):

        self.x_coord, self.y_coord = self.board.getPosition(self.x, self.y)

        food = draw.rect(
            window.gameDisplay,
            colours['black'],
            (self.x_coord, self.y_coord, self.board.grid_size, self.board.grid_size)
        )
