"""Newtown
(c)2018->
stOneskull"""


import pickle, queue, threading, time
from random import randint as d, choice
from player import Player


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
        Heart = False

    print(); sh(1); print(); sh(2)

    return main


def put(data, filename):
    '''pickle save data'''

    with open(filename, 'wb') as jar:
        pickle.dump(data, jar)


def get(filename):
    ''' return the pickled data
    or return 'nofile' '''

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
            return main('new')

    u = see

    # load success

    loaded = 'Loaded.. Welcome back, ' + u.name
    sh(1.5); print(loaded); sh(3)

    clr()
    sh(1)

    return menu


def menu():
    print("""
    0

    """)
    sh(3)
    sayit = input('mmhmm..')
    print('indeed, ' + sayit)
    sh(3)
    return calc(sayit)


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
    name = input('your name? ').strip()
    u = Player(name)
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


def main(game='load'):
    clr()

    while game != 'new':
        hmm = input('\n    1 - New game\n    2 - Load game\n? ')
        if hmm == '2': return load_game
        if hmm == '1': game = 'new'

    return new_game


def wonderwall(egg):
    while Heart is True:
        egg = egg()


wonderwall(main)
