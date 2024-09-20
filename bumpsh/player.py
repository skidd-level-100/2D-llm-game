from bumpsh.mobs import *

class player(base_mob):
    mob_type = "player"
    has_movement = True
    def return_move(self):
        return getch.getch()