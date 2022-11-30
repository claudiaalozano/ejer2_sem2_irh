#Soldados
import random
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
    def __init__(self):
        self.vikingarmy = []
        self.saxonarmy = []
    def addviking(self, viking):
        self.vikingarmy.append(viking)
    def addsaxon(self, saxon):
        self.saxonarmy.append(saxon)
    def vikingattack(self):
        saxon = random.choice(self.saxonarmy)
        viking = random.choice(self.vikingarmy)
        result = saxon.reciveDamage(viking.attack())
        if saxon.health <= 0:
            self.saxonarmy.remove(saxon)
        return result
    def saxonattack(self):
        saxon = random.choice(self.saxonarmy)
        viking = random.choice(self.vikingarmy)
        result = viking.reciveDamage(saxon.attack())
        if viking.health <= 0:
            self.saxonarmy.remove(viking)
        return result
    def showStatus(self):
        if len(self.saxonarmy) == 0:
            return "The Vikings have won"
        elif len(self.vikingarmy) == 0:
            return "Saxons have fought for their lives and survive another day "
        elif len(self.vikingarmy) >=1 and len(self.saxonarmy) >=1:
            return "The viking and saxon are still in the battle"