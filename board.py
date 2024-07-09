
from figures import *


class Board:
    def __init__(self):
        self.board = self.create_board()

    black_king = King(0, (4, 0))
    white_king = King(1, (4, 7))

    # Создаем начальную расстановку фигур на доске
    def create_board(self):
        board = [[None for j in range(8)] for i in range(8)]
        
        # Расстановка пешек
        board[1] = [Pawn(0, (i, 1)) for i in range(8)]
        board[6] = [Pawn(1, (i, 6)) for i in range(8)]

        # Расстановка ладей
        board[0][0] = Rook(0, (0, 0)) # Черная ладья
        board[0][7] = Rook(0, (7, 0)) # Черная ладья
        board[7][0] = Rook(1, (0, 7)) # Белая ладья
        board[7][7] = Rook(1, (7, 7)) # Белая ладья

        # Расстановка коней
        board[0][1] = Knight(0, (1, 0)) # Черный конь
        board[0][6] = Knight(0, (6, 0)) # Черный конь
        board[7][1] = Knight(1, (1, 7)) # Белый конь
        board[7][6] = Knight(1, (6, 7)) # Белый конь

        # Расстановка слонов
        board[0][2] = Bishop(0, (2, 0)) # Черный слон
        board[0][5] = Bishop(0, (5, 0)) # Черный слон
        board[7][2] = Bishop(1, (2, 7)) # Белый слон
        board[7][5] = Bishop(1, (5, 7)) # Белый слон

        # Расстановка королев
        board[0][3] = Qween(0, (3, 0)) # Черная королева
        board[7][3] = Qween(1, (3, 7)) # Белая королева

        # Расстановка королей
        board[0][4] = self.black_king # Черный король
        board[7][4] = self.white_king # Белый король


        # ====
        # board[1][1] = Pawn(1, (4, 1))
        # board[5][3] = Qween(0, (3, 5))
        # # board[6][4] = Bishop(1, (4, 6))
        # # board[6][4] = None
        # board[0][3] = None
        # ====

        return board
        

    # Отображаем доску
    def display_board(self):

        drawn_board = [
            ['  ', 'a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h '],
            ['8 '] + [None for _ in range(8)] + [' 8'],
            ['7 '] + [None for _ in range(8)] + [' 7'],
            ['6 '] + [None for _ in range(8)] + [' 6'],
            ['5 '] + [None for _ in range(8)] + [' 5'],
            ['4 '] + [None for _ in range(8)] + [' 4'],
            ['3 '] + [None for _ in range(8)] + [' 3'],
            ['2 '] + [None for _ in range(8)] + [' 2'],
            ['1 '] + [None for _ in range(8)] + [' 1'],
            ['  ', 'a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h '],
        ]

        # Заполнение доски фигурами и полями
        for i in range(8):
            for j in range(8):
                cur_ceil = self.board[i][j]

                if isinstance(cur_ceil, Figure):
                    drawn_board[1+i][1+j] = cur_ceil.icon + ' '

                elif i % 2 == 0:
                    if j % 2 == 0:
                        drawn_board[1+i][1+j] = '⬜️'
                    else:
                        drawn_board[1+i][1+j] = '⬛️'
                else:
                    if j % 2 == 0:
                        drawn_board[1+i][1+j] = '⬛️'
                    else:
                        drawn_board[1+i][1+j] = '⬜️'


        # Отрисовка доски в терминале
        print("\n"*15)

        for i in drawn_board:
            print(*i, sep='')
        
        print("\n"*25)
    

    # Перемещаем фигуру
    def move_figure(self, start_pos: tuple, end_pos: tuple, player, game_stage: int) -> bool:
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        figure = self.board[start_y][start_x]
        cur_king = self.white_king if player.color == 1 else self.black_king

        # Выбрана ли фигура
        if figure is None:
            print("Выбрана пустая клетка!!!")
            return False
        
        # Правильный ли цвет
        if figure.color != player.color:
            print("Можно двигать только свои фигуры!!!")
            return False
        
        # Можно ли сделать ход
        if end_pos not in figure.get_valid_moves(self.board, game_stage):
            print("На данную клетку нельзя сходить!!!")
            return False
        
        # Проверяем, не будет ли король находится под атакой
        # Сделать ход -> посмотреть не находится ли король под атакой -> вернуть ход если да
        target = self.board[end_y][end_x]
        self.board[end_y][end_x] = figure
        figure.position = end_pos
        self.board[start_y][start_x] = None

        if cur_king.is_in_check(self.board, game_stage):
            print("Ход ставит вашего короля под удар!!!")

            self.board[start_y][start_x] = figure
            figure.position = start_pos
            self.board[end_y][end_x] = target

            return False

        # Смена фигуры, если пешка дошла до конца
        if isinstance(figure, Pawn):
            if figure.color == 1:
                if figure.position[1] == 0:
                    self.change_pawn(figure)
            
            else:
                if figure.position[1] == 7:
                    self.change_pawn(figure)

        return True


    # Меняем пешку на другую фигуру
    def change_pawn(self, pawn):
        while True:
            print('На какую фигуру хотите поменять пешку?')
            print('- Qween')
            print('- Rook')
            print('- Bishop')
            print('- Knight')
            print('Укажите букву: Q / R / B / K')
            target_figure = input()
            
            pos_x, pos_y = pawn.position
            if target_figure == "Q":
                self.board[pos_y][pos_x] = Qween(pawn.color, pawn.position)
            elif target_figure == "R":
                self.board[pos_y][pos_x] = Rook(pawn.color, pawn.position)
            elif target_figure == "B":
                self.board[pos_y][pos_x] = Bishop(pawn.color, pawn.position)
            elif target_figure == "K":
                self.board[pos_y][pos_x] = Knight(pawn.color, pawn.position)
            else:
                print("Пожалуйста, выберите фигуру 😠")


    def is_checkmate(self, color, game_stage: int):
        cur_king = self.white_king if color == 1 else self.black_king
        cur_king.update_valid_moves(self.board, game_stage)
        
        # Король находиться под атакой
        if not cur_king.is_in_check(self.board, game_stage):
            return False
        
        # Король никуда не может сходить
        if len(cur_king.get_valid_moves(self.board, game_stage)) != 0:
            return False
        
        # Проверяем, какие фигуры могут защитить короля
        for y in range(8):
            for x in range(8):
                figure = self.board[y][x]
                if figure and figure.color == color:

                    for move in figure.get_valid_moves(self.board, game_stage):
                        move_x, move_y = move
                        start_pos = figure.position
                        target = self.board[move_y][move_x]

                        self.board[move_y][move_x] = figure
                        figure.position = move
                        self.board[y][x] = None

                        # Проверяем и возвращаем ход
                        if not cur_king.is_in_check(self.board, game_stage):
                            self.board[y][x] = figure
                            figure.position = start_pos
                            self.board[move_y][move_x] = target
                            return False
                        
                        # Возвращаем ход
                        self.board[y][x] = figure
                        figure.position = start_pos
                        self.board[move_y][move_x] = target
        
        return True



# TESTING
# Board().display_board()