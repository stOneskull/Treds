"""Newtown
(c)2018->
stOneskull"""


import pickle
import time
from random import choice

from player import Player
from god import God


Heart = True


def clr(lines=99):
    print('\n' * lines)


def sh(secs):
    time.sleep(secs)


def game_over():
    global Heart

    clr()

    decision = input('''


                 ___ Game Over ___

               Thank you for playing

                        o o
                       \___/



                Quit or Start Again


                        ''')

    if 'q' in decision.lower():
        Heart = None

    print(); sh(1); print(); sh(2)

    return start


def put(data, filename):
    """pickle save data"""

    with open(filename, 'wb') as jar:
        pickle.dump(data, jar)


def get(filename):
    """ return the pickled data
    or return 'nofile' """

    try:
        with open(filename, 'rb') as jar:
            data = pickle.load(jar)
        return data
    except:
        return 'nofile'


def save_game():
    clr()

    wannasave = input('\nSaving now, ok?  ')
    if 'n' in wannasave.lower():
        return options

    u.loadnum += 1

    savefile = u.name + str(u.loadnum) + '.dat'

    put(u, savefile)

    print('\nGame saved,', u.name + '..')
    sh(0.7)
    print('\nYour Load number is:', u.loadnum)
    sh(5)

    return options


def load_game():
    global u

    clr()

    try:
        name = u.name
    except:
        name = input('\nEnter your name\n').strip()

    loadnum = input('\nEnter your load number\n').strip()

    loadfile = name + loadnum + '.dat'

    see = get(loadfile)

    if see == 'nofile':
        print('no file to load! please wait..')
        sh(3)
        try:
            if u: return options
        except:
            print('starting new game..')
            sh(3)
            return start('new')

    u = see

    # load success

    loaded = 'Loaded.. Welcome back, ' + u.name
    sh(1.5); print(loaded); sh(3)

    clr()
    sh(1)

    return menu

def options():
    clr()
    print("""
    0 - Status
    1 - Resume Game
    4 - Save Game
    6 - Load Game
    8 - Quit Game
    """)

    options_map = {
        '0': status,
        '1': menu,
        '4': save_game,
        '6': load_game,
        '8': game_over,
    }

    while True:
        go = input('? ').strip()
        if go in options_map:
            return options_map[go]


def status():
    clr()
    print(u.name)
    sh(2)
    return options


def menu():
    print('room', u.god.rooms[u.god.eye])
    print("""
    0 - Options

    """)
    sh(3)
    sayit = input('mmhmm.. ')
    print('indeed, ' + sayit)
    sh(2)
    if sayit == '0':
        return options
    sh(3)

    print('room', u.god.rooms[u.god.eye])
    sh(1)
    return step

    #return calc(sayit)


def step():
    clr()
    print('step.. ')
    sh(2)
    u.god.eye += 1
    u.god.eye %= 40
    print('god eye:', u.god.eye)
    return menu


def calc(words):
    words = words.split()
    sh(2)
    print('thinking..')
    sh(3)
    for word in words:
        print(word)
        time.sleep(1)

    return menu


def new_game():
    global u

    while True:
        name = input('your name? ').strip()
        if name:
            break

    u = Player(name)
    u.god = God()
    return intro


def intro():
    for _ in range(50):
        for _ in range(50):
            print(choice(['\\', '/']), end='')
        print()

    sh(3)
    print('goto 10')
    sh(1)

    clr()
    sh(2)

    print('''

        The sky is charcoal

            It is very smoky


        There is a door in front of you

    ''')

    sh(2); print(); sh(1)

    return menu


def start(game=None):
    clr()

    while game != 'new':
        hmm = input('\n    1 - New game\n    2 - Load game\n? ')
        if hmm == '1':
            game = 'new'
        if hmm == '2':
            return load_game

    return new_game


def wonderwall(egg):
    while Heart is True:
        print(egg)
        egg = egg()


if __name__ == '__main__':
    wonderwall(start)
