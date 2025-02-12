import pygame
import sys
from const import *
from game import *
from MouseDragger import Dragger
class Main:
    def __init__(self):
        pygame.init() # inicjalizujemy biblioteke
        # metody pygame + nasze wartości
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess-AI')
        self.game = ChessGame()
        self.dragger = self.game.dragger
    def MainLoop(self):
        game = self.game
        screen = self.screen
        dragger = self.dragger
        board = self.game.board
        while True:
            game.ShowBackground(screen) # board display
            game.ShowMoves(screen)
            game.show_pieces(screen) # show all the pieces
            if dragger.dragging:
                dragger.UpdateBlit(screen)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.UpdateMouse(event.pos)
                    clicked_row = dragger.mouse_y // SQUARE_SIZE
                    clicked_col = dragger.mouse_x // SQUARE_SIZE
                    #print("Wiersz drag | konw", dragger.mouse_y, clicked_row)
                    #print("Kolumna drag | konw", dragger.mouse_x, clicked_col)
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        board.CalculateMoves(piece, clicked_row, clicked_col)
                        dragger.SaveInitial(event.pos)
                        dragger.DragPiece(piece)
                        game.ShowBackground(screen)
                        game.ShowMoves(screen)
                        game.show_pieces(screen)
                    # print(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.UndragPiece(piece)

                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.UpdateMouse(event.pos)
                        game.ShowBackground(screen)
                        game.show_pieces(screen)
                        dragger.UpdateBlit(screen)


                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

main = Main()
main.MainLoop()