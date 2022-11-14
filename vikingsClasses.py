#Soldados
class Soldier:
    def __init__(self,health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def reciveDamage(self, damage):
        self.health -=  damage


class Vikings(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self,health, strength)
        self.name = name
    
    