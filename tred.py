from threading import Thread


class Tred(Thread):
    # override the run function
    def run(self):
        self.value = 23
        sleep(2)
        print('..This is coming from thread', self)
