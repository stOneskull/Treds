from time import sleep

from tred import Tred


Heart = True


def bye():
    global Heart
    if "n" not in input("Continue? ").lower():
        return main
    Heart = None


def namer(namelist='both'):
    import tredata
    return tredata.choose_name(namelist)

def dresser():
    pass


def testing():
    print("tred..")
    thread = Tred(target=lambda: sleep(3), name='Treddy')
    thread.name = namer('male')
    print(thread.name, 'id:', thread.ident, 'alive:', thread.is_alive())
    # thread.name = namer('horse')
    thread.start()
    print('tred started..')
    print(thread.name, 'id:', thread.ident, 'alive:', thread.is_alive())
    thread.join()
    print('tred joined..')
    print(thread.name, 'id:', thread.ident, 'alive:', thread.is_alive())
    print(f'Got value: {thread.value}')

    return bye


def main():
    print("main..")

    return testing


def wonderwall(ball):
    while Heart is True:
        print("ball..", ball)
        ball = ball()


if __name__ == '__main__':
    wonderwall(main)
