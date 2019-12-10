#D&D Dice Rolling + Crit Calculator
import random


def Main ():
    #Main Body of the Dice Rolling Program
    attackBonus = getAttackBonus()
    attackRoll = genAttackRoll()
    attackTotal = int(attackBonus) + attackRoll

    crit = checkCrit(attackRoll)
    if crit == "Critical Failure!":
        print(crit + " - " + str(attackTotal))
        print("You missed and your weapon shattered!")

    elif crit == "Critical!":
        print(crit + " - " + str(attackTotal))
        damage = rollDamage(crit)
        print("You dealt " + str(damage) + "!")

    else:
        print("Attack Total: " + str(attackTotal))
        damage = rollDamage(crit)
        print("You dealt " + str(damage) + " Damage!")





def getAttackBonus():
    #Asks User for their Total Attack Bonus from their 
    # Character Sheet
    attackBonus = input ("Enter your Total Attack Bonus: " )

    return attackBonus


def genAttackRoll():
    #Generates Random Number for d20 Roll
    diceRoll = random.randint(1,20)
    
    return diceRoll


def checkCrit (x):
    #Checks the Randomly Generated d20 Roll 
    # for 1 (Crit Fail) or 20 (Crit Success)
    critFail = "Critical Failure!"
    critical = "Critical!"

    if x == 1:
        return critFail

    elif x == 20:
        return critical

    else:
        return ""

def rollDamage (crit):
    #Rolls your damage based on your Weapon
    diceSides = input ("Enter Damage Dice (dX): ")
    diceAmount = input ("Enter amount of dice: ")
    damageBonus = input ("Enter your Damage Bonus: ")
    damage = 0

    if crit == "Critical!":
        #Crits = 1 Max Damage Roll + 1 Normal Damage Roll
        for i in range (0, int(diceAmount)):
            #Rolling the Normal Damage Roll
            damage = damage + random.randint(1,int(diceSides))
        #Adding the Max Damage Roll and Damage Bonus
        damage = damage + (int(diceAmount) * int(diceSides)) + int(damageBonus)

    elif crit == "Critical Failure!":
        damage = 0

    else:
        for i in range (0,int(diceAmount)):
            #Rolling the Normal Damage Roll
            damage = damage + random.randint(1,int(diceSides))
        #Adding the Damage Bonus    
        damage = damage + int(damageBonus)

    return damage
        

Main()