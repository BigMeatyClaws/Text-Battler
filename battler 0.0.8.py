import random
import math                                              
def normalAttack(character):
    tags = ["default", "physical", "offensive"]
    damage = character.sp*(character.level*1.2)
    message = "throws a wild slap!"
    return tags, damage, message
def normalBlock(character):
    tags = ["default", "physical", "defensive"]
    block = character.sp*(character.level*1.2)
    message = "blocks!"
    return tags, block, message

def fireball(character):
    tags = ["magical", "offensive", "wizard"]
    damage = character.mp*(character.level*4)
    message = "throws a wild fireball!" 
    return tags, damage, message

def manaShield(character):
    tags = ["magical", "defensive", "wizard"]
    block = (character.mp*2)*(character.level*1.2)
    message = "throws...chunks of mana, for a shield! What?"
    return tags, block, message
def daggerThrow(character):
    tags = ["physical", "offensive", "rogue"]
    damage = (character.sp*2)*character.level
    message = "throws a dagger!"
    return tags, damage, message
def dodge(character):
    tags = ["physical", "defensive", "rogue"]
    block = (character.sp*5)*character.level
    message = "throws himself, out of the way!"
    return tags, block, message
def heavySlash(character):
    tags = ["physical", "offensive", "warrior"]
    damage = (character.sp*3)*character.level
    message = "throws a wild slash with his awfully nondescript sword! Is it even an object?!"
    return tags, damage, message
def shieldBlock(character):
    tags = ["physical", "defensive", "warrior"]
    block = character.sp*(character.level*4)
    message = "blocks! With a shield, at that!"
    return tags, block, message

#global spellbook for classes to pull their abilities from by index number
spellbook = [normalAttack, normalBlock, fireball, manaShield, daggerThrow, dodge, heavySlash, shieldBlock]

class BaseCharacter:
    def __init__(self, hp=1, mp=1, sp=1, level=1):
        self.hp = math.floor(hp*(level**1.1))
        self.mp = math.floor(mp*(level**1.1))
        self.sp = math.floor(sp*(level**1.1))
        self.level = level
        self.maxhp = self.hp
        self.maxmp = self.mp
        self.maxsp = self.sp
        self.knownSpells = spellbook[0:2]

