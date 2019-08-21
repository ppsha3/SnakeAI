from Window import *
from Snake import *
from Board import *
from Food import *
import pygame

def play():

    play = True

    while play:

        events = pygame.event.get()

        window.handleQuit(events)

        board.drawGrid()
        # board.displayScore(snake)

        food.drawFood(window)

        snake.drawSnake()
        snake.changeDirection(events)

        # if snake.ateFood(food):
        #     food.randomFood(snake)

        window.run(5)


window = Window(800, 600, 'Snake')
board = Board(window, grid_size=25)
snake = Snake(window, board)
food = Food(board)

play()
