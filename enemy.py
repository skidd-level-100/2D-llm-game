from mobs import *

class enemy(base_mob):
    mob_type = "ai"
    has_movement = True
    interactable = True

    def return_move(self):
        for mob in mobs:
            if mob.mob_type == "player":
                target_X = mob.location_X
                target_Y = mob.location_Y
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

    def interaction():
        os.system("clear")
        print("interacted")
        exit()