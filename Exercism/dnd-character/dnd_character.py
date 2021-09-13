import random

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        atributes =[random.randrange(1,7) for i in range(0,4)]
        atributes.sort()
        atributes.pop(0)
        return(sum(atributes))
    
def modifier (constitution):
    return (constitution - 10)//2