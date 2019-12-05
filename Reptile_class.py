from Animal_class import *

class Reptile(Animal):
    def __init__(self, name, eyes, legs, age = 0):
        super().__init__(name, eyes, legs, age)
        self.scales = True
        self.cold_blooded = True
        self.n_heart_chambers = heart_chambers

    # POLYMORPHISM re-defining the class
    def mate_calling(self):
        return 'look at my scales'
    def seek_heat(self):
        return 'it is cold'
    def seek_shade(self):
        return 'it is hot'
    def prey(self):
        return 'hungry'
    def lay_eggs(self):
        return 'egg laid'
