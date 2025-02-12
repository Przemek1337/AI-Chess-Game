from const import *
from square import Square
from Piece import *
from MovePiece import MovePiece
class Board:
    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(COLS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')
    def _create(self):  # '_' prywatne metody

        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)
    def CalculateMoves(self, piece, row, col):
        def PawnMoves():
            steps = 1 if piece.moved else 2
            start = row + piece.direction
            end = (row + (piece.direction * (1+steps)))
            for move_row in range(start, end, piece.direction):
                if Square.InRange(move_row):
                    if self.squares[move_row][col].IsEmpty():
                        initial = Square(row, col)
                        final = Square(move_row, col)
                        move = MovePiece(initial, final)
                        piece.add_move(move)
                    else:
                        break
                else:
                    break
            possible_move_row = row + piece.direction
            possible_move_cols = [col-1, col+1]
            for possible_move_col in possible_move_cols:
                if Square.InRange(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].HasRivalPiece(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = MovePiece(initial, final)
                        piece.add_move(move)

        def KnightMoves():
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1)
            ]
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.InRange(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].IsEmptyOrRivalPiece(piece.color):
                        initial = Square(row,col)
                        final = Square(possible_move_row,possible_move_col)
                        move = MovePiece(initial,final)
                        piece.add_move(move)

        if piece.name == 'pawn':
            PawnMoves()
        elif piece.name == 'knight':
            KnightMoves()
        elif piece.name == 'bishop':
            pass
        elif piece.name == 'rook':
            pass
        elif piece.name == 'queen':
            pass
        elif piece.name == 'king':
            pass

    def _add_pieces(self, color):
        row_pawn, row_other = (6,7) if color == 'white' else (1,0)
        #pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
        #knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        #bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        #queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        #king
        self.squares[row_other][4] = Square(row_other, 4, King(color))