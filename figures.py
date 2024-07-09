
class Figure:
    icons = None
    valid_moves = []
    stage = 0

    def __init__(self, color: int, position: tuple): #color 1 - white, 0 - black
        self.position = position
        self.color = color
        self.icon = self.icons[self.color]
    
    
    def update_valid_moves(self, board, game_stage: int):
        self.stage = game_stage
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
        
        self.valid_moves = valid_moves
        return valid_moves


    def get_valid_moves(self, board, game_stage: int):
        if self.stage == game_stage:
            return self.valid_moves
        else:
            return self.update_valid_moves(board, game_stage)


# Ладья
class Rook(Figure):
    icons = ["♖", "♜"]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Вправо, влево, вверх, вниз



# Конь
class Knight(Figure):
    icons = ["♘", "♞"]
    directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]


    def update_valid_moves(self, board, game_stage: int):
        self.stage = game_stage
        valid_moves = []

        for direction in self.directions:
            new_x = self.position[0] + direction[0]
            new_y = self.position[1] + direction[1]

            if 0 <= new_x <= 7 and 0 <= new_y <= 7:  # Проверка границ доски
                if board[new_y][new_x] is None:  # Пустая клетка
                    valid_moves.append((new_x, new_y))
                elif board[new_y][new_x].color != self.color:  # Вражеская фигура
                    valid_moves.append((new_x, new_y))
        
        self.valid_moves = valid_moves
        return valid_moves


    def get_valid_moves(self, board, game_stage: int):
        if self.stage == game_stage:
            return self.valid_moves
        else:
            return self.update_valid_moves(board, game_stage)




# Слон
class Bishop(Figure):
    icons = ["♗", "♝"]
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]



# Король
class King(Figure):
    icons = ["♔", "♚"]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]


    def is_in_check(self, board, game_stage: int):
        opponent_color = 1 if self.color == 0 else 0
        for row in board:
            for piece in row:
                if piece and piece.color == opponent_color:
                    if self.position in piece.get_valid_moves(board, game_stage):
                        return True
        return False                


    def update_valid_moves(self, board, game_stage: int):
        self.stage = game_stage
        possible_moves = []

        for direction in self.directions:
            new_x = self.position[0] + direction[0]
            new_y = self.position[1] + direction[1]

            if 0 <= new_x <= 7 and 0 <= new_y <= 7:
                target_piece = board[new_y][new_x]
                if target_piece is None or target_piece.color != self.color:
                    possible_moves.append((new_x, new_y))

        # valid_moves = [move for move in possible_moves if not self.is_in_check(move, board)]
        valid_moves = []
        # move = (x, y)    
        for move in possible_moves:
            move_x, move_y = move
            pos_x, pos_y = self.position[0], self.position[1]

            target = board[move_y][move_x]
            board[move_y][move_x] = self
            self.position = move
            board[pos_y][pos_x] = None

            if not self.is_in_check(board, game_stage):
                valid_moves.append(move)

            board[pos_y][pos_x] = self
            self.position = (pos_x, pos_y)
            board[move_y][move_x] = target


        self.valid_moves = valid_moves
        return valid_moves        


    def get_valid_moves(self, board, game_stage: int):
        if self.stage == game_stage:
            return self.valid_moves
        else:
            return self.update_valid_moves(board, game_stage)



# Королева
class Qween(Figure):
    icons = ["♕", "♛"]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]



# Пешка
class Pawn(Figure):
    icons = ["♙", "♟"]

    def update_valid_moves(self, board, game_stage: int):
        if self.color == 1:
            if self.position[1] == 6:
                self.directions = [(0, -1), (0, -2), (-1, -1), (1, -1)]
            else:
                self.directions = [(0, -1), (-1, -1), (1, -1)]
        else:
            if self.position[1] == 1:
                self.directions = [(0, 1), (0, 2), (-1, 1), (1, 1)]
            else:
                self.directions = [(0, 1), (-1, 1), (1, 1)]


        self.stage = game_stage
        valid_moves = []

        for direction in self.directions[:-2]:
            new_x = self.position[0] + direction[0]
            new_y = self.position[1] + direction[1]

            if 0 <= new_x <= 7 and 0 <= new_y <= 7:  # Проверка границ доски
                if board[new_y][new_x] is None:  # Пустая клетка
                    valid_moves.append((new_x, new_y))

        for direction in self.directions[-2:]:
            new_x = self.position[0] + direction[0]
            new_y = self.position[1] + direction[1]

            if 0 <= new_x <= 7 and 0 <= new_y <= 7:  # Проверка границ доски
                if board[new_y][new_x] and board[new_y][new_x].color != self.color:  # По диагонали стоит вражеская фигура
                    valid_moves.append((new_x, new_y))
        
        self.valid_moves = valid_moves
        return valid_moves    


    def get_valid_moves(self, board, game_stage: int):
        if self.stage == game_stage:
            return self.valid_moves
        else:
            return self.update_valid_moves(board, game_stage)



