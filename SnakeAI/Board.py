from pygame import draw
import threading
import time
from Colours import *


class Board():

    def  displayScore(self, snake):
        pass


    def __init__(self, window, grid_size):

        self.window = window
        self.grid_size = grid_size

        self.winner = None


    def getPosition(self, x, y):

        x_coord = x * self.grid_size
        y_coord = y * self.grid_size

        return [x_coord, y_coord]


    def getGridPoint(self, x, y):

        x_point = int(x/self.grid_size)
        y_point = int(y/self.grid_size)

        return [x_point, y_point]


    def makeColumns(self):

        columns = int(self.window.display_width/self.grid_size) + 1
        temp = 0

        for i in (range(1, columns)):

            start_point = (temp, 0)
            end_point = (temp, self.window.display_height - 50)

            draw.aaline(
                self.window.gameDisplay,
                colours['lime'],
                start_point,
                end_point
            )

            temp = temp + self.grid_size


    def makeRows(self):

        rows = int(self.window.display_height/self.grid_size)
        temp = 0

        for i in (range(1, rows)):

            start_point = (0, temp)
            end_point = (self.window.display_width, temp)

            draw.aaline(
                self.window.gameDisplay,
                colours['lime'],
                start_point,
                end_point
            )

            temp = temp + self.grid_size

        draw.aaline(
            self.window.gameDisplay,
            colours['black'],
            start_point,
            end_point
        )


    def drawGrid(self):

        column_thread = threading.Thread(target=self.makeColumns)
        row_thread = threading.Thread(target=self.makeRows)

        column_thread.start()
        row_thread.start()

        column_thread.join()
        row_thread.join()


    def checkDeath(self, snake):

        if 0 <= snake.head_pos[0] < 32 and 0 <= snake.head_pos[1] < 22:
            return False

        print(snake.head_pos)
        return True
