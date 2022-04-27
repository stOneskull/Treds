from threading import Thread
from time import sleep
from random import randint


class Tred(Thread):
    # override the run function
    def run(self):
        self.value = randint(1, 23)
        sleep(2)
        print('..This is coming from thread', self)
