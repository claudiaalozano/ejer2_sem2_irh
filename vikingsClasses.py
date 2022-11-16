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
    
    def attack(self):
        return super().attack()
    
    def reciveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "{} has recived {} points of damage".format(self.name, damage)
        else:
            return "{} has died in the combat".format(self.name)
        
    def battleCry(self):
        return "Odin Owns You ALL!"

class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
    
    def attack(self):
        return super().attack()
    
    def reciveDamage(self, damage):
        self.health -=  damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        else: 
            return"A Saxon has died in the combat"

class War:
    