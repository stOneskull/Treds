from threading import Thread
from time import sleep

class Tred(Thread):
    # override the run function
    def run(self):
        self.value = 23
        sleep(2)
        print('..This is coming from thread', self)
