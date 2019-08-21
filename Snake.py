from pygame import *
from Colours import *

class Snake():

    def __init__(self, window, board):

        self.window = window
        self.board = board

        self.head_pos = [2,2]
        self.x_change = 0
        self.y_change = 1

        self.body = [
            self.head_pos
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
            self.growBody()
            return True

        return False


    def growBody(self):

        tailPos = self.body[-1]
        print('Tail', tailPos)
        self.body.append(tailPos)
        print('Body', self.body)


    def drawSnake(self):

        for i in range(0, len(self.body)):

            if i == 0:
                nextCubePos = self.body[i][:]
                # print('Next: ', nextCubePos)
                self.head_pos[0] = self.head_pos[0] + self.x_change
                self.head_pos[1] = self.head_pos[1] + self.y_change
                self.body[i] = self.head_pos
                # print('Head:', self.body[i], self.x_change, self.y_change)
                thisCubePos = self.body[i][:]
                # print('This:', thisCubePos)
            else:
                thisCubePos = nextCubePos
                nextCubePos = self.body[i]

            draw.rect(
                self.window.gameDisplay,
                colours['grey'],
                (self.board.getPosition(*thisCubePos),
                (self.board.grid_size, self.board.grid_size))
            )
