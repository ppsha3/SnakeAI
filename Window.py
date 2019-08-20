from pygame import *
from Colours import *


class Window():

    def handleQuit(self, events):

        for event in events:
            # print(event)
            if event.type == QUIT:
                quit()
                exit()


    def run(self, fps):

        display.update()
        self.clock.tick(fps)
        self.gameDisplay.fill(colours['white'])


    def makeWindow(self, title):

        init()

        self.clock = time.Clock()

        gameDisplay = display.set_mode((self.display_width, self.display_height))
        display.set_caption(title)

        return gameDisplay


    def __init__(self, display_width, display_height, title):

        self.display_width = display_width
        self.display_height = display_height

        self.gameDisplay = self.makeWindow(title)
