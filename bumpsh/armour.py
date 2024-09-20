import random
from bumpsh.weapon import *
class armour():

    def __init__(self,rarity,level):
        self.rarity = rarity
        #sets rarity string 
        if rarity <= 2:
            self.rarity_str = f"common({rarity})"
        elif rarity <= 6:
            self.rarity_str = f"epic({rarity})"
        elif rarity <= 9:
            self.rarity_str = f"legendary({rarity})"
        elif 10 <= self.rarity:
            self.rarity_str = f"LEGENDARY({rarity})"
        else:
            self.rarity_str = f"common({rarity})"
        #applies random levelups if the armoour comes with level ups
        self.level = level
        keys = list(self.resistances.keys())
        for i in range(level):
            rand_key = random.choice(keys) # cheeky
            self.resistances[rand_key] += int(1 * (rarity / 2))

    # like stats but for armour
    resistances = {
        "phyisical": 5,
        "slash": 0,
        "stab": 0,
        "bash": 0,
        "base": 0,
        "elemental": 5,
        "fire": 0,
        "poision": 0
    }

    # for level up later
    def set_stats():
        pass
    # little wrapper function to grab only damage types and not amount of damage
    def get_damage_types(self, instance):
        return instance[1], instance[2]

    def calculate_damage_taken(self, damages):
        damage_total = 0
        damage_to_take = 0
        defense_messsages = []
        # grabs each damage instance and applies resistances
        for instance in damages:
            damage_base_type, damage_special_type = self.get_damage_types(instance) 
            damage_to_take = instance[0] # alias varable for the upcoming damage
            damage_before_armour = damage_to_take # not really used yet
            # if that damage type even exists
            if damage_special_type in self.resistances:
                # if you have levels in that damage type
                if self.resistances[damage_special_type] > 0:
                    percentage = self.resistances[damage_special_type] / 15 # if this doesnt come out to a decimal you are bad
                    subtracted_damaged = int(damage_to_take * percentage) # gets rid of damage based on percentage

                    #avoids negitives
                    if subtracted_damaged < 0: 
                        subtracted_damaged = damage_to_take
                    damage_to_take -= subtracted_damaged # subtracts damage from the total you take

                    defense_messsages.append(f"{self.rarity_str} armour absorbed {subtracted_damaged} of {damage_special_type} damage") # logs message

                    # same as above but with base damage types
            if damage_base_type in self.resistances:
                        percentage = self.resistances[damage_base_type] / 25
                        subtracted_damaged = int(damage_to_take * percentage)
                        if subtracted_damaged < 0:
                            subtracted_damaged = damage_to_take
                        damage_to_take -= subtracted_damaged
                        defense_messsages.append(f"{self.rarity_str} armour absorbed {subtracted_damaged} of {damage_base_type} damage")

            damage_total += damage_to_take # set total damage
            percentage = 0 # bug fix?
            damage_to_take = 0 # bug fix?
            
        return defense_messsages, damage_total, damage_before_armour # bam


# test code
def main():
    stats = {
    "fortitude" : 4,
    "strength" : 1,
    "charisma" : 1
    }

    for loop in range(1):
        test_armour = armour(9,10)
        test_weapon = weapon(4,10)
        keys = list(test_armour.resistances.keys())
        rand_key = random.choice(keys)
        defense_messsages, damage_total, damage_before_armour = test_armour.calculate_damage_taken(test_weapon.damage_calculation(stats, rand_key))
        print ("armour stats:")
        for key,value in test_armour.resistances.items():
            print (f"{key},{value}")
        for i in defense_messsages:
            print (i)
        print(f"{damage_total} out of {damage_before_armour} damage taken")
if __name__ == "__main__":
    main()


