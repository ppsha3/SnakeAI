from Window import *
from Snake import *
from Board import *
import pygame

displayFood()

def createFood(x, y):

    x_coord, y_coord = board.getPosition(x, y)

    food = pygame.draw.rect(
        window.gameDisplay,
        colours['black'],
        (x_coord, y_coord, board.grid_size, board.grid_size)
    )

    return food

def ateFood(snake, food):

    if snake.head_pos == [food[0], food[1]]:
        food = createFood(1, 1)


def play():

    play = True

    while play:

        events = pygame.event.get()

        window.handleQuit(events)

        board.drawGrid()
        # board.displayScore(snake)

        food.drawFood()

        snake.drawSnake()
        snake.changeDirection(events)

        if snake.ateFood(food):
            food.randomFood(snake)

        window.run(5)


window = Window(800, 600, 'Snake')
board = Board(window, grid_size=25)
snake = Snake(window, board)
food = Food(board)

play()
