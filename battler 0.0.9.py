import math
import random

class inputHandler:
    def __init__(self, prompt=""):
        self.done = False
        self.prompt = prompt+"\n"
    
    def rawInput(self):
        self.playerInput = input(self.prompt)
        self.done = True
        return self.playerInput

    def stringInput(self):
        self.playerInput = input(self.prompt)
        self.done = True
        return self.playerInput

    def intInput(self):
        self.playerInput = input(self.prompt)
        while self.playerInput.isdigit() == False:
            self.playerInput = input(self.prompt)
        self.done = True
        return int(self.playerInput)


class BaseCharacter:
    def __init__(self, name):
        self.name = name + " " + self.__class__.__name__
        self.isPlayer = False
        self.setStats()
        self.spellBook()

    def setStats(self, baseHP = 10, baseMP = 10, baseSP = 10, baseLevel = 1):
        self.classModifier = 1
        self.level = baseLevel
        self.basehp = baseHP
        self.hp = self.maxhp = self.setHP()
        self.basemp = baseMP
        self.mp = self.maxmp = self.setMP()
        self.basesp = baseSP
        self.sp = self.maxsp = self.setSP()

    def setHP(self):
        self.classModifier = 1
        return self.basehp * ((self.classModifier * 1 ) * (self.level * 1))
    
    def setMP(self):
        self.classModifier = 1
        return self.basemp * ((self.classModifier * 1 ) * (self.level * 1))

    def setSP(self):
        self.classModifier = 1
        return self.basesp * ((self.classModifier * 1 ) * (self.level * 1))

    def rollInitiative(self, dice):
        result = random.randrange(1, dice)
        return result
    
    def isDead(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def printStatus(self):
        print(self.name+" status:")
        hpstatus = str(self.hp)+"/"+str(self.maxhp)
        mpstatus = str(self.mp)+"/"+str(self.maxmp)
        spstatus = str(self.sp)+"/"+str(self.maxsp)
        print("Health: "+ hpstatus)
        print("Mana: "+ mpstatus)
        print("Stamina: "+ spstatus)

    def spellBook(self):
        self.spellList = []


