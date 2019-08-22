from pygame import *
from Colours import *

class Snake():

    def __init__(self, window, board):

        self.window = window
        self.board = board

        self.head_pos = [2,5]
        self.x_change = 0
        self.y_change = 1

        self.body = [
            self.head_pos,
            [2,4],
            [2,3],
            [2,2]
        ]


    def changeDirection(self, events):

        for event in events:
            if event.type == KEYDOWN:
                if key.name(event.key)  == 'right':
                    self.x_change = 1
                    self.y_change = 0
                if key.name(event.key)  == 'left':
                    self.x_change = -1
                    self.y_change = 0
                if key.name(event.key)  == 'up':
                    self.x_change = 0
                    self.y_change = -1
                if key.name(event.key)  == 'down':
                    self.x_change = 0
                    self.y_change = 1


    def ateFood(self, food):

        if [food.x, food.y] == self.head_pos:
            self.growBody([food.x, food.y])
            return True

        return False


    def growBody(self, tailPos):

        self.body.append(tailPos)


    def drawSnake(self):

        print('Len:', self.body)

        for i in range(0, len(self.body)):

            if i == 0:
                nextCubePos = self.body[i][:]
                self.head_pos = [self.head_pos[0] + self.x_change,
                                    self.head_pos[1] + self.y_change]
                self.body[i] = self.head_pos[:]
                thisCubePos = self.body[i][:]
            else:
                thisCubePos = nextCubePos
                nextCubePos = self.body[i][:]
                self.body[i] = thisCubePos[:]


            draw.rect(
                self.window.gameDisplay,
                colours['grey'],
                (self.board.getPosition(*thisCubePos),
                (self.board.grid_size, self.board.grid_size))
            )

        print('Len:', self.body)
