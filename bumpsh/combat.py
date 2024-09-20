# 1.25 harder to level per level
# 10 exp per level of the npc killed
import time
import os

def fight(npc1, npc2):
    messages = [] # chronlogically store combat messages here

    # loop until dead
    while npc1.dead == False and npc2.dead == False:
        messages.append(attack(npc1, npc2)) # npc1 gets first turn
        messages.append(attack(npc2, npc1)) 
        os.system("clear") # clear (wont work on windows yet)

        # keep the messages outputted to screen below 6
        if len(messages) > 5:
            cut = len(messages) - 5
        else:
            cut = 0
        counter = cut

        for message in messages[cut:]:
            counter += 1 # keep track of turn count
            print (f"##move: {counter}##")
            print (message[0]) # says what damage was deflected
            print (message[1]) # says how much damage was done total
            print("##next move##")
    time.sleep(5)

    # check for game over
    if npc1.npc_type == "player": 
        if npc1.dead == True:
            os.system("clear")
            print("game over")
            exit()
    elif npc2.npc_type == "player":
        if npc2.dead == True:
            os.system("clear")
            print("game over")
            exit()

def attack(npc1, npc2):
    attack_type = npc1.take_combat_input(npc2) # takes input from npc
    damages = npc1.weapon.damage_calculation(npc1.stats,attack_type) # calcultates damages
    defense_messsages, damage_total, damage_before_armour = npc2.armour.calculate_damage_taken(damages) # runs armour through the armour class
    
    messages = []
    messages.append(defense_messsages)

    if npc2.dead == True:
        messages.append(f"killed {npc2.name} with {damage_total} damage!")
    else:
        messages.append(f"hit {npc2.name} with {damage_total} damage.")
    npc2.take_damage(damage_total)

    return messages # returns combined attack and defense messages




