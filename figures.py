
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

                if 0 <= new_x <= 7 and 0 <= new_y <= 7:  # Проверка границ доски
                    if board[new_y][new_x] is None:  # Пустая клетка
                        valid_moves.append((new_x, new_y))
                    elif board[new_y][new_x].color != self.color:  # Вражеская фигура
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



# Конь
class Knight(Figure):
    icons = ["♘", "♞"]
    directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]


    def get_valid_moves(self, board):
        valid_moves = []

        for direction in self.directions:
            new_x = self.position[0] + direction[0]
            new_y = self.position[1] + direction[1]

            if 0 <= new_x <= 7 and 0 <= new_y <= 7:  # Проверка границ доски
                if board[new_y][new_x] is None:  # Пустая клетка
                    valid_moves.append((new_x, new_y))
                elif board[new_y][new_x].color != self.color:  # Вражеская фигура
                    valid_moves.append((new_x, new_y))
        
        return valid_moves



# Слон
class Bishop(Figure):
    icons = ["♗", "♝"]
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]



# Король
class King(Figure):
    icons = ["♔", "♚"]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]


    def get_valid_moves(self, board):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        possible_moves = []

        for direction in directions:
            new_x = self.position[0] + direction[0]
            new_y = self.position[1] + direction[1]

            if 0 <= new_x <= 7 and 0 <= new_y <= 7:
                target_piece = board[new_y][new_x]
                if target_piece is None or target_piece.color != self.color:
                    possible_moves.append((new_x, new_y))

        valid_moves = [move for move in possible_moves if not self.is_in_check(move, board)]
        
        return valid_moves

    def is_in_check(self, position, board):
        opponent_color = 1 if self.color == 0 else 0
        for row in board:
            for piece in row:
                if piece is not None and piece.color == opponent_color:
                    if position in piece.get_valid_moves(board):
                        return True
        return False                



# Королева
class Qween(Figure):
    icons = ["♕", "♛"]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]



# Пешка
class Pawn(Figure):
    icons = ["♙", "♟"]
    directions = [(0, 1), (-1, 1), (1, 1)]


    def get_valid_moves(self, board):
        valid_moves = []

        direction = self.directions[0]
        new_x = self.position[0] + direction[0]
        new_y = self.position[1] + direction[1]

        if 0 <= new_x <= 7 and 0 <= new_y <= 7:  # Проверка границ доски
            if board[new_y][new_x] is None:  # Пустая клетка
                valid_moves.append((new_x, new_y))

        for direction in self.directions[1:]:
            new_x = self.position[0] + direction[0]
            new_y = self.position[1] + direction[1]

            if 0 <= new_x <= 7 and 0 <= new_y <= 7:  # Проверка границ доски
                if board[new_y][new_x] is not None and board[new_y][new_x].color != self.color:  # По диагонали стоит вражеская фигура
                    valid_moves.append((new_x, new_y))
        
        return valid_moves


