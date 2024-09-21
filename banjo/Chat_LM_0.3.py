import ollama
import os
from ollama import *
from Inventory import Inventory,Food

#response = generate('mistral', 'Why is the sky blue?')
#print(response['response'])


modelfile='''
FROM llama3.1_modded
SYSTEM You are a system for a game that acts as an NPC.
'''

ollama.create(
   model='example',
   modelfile=modelfile,
   )

#general notes:
  #maybe do separate checks of different areas of thought.
  #keep the stating of backstory
  #trading cant happen via dialog, quests cantr be given YET.
  #mke sure to not re greet people
  #filter looks for repeated text, like repeated introductions

  #change repeat penalty and how many tokcens to looks back on.
    #have a secondary prompt read conversation and decide wht actions were taken. or what owen said was have it make many true false statements like was it a possitive converation.

#first action is to leave conversation if the player is being weird of unfriendly. sicifically include examples, such as modern techbnology or player being to demanding

#to do
    #NPC data format next

    #Data from inventory
    #trading
    #update background on interact
NPC_Data = (f"""test {0}""".format(1))

name = "Harold Joe"
personality = "Kind,Friendly, Shy"
History = "Grew up in evertale and currently lives there. is 35 years old, has been a miner all his life. has a family. likes to here stories of adventures, always down to trade if he has anything. loves his town"

def Inventory_NPC_Format(Inventory):
  Formatted_Inventory = ""
  for item in Inventory.items:
    if item.is_stackable == True:
      Formatted_Inventory = Formatted_Inventory + f"\n{item.name} x{item.quantity}"
    else:
      Formatted_Inventory = Formatted_Inventory + f"\n{item.name}"
  return Formatted_Inventory

Inventory_1 = Inventory()
Inventory_1.add(Food(
    name="burger",
    health_increase=10,
    quantity=5
))
Inventory_1.add(Food(
    name="ice cream",
    health_increase=5,
    quantity=1
))
Inventory_1.add(Food(
    name="popcorn",
    health_increase=30,
    quantity=2
))

print(Inventory_NPC_Format(Inventory_1))

NPC_Data = (f"""
Name = {name}
Personality = {personality}
History = {History}
[Inventory]{Inventory_NPC_Format(Inventory_1)}
""")
#learn to print off args. unlimited
#iterate a seaprate string based on inventory and append, even use .format




print(NPC_Data)

#NPC's data
npc_1 = "name-Jerry Joe. context- greeting a player for the fist time. setting, in the town of evertale. Personality-nice wise friendly;backstory-a miner that had madea living off mining his whole life and supports his family,has grown up hearing stories of adventures and still enjoys hearing peoples tales. lives in evertale. Always eager to trade."
npc_2 = "Personality-kunning bad smart;backstory-I bad guy thats always looking out for himself, grew up in tyland, and now lives in hashvil. smith by trade, but does some under the table work as well."

#initial prompt components for LM response------------------------------------------------------


Introduction = "you will be presented with serveral catagories of information that you need to know before responsing as an NPC in a game. catagories will be seaprated with [], do not use [] in your response."

Initial_Instruction = """[Initial Instructions]
you will be acting as the voice of an NPC in a game. 
this all takes place in medeival times.
you only respond with exactly as the NPC would with no other information. 
with that in mind never state what your about to do as a bot, thats out of character. 
You can use paratheses to show an action the character does. 
if the player speaks of unknowns places or things, dont have the NPC act like he knows. 
You can only refer to places in that are in the information presentted at the beginning or within the context given context.
Make sure that the NPC doesnt let the player order him around, he is his own person.
After you look over all the NPC's and current conversations data please respond with only his exact reponse (this can include a NPC Command) of what the NPC would say, never add anything else becides that, no system information. make it like a conversation."""



dialog_instructions = """[Dialog Instructions]
| now here all the dailog that has happened so far, please continue it as one fluid conversation no time has pasted in between dialog. 
If there isnt any dialog loaded simply have a in character greeting or introduction, this may actually be nohing if thats in character.
Do not speak for the player ever. 
Remember not to repeat this dialog, only say new response.
The Player can already see all the dialog that has happened, no need to repeat it.
you will need to consider this dialog before responding:"""

NPC_Command_Instructions = """Another vital part of interactions with the player in the use of "NPC Commands. 
This is how the NPC interacts with the game".
The game will read these commmands when they say a command, and then activate the command after the chat.
This is the only time the NPC will say something that doesnt look like  normal conversation or something that looks system like.
Rememeber this is for the game to read after the NPC says it, then it runs the command.
The NPC doesnt see the NPC commands or its brackets.
Dont force the conversation to use a NPC command let it happen naturally or not at all.
example if he is a trader, or market keeper, he will try to trade more vs a normal non trader wont just say lets trade, but if the player suggests it then he MIGHT.
The folllowing is the list of the ONLY NPC commands that you can use:
[Leave] : The NPC  Decideds that its time to leave the conversation, whether out of anger or just because its time to go.
[Trade] : The NPC decides that they want to start the trading process with the player, this opens the tading menu. ue this when he wants to trade in general or specific items. So even of they just begin the trading process use this command. Once the player is done trading make sure he wants to re intiate trading before running this command again.
[Attack] : The NPC decides that they are mad enough at the player to attack him, or that they want the loot the play has, or If they have any in character modivation to attack them, or if their role is to attack a player.  This initiates the games battle system.
To use them simply say in contenxt of the rest of th response generated "[NPC Command]" replacing the "NPC Command" words with one of the avialable NPC commands listed above.
So to summerize your ouptut should be the newest response that the NPC should have given the information provided, and say a NPC command in the mist of that if appropriate to the context.
Think of it as an action for the NPC to do.
"""

