from bumpsh.render import *
from bumpsh.mapsetup import *
from bumpsh.armour import *
from bumpsh.events import *
from bumpsh.combat import *
import getch
import os

def pick_rand_in_list_no_seed(list):
    amount = len(list)
    return list[random.randint(1, amount) - 1]

# populates a npc list with random npcs in a list
def populate_with_npcs(npcs, npcs_to_add, amount):
    for i in range(amount):
        npcs.append(pick_rand_in_list_no_seed(npcs_to_add))


# run this on a list of npcs to remove dead ones, or after an npc could die
def delete_dead(npcs):
    index=0

    while index < len(npcs):

        if npcs[index].dead == True:
            del npcs[index]
            index -= 1

        index += 1

# check if a specific index within map is in use by a bot and returns the index value of that bot or False
def is_location_used_by_bot(real_location, npcs):
    for index, npc in enumerate(npcs):
        if npc.real_location == real_location and npc.npc_type != "player":
            return index
    return False
        
# if player location = npc location then run the interact event on that npc
def event_check(npcs): 
    used = is_location_used_by_bot(npcs[0].get_my_location(), npcs)
    if used != False:
        if npcs[used].interactable == True: 
            npcs[used].interaction()

# pathing from -> to, returns "left", "right", "up", "down"
def get_to(from_X, from_Y, target_X, target_Y):
 # returns what direction the target is from the original location
    total_X = from_X - target_X
    total_Y = from_Y - target_Y

    total_X_abs = abs(total_X)
    total_Y_abs = abs(total_Y)

    if total_Y_abs < total_X_abs:
        # X is furthest
        if 0 <= total_X:
            return "left"
        else:
            return "right"
    else:
        #Y is furthest
        if 0 <= total_Y:
            return "down"
        else:
            return "up"

# gets the real index of an abstacted X,Y location
def get_real_location(X, Y):
    global dim_X
    return dim_X * Y + X - 1


# basics of a "living" npc, all npcs should inherit this class
class base_npc():

    # sets base stats, locations, name, texture etc
    def __init__(self, location_X, location_Y, texture, name):
        self.max_health, self.base_max_damage, self.base_min_damage, self.min_damage, self.max_damage, self.max_health = 0,0,0,0,0,0 # zero out all stats
        self.health = 20
        self.texture = texture
        self.location_X, self.location_Y = location_X, location_Y # location with a tile()
        self.set_stats() # set all stats based on the "stats" dict
        self.name = name
        self.get_my_location() # gets real (index) location

    stats = {
        "fortitude" : 4,
        "strength" : 1,
        "charisma" : 1
    }   

    npc_type = "base" # type IE: type = "player"
    has_movement = False # can it move? if not the movement function skips it
    interactable = False # can it be interacted with? if not the event_check function skips it
    dead = False # is it dead, delete_dead function will delete it
    gold = 0 # hmmmmm


    # updates stat values based on stat levels
    def set_stats(self):
        self.max_health = self.stats["fortitude"] * 5
        self.base_min_damage, self.base_max_damage = 1, 4
        self.min_damage, self.max_damage = self.min_damage + self.stats["strength"], self.max_damage + self.stats["strength"]

    # gets index location and also caches the varable, in theory you can always use the cache but if you do some
    # weird crap you can use the return value as well
    def get_my_location(self):
        answer = get_real_location(self.location_X, self.location_Y)
        self.real_location = answer
        return answer

    # kill it
    def make_dead(self):
        self.dead = True
    
    def take_damage(self, damage):
        self.health -= damage
        self.health_check()

    def health_check(self):
        if self.health < 0:
            self.health = 0
            self.make_dead()


## CUSTOM NPCS

# player class
class player(base_npc):
    npc_type = "player"
    current_tile_Y = 0 # what tile are you on?
    current_tile_X = 0 # what tile are you on?
    has_movement = True

    weapon = weapon(1,1)
    armour = armour(1,1)

    # a function all moving npcs should have defined return: "w,a,s,d"
    def return_move(self, zero):
        return getch.getch()

    def take_combat_input(self, npc_to_kill):
        index_number = 1
        for index, value in self.armour.resistances.items():
            print(f"{index_number}) {index}")
            index_number += 1
            success = False
        while success == False:
            try:    
                choice = int(input("what attack do you choose: "))
                choice -= 1
                if choice < 0 or choice > len(self.armour.resistances) - 1:
                    print(f"invalid choice must be between 1 and {len(self.armour.resistances)}")
                else:
                    success = True
            except Exception as e:
                print("try again")
                print(e)
        return list(self.armour.resistances.keys())[choice]


# test enemy
class enemy(base_npc):
    npc_type = "enemy_bot"
    has_movement = True
    interactable = True
    weapon = weapon(0,0)
    armour = armour(0,0)
    
    # gets the players location and pathfinds to it
    def return_move(self, npcs):
        for npc in npcs:
            if npc.npc_type == "player":
                target_X = npc.location_X
                target_Y = npc.location_Y
                player_exists = True
                break
            else:
                player_exists = False
        if player_exists == True:
            direction = get_to(self.location_X, self.location_Y, target_X, target_Y)
            if direction == "up":
                return "w"
            elif direction == "left":
                return "a"
            elif direction == "down":
                return "s"
            elif direction == "right":
                return "d"

    # when the player is in the same location as this npc it runs this
    def interaction(self):
        os.system("clear")
        print("interacted")
        exit() # game over

    def take_combat_input(self, npc_to_kill):
        return list(self.armour.resistances.keys())[random.randint(1, len(self.armour.resistances) - 1)]

# yes technically items are npcs that cant move, fight me
class interactable_object(base_npc):
    has_movement = False
    interactable = True
    npc_type = "object"

# test weird object
class weird_object(interactable_object):
    def interaction(self):
        os.system("clear")
        choice = input(f"you find a weird object, touch it? y/N \n")
        if choice == "y":
            random_event()
        else:
            self.make_dead()
