class Player:
    '''the U-niverse'''

    def __init__(self, name):
        self.name = name
        self.loadnum = 0
        self.money = 23
        self.book = {}
        self.bag = {'pillow': 1, 'comb': 1, 'book': self.book}


