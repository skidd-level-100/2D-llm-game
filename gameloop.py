from bumpsh.tile import *
from bumpsh.movement import *
from bumpsh.combat import *
import os

def game_loop():
    # this sets the games initial run up, when we have savable progress this will need a rework
    start_player = player(1,1,"00", "bumpsh")
    current_tile = get_tile(start_player.current_tile_X, start_player.current_tile_Y)
    current_tile.player_insert(start_player)
    last_tile_str = str(str(current_tile.npcs[0].current_tile_X) + str(current_tile.npcs[0].current_tile_Y))
    current_tile_str = last_tile_str
   
    ##uncomment these to test fighting
    #test_enemy = enemy(10,10,"00", "goblin")
    #fight(start_player,test_enemy)
   
   
    while True:
        # if your tile changes
        current_tile_str = str(str(current_tile.npcs[0].current_tile_X) + str(current_tile.npcs[0].current_tile_Y)) # caches current tile after moving for comparing later
   
        if last_tile_str != current_tile_str:
            last_tile = tiles[last_tile_str] # grabs the tile before you entered a new one
            current_tile = get_tile(last_tile.npcs[0].current_tile_X,last_tile.npcs[0].current_tile_Y ) # grabs a new tile (makes one if not exist)
            current_tile.player_insert(last_tile.npcs[0]) # copys the player over into the new tile
            del last_tile.npcs[0] # deletes the old player from the last tile
            if current_tile.player_has_been == False:
                populate_with_npcs(current_tile.npcs, [enemy(random.randint(5, 29), random.randint(5, 29), "EE", "enemy"), weird_object(random.randint(5, 29), random.randint(5, 29), "??", "object"), weird_object(random.randint(5, 29), random.randint(5, 29), "??", "object"), weird_object(random.randint(5, 29), random.randint(5, 29), "??", "object"), weird_object(random.randint(5, 29), random.randint(5, 29), "??", "object")], 5)
                current_tile.player_has_been = True
            del last_tile.backdrop # deletes backdrop from the last tile (keeps seed)
            current_tile.make_backdrop() # generates the backdrop from the saved seed
   
        os.system("clear")
        current_tile.render() # prints the map onto screen
   
        # cordnate displays
        print(f"{current_tile.npcs[0].current_tile_X}, {current_tile.npcs[0].current_tile_Y}")
        # moves all the npcs
        for npc in current_tile.npcs:
            if npc.has_movement == True:
                event_check(current_tile.npcs) # checks if the player is in the same place as an npc and executes that npcs interact function
   
                if npc.npc_type == "player":
                    last_tile_str = str(str(current_tile.npcs[0].current_tile_X) + str(current_tile.npcs[0].current_tile_Y)) # caches your current tile before moving
                move_npc(npc, current_tile.npcs)
                delete_dead(current_tile.npcs)
def main():
   game_loop()

if __name__ == "__main__":
    main()