from random import randint
from vikingsClasses import *

def fight(viking, saxon):
    number_v = int(input("Number of viking: "))
    number_s = int(input("Number of saxon: "))
    vikings = []
    saxons = []

    for i in range(number_v):
        vikings.append(viking)
    for i in range(number_s):
        saxons.append(saxon)
    
    while len(vikings) > 0 and len(saxons) > 0:
        viking = vikings[randint(0, len(vikings)-1)]
        saxon = saxons[randint(0, len(saxons)-1)]
        saxon.reciveDamage(viking.attack())
        if saxon.health <= 0:
            saxons.remove(saxon)
        else:
            viking.reciveDamage(saxon.attack())
            if viking.health <= 0:
                vikings.remove(vikings)
    
    if len(viking) > 0:
        print("The Vikings win.")
    else:
        print("The Saxons win.")

if __name__ == "__main__":
    
