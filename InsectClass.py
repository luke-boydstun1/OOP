import random 


class Insect():

    def __init__(self):
        self.wings = 2
        self.legs = 6
        self.flight = 0

    def set_flight(self):
        self.flight = random.randint(0,10)

    def get_flight(self):
        return self.flight
        



