import tkinter as tk


class Map:
    def __init__(self, rooms):
        self.window = tk.Tk()
        self.window.title('Map')
        self.populate(rooms)

    def populate(self, rooms):
        #11 x 11, 0 to 120
        draft_board = [
            list(range(square, square+11)) for square in range(0, 121, 11)
        ]

        tiles = {side:{square:[] for square in range(11)} for side in range(4)}

        sides = {
            0: list(range(120,110,-1)),
            1: list(range(110,0,-11)),
            2: list(range(11)),
            3: list(range(10,120,11)),
        }

        board = {}
        room_num = 0
        for side in sides:
            for square in sides[side]:
                board[square] = self.make_square(rooms[room_num])
                room_num += 1



    def make_square(self, room):
        square = tk.Label(
            self.window, text=f'{room}'
        )
        return square
