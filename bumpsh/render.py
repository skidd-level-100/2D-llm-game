import random
from bumpsh.mapsetup import *
from bumpsh.npcs import *
import os 
# picks a random thing in a list, seemed useful random probably already has this but I didnt want to look it up
def pick_rand_in_list(list, seed):
    random.seed(seed)
    amount = len(list)
    return list[random.randint(1, amount) - 1]

# could be optimized but im tired
# makes a random backdrop that you later paste over the top of with npcs
def create_blank_frame(seed_original, textures):
    random.seed(seed_original)
    dim_X, dim_Y
    blank_frame = []
    for i in range(dim_X * dim_Y):
        seed = random.randint(1,6969696)
        blank_frame.append(pick_rand_in_list(textures,seed))
        seed_original = random.randint(1,6969696)
    return blank_frame

# the fabled "later" from the create_blank_frame function
#places all npcs passed into it into a given list(map)
def place_npcs_in_frame(npcs, map):
    for current_npc in npcs:
        map[current_npc.get_my_location()] = current_npc.texture
    return map

#actually makes a frame easy to render (kinda useful)
def make_frame(bad_frame):
    global dim_X, dim_Y
    layer_count = int((len(bad_frame) + 1) / dim_Y)
    frame = []
    for current_X in range(layer_count):
        frame.append(bad_frame[current_X * dim_X : current_X * dim_X + dim_X])
    return frame