from banjo.Entity import *
import random

class Village():
    def __init__(self,min,max,lv_min,lv_max) -> None:
        self.villagers = []
        for i in range(random.randint(min,max)):
            self.villagers.append(Spawn_Human(
                level=random.randint(lv_min,lv_max),
                is_player= False
            ))