class Wizard(BaseCharacter):
    def __init__(self, hp=1, mp=1, sp=1, level=1):
        super().__init__(hp, mp, sp, level)
        self.hp = math.floor((self.hp//2)*(self.level**1.1))
        self.mp = math.floor((self.mp//0.25)*(self.level**1.5))
        self.sp = math.floor(self.sp*(self.level**1.1))
        self.maxhp = self.hp
        self.maxmp = self.mp
        self.maxsp = self.sp        
        self.knownSpells = spellbook[0:4]


class Warrior(BaseCharacter):
    def __init__(self, hp=1, mp=1, sp=1, level=1):
        super().__init__(hp, mp, sp, level)
        self.hp = math.floor((self.hp//0.5)*(self.level**1.5))
        self.mp = math.floor((self.mp//2)*(self.level**1.1))
        self.sp = math.floor((self.sp//0.75)*(self.level**1.25))
        self.maxhp = self.hp
        self.maxmp = self.mp
        self.maxsp = self.sp
        self.knownSpells = spellbook[0:2] + spellbook[6:8]

class Rogue(BaseCharacter):
    def __init__(self, hp=1, mp=1, sp=1, level=1):
        super().__init__(hp, mp, sp, level)
        self.hp = math.floor((self.hp//0.8)*(self.level**1.05))
        self.mp = math.floor(self.mp*(self.level**1.05))
        self.sp = math.floor((self.sp//0.25)*(self.level**2))
        self.maxhp = self.hp
        self.maxmp = self.mp
        self.maxsp = self.sp
        self.knownSpells = spellbook[0:2] + spellbook[4:6]
#Global list for all the classes

availableClasses = [Rogue, Warrior, Wizard]
class playerInputClass:
    def __init__(self):
        self.choice = input()
    def promptedInput(prompt):
        choice = input(prompt)
        if choice.__class__ == str:
            choice = choice.lower()
        if choice == "y" or choice == "yes":
                choice = 1
        elif choice == "n" or choice == "no":
                choice = 0
        print("\n")
        return choice
    def intPromptedInput(prompt):
        choice = input(prompt)
        while choice.isnumeric() != True:
            choice = input(prompt)
        return int(choice)
#Main battle function
def Battle():
    returned = playerControlled = playerInputClass.promptedInput("Control this game? y/n")
    while returned != 0 and returned != 1:
        returned = playerControlled = playerInputClass.promptedInput("Control this game? y/n")
    turn = 0
    baseHP = 100
    baseMP = 100
    baseSP = 100
    baseLevel = 5
    if returned == 0:
        guy1 = random.choice(availableClasses)
        guy2 = random.choice(availableClasses)
    elif returned == 1:
        def classStrings(availableClasses):
            prompt = "Pick your character: "
            classes = ""
            num = 0
            for eachThing in availableClasses:
                num = num+1
                classes = classes+str(eachThing().__class__.__name__)+": "+str(num)+" "
            finalPrompt = prompt+classes
            return finalPrompt
        prompt = classStrings(availableClasses)
        output = playerInputClass.intPromptedInput(prompt)
        while output > len(availableClasses) or output < 1:
            print("Are you sure that was a real number belonging to a class?")
            output = playerInputClass.intPromptedInput(prompt)
        guy1 = availableClasses[output-1]
        guy2 = random.choice(availableClasses)
    def rollDice(sides):
        roll = random.randrange(1, sides)
        return roll

    def randomSpell(character):
        spell = random.choice(character.knownSpells)
        return spell #returns list of tags and value
    
    def spellChoice(character):
        prompt = "Pick spell: "
        availableSpells = ""
        num = 0
        for eachSpell in character.knownSpells:
            num = num+1
            availableSpells = availableSpells+" "+str(num)+": "+str(eachSpell.__name__)
        spell = input(prompt+availableSpells)
        spell = int(spell)
        spell = character.knownSpells[spell-1]
        while spell not in character.knownSpells:
            spell = input(prompt+availableSpells)
            spell = character.knownSpells[spell-1]
        return spell #list of tags and value

    def combatLoop(redFighter, blueFighter):
        if playerControlled == 0:
            akai = "Red "
        else:
            akai = "Player "
            redFighter.player = 1
            blueFighter.player = 0
        redFighter.name = akai+ redFighter.__class__.__name__
        blueFighter.name = "Blue " + blueFighter.__class__.__name__     

        def initRoll():
            red = rollDice(20)
            blue = rollDice(20)
            if red == blue:
                fighters = [redFighter, blueFighter]
                winner = random.choice(fighters)
                return winner, red, blue
            elif red>blue:
                winner = redFighter
                return winner, red, blue
            elif red<blue:
                winner = blueFighter
                return winner, red, blue
            else:
                print("something happened")


        def dealDamage(dealer):         
            spell = randomSpell(dealer)
            tags, value, message = spell(dealer)
            while "offensive" not in tags:
                spell = randomSpell(dealer)
                tags, value, message = spell(dealer)
            print("Dealer:", dealer.name)   
            if dealer.mp and dealer.sp > 0 and "offensive" in tags:
                damage = value                 
                print(dealer.name, message, str(damage)+" damage!")
                return damage                         
            elif dealer.sp > 0 and "offensive" in tags and "physical" in tags:
                damage = value            
                print(dealer.name, message, str(damage)+" damage!")
                return value                             
            elif dealer.mp > 0 and "offensive" in tags and "magical" in tags:
                damage = value               
                print(dealer.name, message, str(damage)+" damage!")
                return damage                
            #finish this
        def dealDamageChoice(dealer):
            spell = spellChoice(dealer)
            tags, value, message = spell(dealer)
            while "offensive" not in tags:
                spell = spellChoice(dealer)
                tags, value, message = spell(dealer)
            damage = value
            return damage
                #this too
        def reduceDamageChoice(taker):
            spell = spellChoice(taker)
            tags, value, message = spell(taker)
            while "defensive" not in tags:
                spell = spellChoice(taker)
                tags, value, message = spell(taker)
            block = value  
            return block

        def reduceDamage(taker):
            spell = randomSpell(taker)
            tags, value, message = spell(taker)
            while "defensive" not in tags:
                spell = randomSpell(taker)
                tags, value, message = spell(taker)
            print("Taker:", taker.name)                
            if taker.mp and taker.sp > 0 and "defensive" in tags:
                block = value  
                print(taker.name, message, str(block)+" block")
                return block                      
            elif taker.sp > 0 and "defensive" in tags and "physical" in tags:
                block = value  
                print(taker.name, message, str(block)+" block")
                return block                      
            elif taker.mp > 0 and "defensive" in tags and "magical" in tags:
                block = value         
                print(taker.name, message, str(block)+" block")
                return block                 

        def calculateDamage(attack, defense):
            resultingDamage = math.floor(attack) - math.floor(defense)
            resultingDamage = math.floor(resultingDamage)
            return resultingDamage    


        while redFighter.hp > 0 and blueFighter.hp > 0:
            nonlocal turn
            turn = turn + 1
            print("Turn ",turn)
            print("Fight status:", redFighter.name, str(redFighter.hp)+"/"+str(redFighter.maxhp),"vs",blueFighter.name, str(blueFighter.hp)+"/"+str(blueFighter.maxhp))    
            initiativeWinner, redRoll, blueRoll = initRoll()
            print("Initiative winner:", initiativeWinner.name+".", "Red:",redRoll, "vs Blue:", blueRoll)
            def damagePhase(firstFighter, secondFighter):
                if initiativeWinner == firstFighter:
                    if firstFighter.player == 1:
                        attack = dealDamageChoice(firstFighter)
                        defense = reduceDamage(secondFighter)
                    elif secondFighter.player == 1:
                        attack = dealDamage(firstFighter)
                        defense = reduceDamageChoice(secondFighter)
                    else:
                        attack = dealDamage(firstFighter)
                        defense = reduceDamage(secondFighter)                    
                    resultingDamage = math.floor(calculateDamage(attack, defense))
                    if resultingDamage > 0 and firstFighter.hp > 0:                       
                        secondFighter.hp = secondFighter.hp - resultingDamage
                        print(secondFighter.name, "took", str(resultingDamage), "damage!")
                        print(str(secondFighter.hp)+"/"+str(secondFighter.maxhp)) 
                    elif firstFighter.hp <= 0:
                        return                                       
                    elif resultingDamage <= 0:
                        print(secondFighter.name, "took no damage!")
                    else:
                        print("something went wrong 1")
                        return
                    if secondFighter.hp > 0:
                        if firstFighter.player == 1:
                            attack = dealDamage(secondFighter)
                            defense = reduceDamageChoice(firstFighter)
                        elif secondFighter.player == 1:
                            attack = dealDamageChoice(secondFighter)
                            defense = reduceDamage(firstFighter)
                        else:
                            attack = dealDamage(secondFighter)
                            defense = reduceDamage(firstFighter)                         
                        resultingDamage = math.floor(calculateDamage(attack, defense))
                        if resultingDamage > 0 and secondFighter.hp > 0:                           
                            firstFighter.hp = firstFighter.hp - resultingDamage
                            print(firstFighter.name, "took", str(resultingDamage), "damage!")
                            print(str(firstFighter.hp)+"/"+str(firstFighter.maxhp))
                        elif secondFighter.hp <= 0:
                            return
                        elif resultingDamage <= 0:
                            print(firstFighter.name, "took no damage!")
                        else:
                            print("something went wrong 2")
                            return
                elif secondFighter.hp > 0:
                    damagePhase(secondFighter, firstFighter)       
            damagePhase(redFighter, blueFighter)      


    combatLoop(guy1(baseHP, baseMP, baseSP, baseLevel), guy2(baseHP, baseMP, baseSP, baseLevel))
Battle()
