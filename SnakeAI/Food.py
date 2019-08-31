from pygame import draw
from random import randint
from Colours import *

class Food():

    def checkFood(self, snake):

        while [self.x, self.y] in snake.body or self.x >= 25 or self.y >= 22:
            return False

        return True


    def makeFood(self, snake):

        while not self.checkFood(snake):

            self.x = randint(0, self.board.grid_size + 1)
            self.y = randint(0, self.board.grid_size + 1)

        return [self.x, self.y]


    def __init__(self, board, snake):

        self.board = board
        self.x = randint(0, self.board.grid_size)
        self.y = randint(0, self.board.grid_size)

        self.makeFood(snake)


    def drawFood(self, window):

        self.x_coord, self.y_coord = self.board.getPosition(self.x, self.y)

        food = draw.rect(
            window.gameDisplay,
            colours['black'],
            (self.x_coord,
             self.y_coord,
             self.board.grid_size,
             self.board.grid_size
             )
        )
