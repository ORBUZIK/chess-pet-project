# from dot import *


class Figure:
    icons = None

    def __init__(self, color: int, position: tuple): #color 1 - white, 0 - black
        self.position = position
        self.color = color
        self.icon = self.icons[self.color]

    def get_valid_moves(self, board):
        valid_moves = []

        for direction in self.directions:
            for i in range(1, 8):  # Максимальное количество клеток в любом направлении
                new_x = self.position[0] + direction[0] * i
                new_y = self.position[1] + direction[1] * i

                if 0 <= new_x < 8 and 0 <= new_y < 8:  # Проверка границ доски
                    if board[new_x][new_y] is None:  # Пустая клетка
                        valid_moves.append((new_x, new_y))
                    elif board[new_x][new_y].color != self.color:  # Вражеская фигура
                        valid_moves.append((new_x, new_y))
                        break
                    else:  # Собственная фигура
                        break
                else:
                    break
        
        return valid_moves


# Ладья
class Rook(Figure):
    icons = ["♖", "♜"]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Вправо, влево, вверх, вниз

    # icon_white = 
    # icon_black = 


# Конь
class Knight(Figure):
    icons = ["♘", "♞"]
    directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]


    # !!! ПЕРЕЗАПИСАТЬ get_valid_moves !!!

    # icon_white = 
    # icon_black = 


# Слон
class Bishop(Figure):
    icons = ["♗", "♝"]
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    # icon_white = 
    # icon_black = 


# Король
class King(Figure):
    icons = ["♔", "♚"]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]


    # !!! ПЕРЕЗАПИСАТЬ get_valid_moves !!!

    # icon_white = 
    # icon_black = 


# Королева
class Qween(Figure):
    icons = ["♕", "♛"]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    # icon_white = 
    # icon_black = 


# Пешка
class Pawn(Figure):
    icons = ["♙", "♟"]
    directions = [(-1, 1), (0, 1), (1, 1)]

    # icon_white = 
    # icon_black = 

