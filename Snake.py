from pygame import *
from Colours import *

class Snake():

    def __init__(self, window, board):

        self.window = window
        self.board = board

        self.head_pos = [5, 5]
        self.x_change = 0
        self.y_change = 1
        # self.turns = []

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

    def growBody(self):

        tailPos = self.body[-1]
        self.body.append[[tailPos[0], tailPos[1]]]

    # def drawHead(self):
    #
    #     nextCubePos = self.board.getPosition(self.x_coord, self. y_coord)
    #
    #     draw.rect(
    #         self.window.gameDisplay,
    #         colours['grey'],
    #         (self.board.getPosition(self.head_pos),
    #           self.board.grid_size, self.board.grid_size))
    #     )
    #
    #    return nextCubePos


    def drawSnake(self):

        for i in range(0, len(self.body)):

            if i == 0:
                self.head_pos[0] = self.head_pos[0] + self.x_change
                self.head_pos[1] = self.head_pos[1] + self.y_change

                thisCubePos = [self.head_pos[0], self.head_pos[1]]
            else:
                thisCubePos = self.body[i-1]

            draw.rect(
                self.window.gameDisplay,
                colours['grey'],
                (self.board.getPosition(*thisCubePos),
                (self.board.grid_size, self.board.grid_size))
            )
