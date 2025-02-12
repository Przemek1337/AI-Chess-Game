import pygame
from const import *
from Board import Board
from MouseDragger import Dragger
class ChessGame:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
    # Show methods

    def ShowBackground(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) #light green
                else:
                    color = (119, 154, 88) # dark green
                rectangle = (col * SQUARE_SIZE, row * SQUARE_SIZE,
                             SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(surface, color, rectangle)
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = (col * SQUARE_SIZE + SQUARE_SIZE // 2,  row * SQUARE_SIZE + SQUARE_SIZE // 2)
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)
    def ShowMoves(self, surface):
        if self.dragger.dragging:
            piece =self.dragger.piece
            for move in piece.moves:
                color = '#C86464' if (
                    move.final.row + move.final.col) % 2 == 0 \
                    else '#C84646'
                rectangle = (move.final.col * SQUARE_SIZE, move.final.row * SQUARE_SIZE,
                             SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(surface, color, rectangle)