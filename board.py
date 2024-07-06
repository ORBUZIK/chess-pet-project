
from xmlrpc.client import Boolean, boolean
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
        board[1] = [Pawn(0, (i, 1)) for i in range(1, 9)]
        board[6] = [Pawn(1, (i, 6)) for i in range(1, 9)]

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
        # board[1][4] = Qween(0, (4, 1))
        # board[5][3] = Qween(0, (3, 5))
        # board[6][4] = Bishop(1, (4, 6))
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
        
        print("\n"*35)
    

    # def move_figure(self, start_pos, end_pos) -> None:
    #     figure = self.board[start_pos[1]][start_pos[0]]
        
    #     # Выбрана ли фигура
    #     if figure is None:
    #         return "Выбрана пустая клетка!!!"

    #     # Можно ли сделать ход
    #     if end_pos not in figure.get_valid_moves(self.board):
    #         return "На данную клетку нельзя сходить!!!"
        
    #     # Проверяем, не будет ли король находится под атакой
    #     temp_board = [row[:] for row in self.board]
    #     cur_king = None
    #     for row in temp_board:
    #         for ceil in row:
    #             if isinstance(ceil, King) and ceil.color == figure.color:
    #                 cur_king = ceil
    #                 break
    #         if cur_king:
    #             break
    #     if not cur_king:
    #         return "Не получилось найти короля 😕"
        
    #     temp_board[end_pos[1]][end_pos[0]] = temp_board[start_pos[1]][start_pos[0]]
    #     temp_board[start_pos[1]][start_pos[0]] = None
    #     if cur_king.is_in_check(cur_king.position, temp_board):
    #         return "На данную клетку нельзя сходить!!!"

        
    #     # Передвигаем фигуру
    #     figure.position = end_pos
    #     self.board[end_pos[1]][end_pos[0]] = figure
    #     self.board[start_pos[1]][start_pos[0]] = None

    def move_figure(self, start_pos: tuple, end_pos: tuple, player) -> Boolean:
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        figure = self.board[start_y][start_x]

        # Выбрана ли фигура
        if figure is None:
            print("Выбрана пустая клетка!!!")
            return False
        
        # Правильный ли цвет
        if figure.color != player.color:
            print("Можно двигать только свои фигуры")
            return False
        
        # Можно ли сделать ход
        if end_pos not in figure.get_valid_moves(self.board):
            print("На данную клетку нельзя сходить!!!")
            return False
        
        # Проверяем, не будет ли король находится под атакой
        # temp_board = [row[:] for row in self.board]
        # temp_board[end_y][end_x] = temp_board[start_y][start_x]
        # temp_board[start_y][start_x] = None


        # Сделать ход -> посмотреть не находится ли король под атакой -> вернуть ход если да



    def is_in_check(self, color):
        # Метод для проверки, находится ли король под шахом
        pass

    def is_checkmate(self, color):
        # Метод для проверки мата
        pass


# TESTING
