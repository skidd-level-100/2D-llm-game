from npcs import *
from mapsetup import *
from tile import *

# returns a tile at the given cordnates
def get_tile(X, Y):
    global tiles
    if str(str(X) + str(Y)) in tiles:
        return tiles[str(str(X) + str(Y))]
    else:
        tiles[str(str(X) + str(Y))] = tile()
        tiles[str(str(X) + str(Y))].make_backdrop()
        return tiles[str(str(X) + str(Y))]

# returns False if the cordnates are out of tile, the from part is going to be used to check lines later
def boundry_check(from_X, from_Y, to_X, to_Y):
    if dim_X < to_X:
        return False
    elif to_X <= 0:
        return False
    elif dim_Y <= to_Y:
        return False
    elif to_Y < 0:
        return False
    else:
        return True

# lets the selected npc make a move

def move_npc(selected_npc, npcs):
    # who wouldve thought that if your npcs cant move that it cant move
    if selected_npc.has_movement == True:
        # makes stuff ez
        npc_X = selected_npc.location_X 
        npc_Y = selected_npc.location_Y

        # runs whatever the npcs does to pathfind in players case its getch.getch()
        move = selected_npc.return_move(npcs)

        #caching results of boundry_check to improve performance (this stuff runs many times per frame you know)
        b_check_1 = boundry_check(npc_X, npc_Y, npc_X, npc_Y + 1)
        b_check_2 = boundry_check(npc_X, npc_Y, npc_X - 1, npc_Y)
        b_check_3 = boundry_check(npc_X, npc_Y, npc_X, npc_Y - 1)
        b_check_4 = boundry_check(npc_X, npc_Y, npc_X + 1, npc_Y)

        # lets npc move if it is within tile boundrys
        if move == "w" and b_check_1 == True:
            selected_npc.location_Y += 1
        elif move == "a" and b_check_2 == True:
            selected_npc.location_X -= 1
        elif move == "s" and b_check_3 == True:
            selected_npc.location_Y -= 1
        elif move == "d" and b_check_4 == True:
            selected_npc.location_X += 1
        else: # oh I hate this part, if the player hits a tile edge change the tile cordnate correctly and move them into a realistic spot
            if selected_npc.npc_type == "player":
                if b_check_1 == False:
                    selected_npc.current_tile_Y += 1
                    selected_npc.location_Y = 1
                elif b_check_2 == False:
                    selected_npc.current_tile_X -= 1
                    selected_npc.location_X = dim_X - 1
                elif b_check_3 == False:
                    selected_npc.current_tile_Y -= 1 
                    selected_npc.location_Y = dim_Y - 1
                elif b_check_4 == False:
                    selected_npc.current_tile_X += 1
                    selected_npc.location_X = 1
