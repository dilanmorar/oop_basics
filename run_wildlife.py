from Animal_class import *
from Reptile_class import *

# how to create object
# creating an instance of animal class
simba = Animal('simba', 3, 1, 8)

ringo = Reptile('ringo', 3, 1, 8)
print(ringo.eat('food'))
print(ringo.seek_heat())

# 2 different results POLYMORPHISM
print(simba.mate_calling())
print(ringo.mate_calling())

# print(simba)
# print(type(simba))
#
# print(simba.eat('chicken'))
# print(simba.go_potty())
# print(simba.sleep())
#
# print(simba.age)
# print(simba.bones)