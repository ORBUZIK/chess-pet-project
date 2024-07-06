
from board import *
from player import *


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(0), Player(1)] #color 1 - white, 0 - black
        self.current_player = 1
    
    def switch_player(self):
        self.current_player = 1 - self.current_player
    
    def play(self):
        while True:

            self.board.display_board()
            player = self.players[self.current_player]
            
            move = player.get_move()

            if self.board.move_figure(*move, player):
                
                if self.board.is_checkmate(player.color):
                    print(f'{player.color} wins!')
                    break
                self.switch_player()
            
            else:
                print("Invalid move. Try again.")