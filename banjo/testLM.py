import ollama
from .test.print_test import print_dud

modelfile='''
FROM llama3.1
SYSTEM You are mario from super mario bros.
'''

ollama.create(model='example', modelfile=modelfile)

prompt = "You are a system for a game that only responds as an NPC in a game. nothing else. you goal is to govern NPCs interactions with players in a medieval themed world. never state what your about to do, thats out of character. your goal is to respond like a person would given the NPC's personality and background, be fairly subtle when speaking of their background, it doesnt always need to come up but dont contradict it. you can use paratheses to show an action the character does. After you resieve the NPC's data please respond with only his exact reponse of what the NPC would say, never add anything else becides that, no system information. make it like a conversation. Here is the data:"
npc_1 = "name-Jerry Joe. context- greeting a player for the fist time. setting, in the town of evertale. Personality-nice wise friendly;backstory-a miner that had madea living off mining his whole life and supports his family,has grown up hearing stories of adventures and still enjoys hearing peoples tales. lives in evertale."
npc_2 = "Personality-kunning bad smart;backstory-I bad guy thats always looking out for himself, grew up in tyland, and now lives in hashvil. smith by trade, but does some under the table work as well."
#keep the stating of backstory



prompt_check_prompt = "your role is to varify/check if a response is realistic or plausable given the information / context. the information is from a game where an NPC is talking to a player, you will get a background for the character as well as personality traits and the most important part, their response or innitial interaction to the player. note that if you dont see character dialog or reponse or you see systen inforamtion, or its improperly foramtted just \'no\'. Its important to remember that this character lives in medieval times so no talk of real world infortation, technology or events. a correct repsonse should always be in character. please response to this prompt with the exact word \'yes\' if the response is plausable or \'no\' if not. here is the NPCs response for you to check:"
prompt_check_prompt2 = "you are to response with the exact word \'yes\' or \'no\' based on if the reponse you are given doesnt look like an exact response from a NPC in game. first we will feed you some information on the NPC, then when we tell you to verify the exact reponse. the game takes place in medieval times, a bad reponse ALSO includes talk of modern day events, or technology, or information. remember if the exact words arent exactly as a character would say then say no. if the words data or NPC are used anywhere in the response section say \'no\'"

intro_to_data = "ok that was some chracter information, here is exactly what you need to varify only this infomation, nothing before this, remember to reply with with exactly\'no\' or \'yes\' everytime:"


bad_response ="""
Please provide Jerry Joe's data. I will respond as him.

(Note: Please keep in mind that I'll only be responding with Jerry Joe's exact words, without any additional system information or context.) 

Go ahead and enter the NPC's data!"""



Var555 = False
bad_responses = []
while Var555 == False:
  response = ollama.chat(model='llama3.1', messages=[
    {
      'role': 'user',
      'content': prompt+npc_1,
    },
  ])
  response = response['message']["content"]

  response_check = ollama.chat(model='llama3.1', messages=[
    {
      'role': 'user',
      'content': prompt_check_prompt2+npc_1+intro_to_data+response+"car",
    },
  ])
  if response_check['message']["content"] == "yes" or response_check['message']["content"] == "Yes":
    Var555 = True
  else:
    bad_responses.append(response)

#keep context simple
#make sure it doesnt always go well, with interactions or how the character is feeling


print(response)
print(response_check['message']["content"])

print(bad_responses)

#interact - save chat - feed chat  respond - what for player input