Reinteration_Of_Instructions = "[Reinteration Of Instructions]\nThat was all the information you need, now provide exactly what the character says in response (You can also use NPC commands within the text):"

#prompt compoents for checks -----------------------------------------------------------------------
Introduction_To_Check = "You will be presented inforamtion with a few catagories of information, these instructions and information will inform you how verify a response. A response from a NPC in a game in medieval times."
Initial_Check_Instructions = """[Initial Instructions]
you are to response with the exact word \'yes\' or \'no\' based on if the reponse you are given doesnt look like an exact response from a NPC in game. 
first we will feed you some information on the NPC incuding dialog that has happened in this conversation so far, then we will ask you to verify the reponse the NPC had. 
the game takes place in medieval times, a bad reponse ALSO includes talk of modern day events, or technology, or information.
You will also be looking for NPC commands which will be in brackets, your role will be to make sure the NPC used the NPC commands appropiately given the context. 
An example of a good use is if the NPC is talking about trading, then says lets trade and somewhere in there their is a "[Trade]" commands, that would be good.
An Example of a bad use, which you would simply reply with "no", is the NPC is having a good conversation, who doesnt have mean character triats, and then then run "[Fight]" which is a command that activates a battle with the player.
The Following are NPC commands and what they do:
[Leave] : The NPC  The player is leaving and its time to end the conversation or the NPC decideds that its time to leave the conversation, whether out of anger or just because ieither person is leaving or done with the conversation. This is used to end the interaction from either party.
[Trade] : The the player has suggested that they want to initiate trading with the NPC, this opens the tading menu. The NPC Should be able to suggest trading without opening menu yet when he actaully goes to trade, this command is run.
[Attack] : The NPC decides that they are mad enough at the player to attack him, or that they want the loot the play has, or if their role is to attack a player. This initiates the games battle system.
remember you are also varifying the valitity of the dialog itself, if the exact words arent exactly as a character would say (NPC Commands included) then say only the word no. 
if the words data or NPC or are used anywhere in the response section say \'no\'"""

Initial_Check_Dialog_Dnstructions = """[Dialog Instructions]
now here is all the dailog thats happened in the conversation so far, you will need to consider this information so you can varify the newest response of the NPC:"""

Reinteration_Of_Check_Instructions = """[Reinteration Of Instructions] ok that was some character information and dialog, here is that information I was speaking of that would like you to please varify this next part. 
nothing before this, remember to reply with with exactly\'no\' or \'yes\' everytime if the dialog fits the character and passed the filteres spoken of:"""


#format the inforamtion [Initial Instructions] [Information on NPC] [Conversation For Far] [Instructions For Response]

loaded_npc = NPC_Data
User_Input = ""
past_dialog = "[Dialog]:None"
while User_Input != "exit":
    Var555 = False
    bad_responses = []
    while Var555 == False:
      response = generate("llama3.1_modded",Initial_Instruction+loaded_npc+NPC_Command_Instructions+dialog_instructions+past_dialog+Reinteration_Of_Instructions)
      response = response["response"]

      check = generate("llama3.1_modded",Introduction_To_Check+Initial_Check_Instructions+loaded_npc+Initial_Check_Dialog_Dnstructions+past_dialog+Reinteration_Of_Check_Instructions+response)
      check = check["response"]


      #check for behavior and chec for valid response
      if check == "yes" or check == "Yes":
        Var555 = True
        if past_dialog == "[Dialog]:None":
          past_dialog = "[Dialog]: "
          past_dialog = "NPC:"+past_dialog+response
        else:
          past_dialog = past_dialog+"NPC:"+response+"\n"


    print(response)


    #scan different tags
    if "[Leave]" in response:
      User_Input = "exit"
      break
    if "[Trade]" in response:
      print("Trade Initiated")

    User_Input = input("\nEnter your response here or type \'exit\' to leave the converation: ")
    past_dialog = past_dialog+"Player:"+User_Input+"\n"

    if User_Input == "exit":
      response = generate("llama3.1_modded",Initial_Instruction+loaded_npc+NPC_Command_Instructions+dialog_instructions+past_dialog+Reinteration_Of_Instructions+"[Player Starts Leaving]\nIn this case the player has started walking away, leaving the conversation, reply based on if they are leaving out of context, make them react as such, if they already knew that they were leaving them respond as such. your reply will mark the end of the conversation:")
      response = response["response"]
      print(response)

    
      

    Var555 = False

    #if player leaves it says something, input *the player begins to leave, then get a repsonse then end loop.
