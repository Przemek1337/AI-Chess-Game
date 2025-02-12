
class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def IsEmpty(self):
        return not self.has_piece()

    def HasTeamPiece(self, color):
        return self.has_piece() and self.piece.color == color
    def HasRivalPiece(self, color):
        return self.has_piece() and self.piece.color != color
    def IsEmptyOrRivalPiece(self, color):
        return self.IsEmpty() or self.HasRivalPiece(color)
    def has_piece(self):
        return self.piece is not None
    @staticmethod
    def InRange(*args):
        for argument in args:
            if argument < 0 or argument > 7:
                return False
        return True
#print(Square.InRange(1,5,2,1))