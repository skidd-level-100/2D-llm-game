import random 
import copy 

class weapon():
    # most everthing is derivived via rarity and level
    def __init__(self, rarity, level):
        self.min_damage = random.randint(int(rarity / 2), rarity * 2)
        self.max_damage = random.randint(int( rarity / 2 + self.min_damage), rarity * 2 + self.min_damage)
        self.rarity = rarity
        self.level = level
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
        self.set_stats()

    # these you will RARELY unlock from certain actions
    status_effects = {
        "fire": 0,
        "poision": 0
    }
    
    # one in one hundred chance of getting a status effect (technically poision is rarer)
    #scales with rarity
    def recieve_status_effects(self):
        rng = random.randint(1, 100)
        if rng == 69 and self.status_effects["fire"] < 1:
            self.status_effects["fire"] = random.randint(1, self.rarity)
        elif rng == 32 and self.status_effects["poision"] < 1:
            self.status_effects["poision"] = random.randint(1, self.rarity)
            
    # update stats when you level up weapon
    def set_stats(self):
        additive = (self.level * int(self.rarity / 3))
        self.min_damage = self.min_damage + additive
        self.max_damage = self.max_damage + additive

    # the fun part
    def damage_calculation(self, stats_of_npc, attack_type):
        damage = 0
        weapon_damage = 0
        damages = []
        fire = False
        poision = False

        # check status proc for fire, proc chance averages the amount of status you have
        if self.status_effects["fire"] or attack_type == "fire":
            rng = random.randint(1, 100)
            fire_damage = random.randint(int(self.status_effects["fire"] / 2), int(self.status_effects["fire"] * 2))
            if attack_type == "fire":
                fire_damage += (fire_damage + fire_damage/5 + 2)
            elif attack_type == "elemental":
                fire_damage += (fire_damage + fire_damage/10 + 1)
            if rng < fire_damage:
                damages.append([int(fire_damage), "elemental", "fire"])
                fire = True

        # check status proc for poision, proc chance averages the amount of status you have
        if self.status_effects["poision"] or attack_type == "poision":
            rng = random.randint(1, 100)
            poision_damage = random.randint(int(self.status_effects["poision"] / 2), int(self.status_effects["poision"] * 2))

            if attack_type == "poision":
                poision_damage += (poision_damage + poision_damage/5 + 2)
            elif attack_type == "elemental":
                poision_damage += (poision_damage + poision_damage/10 + 1)
        
            if rng < poision_damage:
                damages.append([int(poision_damage), "elemental", "poision"])
                poision = True

        # if you get really lucky fire and poision combine into a third damage instance
        if fire and poision:
            additional_damage = poision_damage + fire_damage
            damages.append([additional_damage, "elemental", "elemental"])
        
        minimum_damage = copy.deepcopy(self.min_damage)
        maximum_damage = copy.deepcopy(self.max_damage)
        strenght = stats_of_npc["strength"]

        #attck types
        if attack_type == "risk":
            minimum_damage = int(minimum_damage / 3)
            maximum_damage = int(maximum_damage * 2)
            strenght += strenght + int(strenght/3) 
            damage_type = base
        elif attack_type == "slash":
            damage_type = "slash"
        elif attack_type == "stab":
            damage_type = "stab"
        elif attack_type == "bash":
            damage_type = "bash"
        else:
            damage_type = "base"

        damages.append([random.randint(minimum_damage + strenght, maximum_damage + strenght), "phyisical", damage_type]) # damage adds with strenght
        
        return damages




# test code
def main():
    stats = {
    "fortitude" : 4,
    "strength" : 1,
    "charisma" : 1
    }   
    while True:
        test_weapon = weapon(random.randint(1,10),random.randint(1,5))
        test_weapon.recieve_status_effects()
        damages = test_weapon.damage_calculation(stats, "elemental")
        print("start:")
        for i in damages:
            print(i)
        print("end:")

if __name__ == "__main__":
    main()