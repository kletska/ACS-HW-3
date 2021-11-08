from random import randint

from transport import Transport


class Train(Transport):
    def __init__(self):
        super().__init__()
        self.cars_number = None

    def in_from_file(self, file):
        super(Train, self).in_from_file(file)
        self.cars_number = int(file.pop())

    def in_rnd(self):
        super(Train, self).in_rnd()
        self.cars_number = randint(1, 100)

    def out(self, file):
        file.write(F'Train distance = {self.distance}, speed = {self.speed}, cars number = {self.cars_number}, optimal time = {self.optimal_time()}\n')
