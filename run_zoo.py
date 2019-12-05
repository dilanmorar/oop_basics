from Animal_class import *
from Reptile_class import *

# create 2 reptiles
reptile1 = Reptile('Ringo', 2, 4, 17)
reptile2 = Reptile('Susan', 2, 4, 16)

# make the reptiles sleep
print(reptile1.sleep())
print(reptile2.sleep())
print(reptile1.n_heart_chambers)