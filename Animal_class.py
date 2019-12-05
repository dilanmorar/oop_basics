# define animal class

class Animal():
    # class is a cookie cutter for objects
    # define some characteristics
    def __init__(self, name, eyes, legs, age = 0):
        self.bones = True
        self.alive = True
        self.age = 0
        self.number_legs = eyes
        self.number_eyes = legs
    # define some behaviours - methods -
        # things an instance of an object can do
        # fuctions that are dependent on a functions type
    def eat(self, food):
        return 'nom nom nom ' + food
    def mating(self):
        return '<3'
    def mate_calling(self):
        return 'swipe right'
    def sleep(self):
        return 'zzz'
    def go_potty(self):
        return 'dfmkdbhik'

