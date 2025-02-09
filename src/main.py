import pygame
import sys
from const import *
from game import *
class Main:
    def __init__(self):
        pygame.init() # inicjalizujemy biblioteke
        # metody pygame + nasze wartości
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess-AI')
        self.game = ChessGame()
    def MainLoop(self):
        game = self.game
        screen = self.screen
        while True:

            game.ShowBackground(screen)
            game.show_pieces(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

main = Main()
main.MainLoop()