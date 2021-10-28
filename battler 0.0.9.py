import math
import random

class Spell:
    def __init__(self):
        self.spellName = self.__class__.__name__
        self.tags = []
        self.appendTags()    

class OffensiveSpell(Spell):
    def appendTags(self):
        self.tags.append("offensive")
    
    def spellAction(self, caster, target):
        self.applyCost(self, caster)
        self.dealDamage(self, caster, target)   

class NormalAttack(OffensiveSpell):
    def appendTags(self):
        super().appendTags()
        self.tags.append("physical")

    def applyCost(self, caster):
       spellCost = int((baseCost * caster.level) * 1)
       caster.mp = caster.sp - spellCost
       return caster.mp

    def dealDamage(self, caster, target):
        damage = int((baseCost * caster.level) * 1)
        target.hp = target.hp - damage
        return target.hp  

class Fireball(OffensiveSpell):
    def appendTags(self):
        super().appendTags()
        self.attributedClass = "wizard"
        self.tags.append("magical")

    def applyCost(self, caster):
       spellCost = int((baseCost * caster.level) * 2)
       caster.mp = caster.mp - spellCost
       return caster.mp

    def dealDamage(self, caster, target):
        damage = int((baseCost * caster.level) * 1.2)
        return damage

class HeavySlash(OffensiveSpell):
    def appendTags(self):
        super().appendTags()
        self.attributedClass = "warrior"
        self.tags.append("physical")

    def applyCost(self, caster):
       spellCost = int((baseCost * caster.level) * 1.6)
       caster.sp = caster.sp - spellCost
       return caster.sp

    def dealDamage(self, caster, target):
        damage = int((baseCost * caster.level) * 1.25)
        target.hp = target.hp - damage
        return target.hp

class DaggerThrow(OffensiveSpell):
    def appendTags(self):
        super().appendTags()
        self.attributedClass = "rogue"
        self.tags.append("physical")

    def applyCost(self, caster):
       spellCost = int((baseCost * caster.level) * 4)
       caster.sp = caster.sp - spellCost
       return caster.sp

    def dealDamage(self, caster, target):
        damage = int((baseCost * caster.level) * 2)
        target.hp = target.hp - damage
        return target.hp        

class DefensiveSpell(Spell):
    def appendTags(self):
        self.tags.append("defensive")
    
    def spellAction(self, caster, target):
        self.applyCost(self, caster)
        self.blockDamage(self, caster, target)


class NormalDefense(DefensiveSpell):
    def appendTags(self):
        super().appendTags()
        self.tags.append("physical")

    def applyCost(self, caster):
       spellCost = int((baseCost * caster.level) * 1)
       caster.sp = caster.sp - spellCost
       return caster.sp

    def dealDamage(self, caster, target):
        damage = int((baseCost * caster.level) * 1)
        target.hp = target.hp - damage
        return target.hp          

class ManaShield(DefensiveSpell):
    def appendTags(self):
        super().appendTags()
        self.attributedClass = "wizard"
        self.tags.append("magical")

    def applyCost(self, caster):
       spellCost = int((baseCost * caster.level) * 1)
       caster.mp = caster.mp - spellCost
       return caster.mp

    def dealDamage(self, caster, target):
        damage = int((baseCost * caster.level) * 1)
        target.hp = target.hp - damage
        return target.hp              

class ShieldBlock(DefensiveSpell):
    def appendTags(self):
        super().appendTags()
        self.attributedClass = "warrior"
        self.tags.append("physical")

    def applyCost(self, caster):
       spellCost = int((baseCost * caster.level) * 1)
       caster.sp = caster.sp - spellCost
       return caster.sp

    def dealDamage(self, caster, target):
        damage = int((baseCost * caster.level) * 1)
        target.hp = target.hp - damage
        return target.hp              

class Dodge(DefensiveSpell):
    def appendTags(self):
        super().appendTags()
        self.attributedClass = "rogue"
        self.tags.append("physical")

    def applyCost(self, caster):
       spellCost = int((baseCost * caster.level) * 1)
       caster.sp = caster.sp - spellCost
       return caster.sp

    def dealDamage(self, caster, target):
        damage = int((baseCost * caster.level) * 1)
        target.hp = target.hp - damage
        return target.hp      

class GameManager:
    def rawInput(self, prompt):
        playerInput = input(prompt)
        return playerInput

    def stringInput(self, prompt):
        playerInput = input(prompt)
        return playerInput

    def intInput(self, prompt):
        playerInput = input(prompt)
        while playerInput.isdigit() == False:
            playerInput = input(prompt)
        return int(playerInput)


