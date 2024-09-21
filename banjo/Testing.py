from Initiate_Chat import *
from Inventory import *
from Entity import *
from Personalities import *
from Backstory import *
from Name_Generator import *

#NPC_1.traits = "Kind,Friendly, wise"
#NPC_1.History = "[context] - greeting a player for the fist time. setting, - in the town of evertale. backstory-a miner that had madea living off mining his whole life and supports his family,has grown up hearing stories of adventures and still enjoys hearing peoples tales. lives in evertale. Always eager to trade."
#NPC_1.traits = "evil,mean, cunning"
#NPC_1.History = "Grew up in the town of fieldington but has been on the road for some time. used to be miner until he realized how much easier it was to just kill people and take their loot. Has 2 older brothers, is 22 years old, part of a gang."
#NPC_1.Context = "killing the player for their loot. Has been tracking the player for some time. he doesnt want to wait around talking."

#name-Jerry Joe. context- greeting a player for the fist time. setting, in the town of evertale. Personality-nice wise friendly;backstory-a miner that had madea living off mining his whole life and supports his family,has grown up hearing stories of adventures and still enjoys hearing peoples tales. lives in evertale. Always eager to trade."



NPC_1 = Spawn_Human(level=5, name=generate_name(),Traits=Give_Personality(3,5))
print(NPC_1.traits)
NPC_1.History = get_backstory(NPC_1.name,25,NPC_1.traits)
NPC_1.Context = "greeting a player for the fist time"
print(NPC_1.History)

NPC_1.Inventory.add(Food(
    name="burger",
    health_increase=10,
    quantity=5
))
NPC_1.Inventory.add(Food(
    name="ice cream",
    health_increase=5,
    quantity=1
))
NPC_1.Inventory.add(Food(
    name="popcorn",
    health_increase=30,
    quantity=2
))

print(i.name for i in NPC_1.Inventory.items)

#NPC_1.Inventory.print_inventory()

Initiate_Chat(None,NPC_1)


