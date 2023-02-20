import random


class Insect():

    def __init__(self, n, w, l):
        self.name = n
        self.wings = w
        self.legs = l
        self.flight = 0

    def set_flight(self):
        self.flight = random.randint(0, 10)

    def get_flight(self):
        return self.flight

    def get_name(self):
        return self.name
