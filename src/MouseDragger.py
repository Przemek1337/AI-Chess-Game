import pygame
from const import *
class Dragger:
    def __init__(self):
        self.mouse_x = 0
        self.mouse_y = 0
        self.initial_row = 0
        self.initial_col = 0
        self.piece = None
        self.dragging = False
    def UpdateBlit(self, surface):
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        img = pygame.image.load(texture)
        img_center = (self.mouse_x, self.mouse_y)

        self.piece.texture_rect = img.get_rect(center=img_center)
        surface.blit(img, self.piece.texture_rect)
    def UpdateMouse(self, position):
        self.mouse_x, self.mouse_y = position # (xcorr, ycorr)

    def SaveInitial(self, position):
        self.initial_row = position[1] // SQUARE_SIZE
        self.initial_col = position[0] // SQUARE_SIZE
    def DragPiece(self, piece):
        self.piece = piece
        self.dragging = True
    def UndragPiece(self, piece):
        self.piece = None
        self.dragging = False