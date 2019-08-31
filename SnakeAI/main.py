from Window import *
from Snake import *
from Colours import *
from Board import *
from Food import *
import pygame


def game_over():

    game_font = pygame.font.Font(None, 60)
    game_over_text = game_font.render('Game Over', True, colours['black'])

    while True:
        events = pygame.event.get()

        window.gameDisplay.blit(game_over_text, (300, 150))
        window.handleQuit(events)

        window.run(10)


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

        if board.checkDeath(snake):
            break

        if snake.ateFood(food):
            food.makeFood(snake)

        window.run(7)


window = Window(800, 600, 'Snake')
board = Board(window, grid_size=25)
snake = Snake(window, board)
food = Food(board, snake)

play()
game_over()
