from bumpsh.npcs import *
import os
import copy

global tiles # did you know that having access to game data is important?
tiles = {} # we use a dictionary because python negitive indexing simply loops into positive !@#$ and yea each tile is stored like "-1030" is a tile at -10, 30

# this is one dim_X * dim_Y sqaure that the player and npcs can exist in

class tile():

    def __init__(self):
        # just makes the backdrop different in every tile
        self.backdrop_seed = random.randint(1, 69696969)

    # testing, changes the backdrop seed
    def change_backdrop_seed(self):
        self.backdrop_seed = random.randint(1, 69696969)
    # backdrop textures, this might be fun to change for a boss arena
    textures = ["🟩","🟩","🟩","🟩","🟩","🟩","🌲"]

    backdrop = [] # backdrop is only made when the player is in the tile and then is deleted
    npcs = [] # add npcs externally

    player_has_been = False # truly hard to figure out (;
    
    #makes the backdrop, do NOT forget to run this for tiles that dont have it or EVERTHING in that tile breaks
    def make_backdrop(self):
        self.backdrop = create_blank_frame(self.backdrop_seed, self.textures)

    # actually renders a frame
    def render(self):
            map_with_npcs = place_npcs_in_frame(self.npcs, copy.deepcopy(self.backdrop)) # place npcs over the top of the backdrop
            final_frame = make_frame(map_with_npcs) # organizes the height into different lists of blocks(🟩)
            #os.system("clear") # clears terminal (add windows compat later)
            # prints each layer in the "correct" order
            for i in reversed(final_frame):
                print("".join(map(str, i))) # gets rid of pythons dumb list formatting

    # run this function on tiles the player has just entered or else the player wont exist
    def player_insert(self,players_class):
        tmp_list = [players_class]
        tmp_list.extend(self.npcs)
        self.npcs = tmp_list