from random import randint

from plain import Plain
from ship import Ship
from train import Train


class Container:
    def __init__(self):
        self.data = []

    def in_from_file(self, file):
        while len(file) > 0: 
            transport_kind = str(file.pop())
            transport = None
            if transport_kind == "plain":
                transport = Plain()
            elif transport_kind == "ship":
                transport = Ship()
            elif transport_kind == "train":
                transport = Train()
            else:
                raise RuntimeError(F"unexpected transport kind {transport_kind}")

            transport.in_from_file(file)
            self.data.append(transport)

    def in_rnd(self, n):
        for i in range(n):
            transport_kind = randint(1, 3)
            transport = None
            if transport_kind == 1:
                transport = Plain()
            elif transport_kind == 2:
                transport = Ship()
            elif transport_kind == 3:
                transport = Train()

            transport.in_rnd()
            self.data.append(transport)

    def out(self, file):
        for i in range(len(self.data)):
            file.write(F'{i + 1}: ')
            self.data[i].out(file)

    def straight_selection_sort(self):
        for i in range(len(self.data)):
            min_index = i
            for j in range(i, len(self.data)):
                if self.data[j].optimal_time() < self.data[min_index].optimal_time():
                    min_index = j
            
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