class BaseCharacter:
    def __init__(self, name):
        self.name = name + " " + self.__class__.__name__
        self.isPlayer = False
        self.setStats()
        self.spellBook()

    def setStats(self, baseHP = 10, baseMP = 10, baseSP = 10, baseLevel = 1):
        self.level = baseLevel
        self.basehp = baseHP
        self.hp = self.maxhp = self.setHP()
        self.basemp = baseMP
        self.mp = self.maxmp = self.setMP()
        self.basesp = baseSP
        self.sp = self.maxsp = self.setSP()
        self.statGrowthHP = self.hpGrowth()
        self.statGrowthMP = self.mpGrowth()
        self.statGrowthSP = self.spGrowth()

    def setHP(self):
        linearFactor = 0.1
        curveFlatness = 0.1
        curveStrength = 1
        return int(self.basehp + (((self.basehp * (self.level - 1) ** linearFactor) / linearFactor) * curveFlatness) * curveStrength)

    def setMP(self):
        linearFactor = 0.1 
        curveFlatness = 0.1
        curveStrength = 1
        return int(self.basemp + (((self.basemp * (self.level - 1) ** linearFactor) / linearFactor) * curveFlatness) * curveStrength)

    def setSP(self):
        linearFactor = 0.1
        curveFlatness = 0.1
        curveStrength = 1
        return int(self.basesp + (((self.basesp * (self.level - 1) ** linearFactor) / linearFactor) * curveFlatness) * curveStrength)
    
    def hpGrowth(self):
        linearFactor = 0.1
        curveFlatness = 0.1
        curveStrength = 1
        return int(self.basehp + (((self.basehp * (self.level - 1) ** linearFactor) / linearFactor) * curveFlatness) * curveStrength)

    def mpGrowth(self):
        linearFactor = 0.1 
        curveFlatness = 0.1
        curveStrength = 1
        return int(self.basemp + (((self.basemp * (self.level - 1) ** linearFactor) / linearFactor) * curveFlatness) * curveStrength)

    def spGrowth(self):
        linearFactor = 0.1
        curveFlatness = 0.1
        curveStrength = 1
        return int(self.basesp + (((self.basesp * (self.level - 1) ** linearFactor) / linearFactor) * curveFlatness) * curveStrength)

    def rollInitiative(self, dice):
        return random.randrange(1, dice)
    
    def isDead(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def isOOM(self):
        if self.mp <= 0:
            return True
        else:
            return False

    def isOOS(self):
        if self.sp <= 0:
            return True
        else:
            return False

    def printStatus(self):
        print(self.name + " status:")
        hpstatus = str(self.hp) + "/" + str(self.maxhp)
        mpstatus = str(self.mp) + "/" + str(self.maxmp)
        spstatus = str(self.sp) + "/" + str(self.maxsp)
        print("Health: " + hpstatus)
        print("Mana: " + mpstatus)
        print("Stamina: " + spstatus)

    def spellBook(self):
        self.spellList = [NormalAttack, NormalDefense]

    def castSpell(self, target):
        self.currentSpell = self.pickSpell()
        return self.currentSpell.spellAction(self.currentSpell, self, target)

    def pickSpell(self):
        if self.isPlayer == True:
            spell = self.spellList[GameManager.intInput()]
            return spell
        else:
            spell = self.spellList[2]
            return spell


class Wizard(BaseCharacter):
    def setHP(self):
        curveFlatness = 0.16 #0.16 is good default value for HP
        linearFactor = 0.22 #0.22 is good default value for HP
        curveStrength = 1.4 #1.4 is good default value for HP
        return int(self.basehp + (((self.basehp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def setMP(self):
        #https://www.desmos.com/calculator I HATE CURVES I HATE CURVES I HATE CURVES I HATE CURVES
        curveFlatness = 0.16 #0.16 is good default value for MP
        linearFactor = 0.13 #0.13 is good default value for MP
        curveStrength = 14.1 #14.1 is good default value for MP
        return int(self.basemp + (((self.basemp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def setSP(self):
        curveFlatness = 0.226 #0.226 is good default value for SP
        linearFactor = 0.927 #0.927 is good default value for SP
        curveStrength = 1.4 #1.4 is good default value for SP
        return int(self.basesp + (((self.basesp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def hpGrowth(self):
        curveFlatness = 0.16 
        linearFactor = 0.22 
        curveStrength = 1.4 
        return int(self.basehp + (((self.basehp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def mpGrowth(self):
        curveFlatness = 0.16 
        linearFactor = 0.13
        curveStrength = 14.1
        return int(self.basemp + (((self.basemp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def spGrowth(self):
        curveFlatness = 0.226 
        linearFactor = 0.927 
        curveStrength = 1.4 
        return int(self.basesp + (((self.basesp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def spellBook(self):
        super().spellBook()
        self.spellList.append(Fireball)
        self.spellList.append(ManaShield)


class Rogue(BaseCharacter):
    def setHP(self):
        curveFlatness = 0.16 #0.16 is good default value for HP
        linearFactor = 0.22 #0.22 is good default value for HP
        curveStrength = 1.4 #1.4 is good default value for HP
        return int(self.basehp + (((self.basehp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def setMP(self):
        #https://www.desmos.com/calculator I HATE CURVES I HATE CURVES I HATE CURVES I HATE CURVES
        curveFlatness = 0.16 #0.16 is good default value for MP
        linearFactor = 0.13 #0.13 is good default value for MP
        curveStrength = 14.1 #14.1 is good default value for MP
        return int(self.basemp + (((self.basemp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def setSP(self):
        curveFlatness = 0.226 #0.226 is good default value for SP
        linearFactor = 0.927 #0.927 is good default value for SP
        curveStrength = 1.4 #1.4 is good default value for SP
        return int(self.basesp + (((self.basesp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def hpGrowth(self):
        curveFlatness = 0.16 
        linearFactor = 0.22 
        curveStrength = 1.4 
        return int(self.basehp + (((self.basehp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def mpGrowth(self):
        curveFlatness = 0.16 
        linearFactor = 0.13
        curveStrength = 14.1
        return int(self.basemp + (((self.basemp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def spGrowth(self):
        curveFlatness = 0.226 
        linearFactor = 0.927 
        curveStrength = 1.4 
        return int(self.basesp + (((self.basesp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def spellBook(self):
        super().spellBook()
        self.spellList.append(DaggerThrow)
        self.spellList.append(Dodge)


class Warrior(BaseCharacter):
    def setHP(self):
        curveFlatness = 0.16 #0.16 is good default value for HP
        linearFactor = 0.22 #0.22 is good default value for HP
        curveStrength = 1.4 #1.4 is good default value for HP
        return int(self.basehp + (((self.basehp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def setMP(self):
        #https://www.desmos.com/calculator I HATE CURVES I HATE CURVES I HATE CURVES I HATE CURVES
        curveFlatness = 0.16 #0.16 is good default value for MP
        linearFactor = 0.13 #0.13 is good default value for MP
        curveStrength = 14.1 #14.1 is good default value for MP
        return int(self.basemp + (((self.basemp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def setSP(self):
        curveFlatness = 0.226 #0.226 is good default value for SP
        linearFactor = 0.927 #0.927 is good default value for SP
        curveStrength = 1.4 #1.4 is good default value for SP
        return int(self.basesp + (((self.basesp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def hpGrowth(self):
        curveFlatness = 0.16 
        linearFactor = 0.22 
        curveStrength = 1.4 
        return int(self.basehp + (((self.basehp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def mpGrowth(self):
        curveFlatness = 0.16 
        linearFactor = 0.13
        curveStrength = 14.1
        return int(self.basemp + (((self.basemp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)

    def spGrowth(self):
        curveFlatness = 0.226 
        linearFactor = 0.927 
        curveStrength = 1.4 
        return int(self.basesp + (((self.basesp * (self.level - 1) ** curveFlatness) / curveFlatness) * linearFactor) * curveStrength)       

    def spellBook(self):
        super().spellBook()
        self.spellList.append(HeavySlash)
        self.spellList.append(ShieldBlock)


def PickClass(bool):
    availableClasses = [Wizard, Rogue, Warrior]
    if bool == True:
        return availableClasses(GameManager.intInput("Pick a class: 1-Wizard 2-Rogue 3-Warrior"))
def Battle():
    player = PickClass(bool=True)
    enemy = PickClass(bool=False)

Battle()

Tester = Wizard("Casty")
Nigger = Wizard("Blasty")
Tester.setStats(10,10,10,2)
Nigger.setStats(10,10,10,2)
baseCost = 5
#Tester.currentSpell = Tester.spellList[2]
damage = Tester.castSpell(Nigger)
Tester.printStatus()
Nigger.printStatus()

#Figure out how you want the castSpell() to actually return its value or whatever the fuck it's meant to do, I don't know
#Finish the rest of the spells, see if you can get basic battle loop going, stop procrastinating you fucking faggot USE OBJECTS AS ARGUMENTS AND SELF'S SELVES