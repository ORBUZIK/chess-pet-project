

class Player:
    def __init__(self, color: int): #color 1 - white, 0 - black
        self.color = color
        self.number = 1 if self.color == 1 else 2


    def cords_to_pos(self, cords: str) -> tuple:
    
        trans_alph_x = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
        }

        trans_alph_y = {
            '1': 7,
            '2': 6,
            '3': 5,
            '4': 4,
            '5': 3,
            '6': 2,
            '7': 1,
            '8': 0,
        }

        x = trans_alph_x[cords[0]]
        y = trans_alph_y[cords[1]]

        return (x, y)


    def get_move(self) -> list[tuple, tuple]:
        while True:
            try:
                move = input(f"|Игрок {self.number}| Ваш ход: ").split()
                return [self.cords_to_pos(i) for i in move]
            except:
                print("Введите правильные координаты 😠")

