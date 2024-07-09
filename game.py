
from board import *
from player import *


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(0), Player(1)] #color 1 - white, 0 - black
        self.current_player = 1
        self.stage = 1
    
    def switch_player(self):
        self.current_player = 1 - self.current_player
    
    def play(self):
        # # Определяем valid_moves для всех фигур в первый ход 
        # for row in self.board:
        #     for piece in row:
        #         if piece:
        #             piece.get_valid_moves()

        # GREETING
        self.board.display_board()
        print("Welcom to Chess!")
        print('\n')
        print('Вводите ходы в формате: [координаты фигуры] [куда фигура ходит]')
        print(f'Пример: a2 a3')
        print('\n')

        while True:

            player = self.players[self.current_player]
            move = player.get_move()

            if self.board.move_figure(*move, player, self.stage):
                
                if self.board.is_checkmate(1 - player.color, self.stage):
                    print('\n')
                    print(f'🥳 Игрок {player.number} победил 🥳')
                    print('\n')
                    break

                self.stage += 1
                self.switch_player()
            
            self.board.display_board()