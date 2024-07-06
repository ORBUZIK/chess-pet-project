

class Player:
    def __init__(self, color: int): #color 1 - white, 0 - black
        self.color = color


    def cords_to_pos(self, cords: str) -> tuple:
    
        trans_alph_x = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8,
        }

        trans_alph_y = {
            '1': 8,
            '2': 7,
            '3': 6,
            '4': 5,
            '5': 4,
            '6': 3,
            '7': 2,
            '8': 1,
        }

        x = trans_alph_x[cords[0]]
        y = trans_alph_y[cords[1]]

        return (x, y)


    def get_move(self) -> list[tuple, tuple]:
        move = input("Ваш ход: ").split()
        return [self.cords_to_pos(i) for i in move]

print(Player(1).get_move())