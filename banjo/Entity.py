import random
from dataclasses import dataclass
from Inventory import Inventory



class NPC():
    def __init__(self,
        level: int,
        strength: int,
        constitution: int,
        is_player: bool = False,
        Inventory : Inventory = Inventory(),
        name : str = "John Smith",
        Traits : str = "[None]",
        History :str = "[None]",
        Context : str = "Meeting the player for the first time. but after you greet once, dont greet again, you already did that."
        ) -> None:

        self.level = level
        self.strength = strength
        self.constitution = constitution
        self.is_player = is_player
        self.name = name

        self.max_health = self.constitution * 3
        self.health = self.max_health

        #tag for if further data needs to be put in
        self.loaded = True

        #NPC Data
        self.Inventory = Inventory()
        self.traits = Traits
        self.History = History
        self.Context = Context


        if self.is_player == False:
            for _ in range(self.level-1):
                random_attribute = random.randint(1,2)
                if random_attribute == 1:
                    self.strength += 1
                elif random_attribute == 2:
                    self.constitution +=1
            self.max_health = self.constitution * 3
            self.health = self.max_health


def Spawn_Human(level: int, is_player: bool = False, name : str = "Human"):
    entity = NPC(
        is_player = is_player,
        level = level,
        strength = 2,
        constitution = 2,
        name = name
    )
    return entity

#def make_goblin(level: int, is_player: bool = False):
#    entity = EntityStats(
#        is_player = is_player,
#        level = level,
#        strength = 4,
#        constitution = 2
#        )
#    return entity


#def make_elf(level: int, is_player: bool = False):
#    entity = EntityStats(
#        is_player = is_player,
#        level = level,
#        strength = 2,
#        constitution = 2
#        )
#    return entity


def main():
    human = Spawn_Human(level=3, is_player=False)
    print(human.type)
    print(human.max_health)

    #goblin = make_goblin(level=3)
    #rint(goblin.type)
    #print(goblin.max_health)
    #elf = make_elf(level=2)
    #print(elf.type)
    #print(elf.max_health)


if __name__ == '__main__':
    main()




#lets say you run into a ememy, says something to you, then usually attacks, sometimes based on personality, and chance lets you say something first and maybe you can convince him not to fight you.
#personality prompt of ememeies
