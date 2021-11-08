from random import randint

from transport import Transport


class Plain(Transport):
    def __init__(self):
        super().__init__()
        self.fly_distance = None
        self.lifting_capacity = None

    def in_from_file(self, file):
        super(Plain, self).in_from_file(file)
        self.fly_distance = int(file.pop())
        self.lifting_capacity = int(file.pop())

    def in_rnd(self):
        super(Plain, self).in_rnd()
        self.fly_distance = randint(1, 100)
        self.lifting_capacity = randint(1, 100)

    def out(self, file):
        file.write(F'Plain distance = {self.distance}, speed = {self.speed}, fly distance = {self.fly_distance}, lifting capacity = {self.lifting_capacity} optimal time = {self.optimal_time()}\n')

    def optimal_time(self):
        return self.fly_distance / self.speed
