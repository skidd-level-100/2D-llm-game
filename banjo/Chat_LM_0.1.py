import ollama
import os

test = "test"

modelfile='''
FROM llama3.1
SYSTEM You are mario from super mario bros.
'''

ollama.create(model='example', modelfile=modelfile)

#general notes:
  #maybe do separate checks of different areas of thought.
  #keep the stating of backstory
  #trading cant happen via dialog, quests cantr be given YET.
  #mke sure to not re greet people
  #filter looks for repeated text, like repeated introductions



#NPC's data
npc_1 = "name-Jerry Joe. context- greeting a player for the fist time. setting, in the town of evertale. Personality-nice wise friendly;backstory-a miner that had madea living off mining his whole life and supports his family,has grown up hearing stories of adventures and still enjoys hearing peoples tales. lives in evertale."
npc_2 = "Personality-kunning bad smart;backstory-I bad guy thats always looking out for himself, grew up in tyland, and now lives in hashvil. smith by trade, but does some under the table work as well."


#initial prompt components for LM response
prompt = "You are a system for a game that only responds as an NPC in a game. nothing else. you goal is to govern NPCs interactions with players in a medieval themed world. never state what your about to do, thats out of character. your goal is to respond like a person would given the NPC's personality and background, and past dailog, be fairly subtle when speaking of their background, it doesnt always need to come up but dont contradict it. you can use paratheses to show an action the character does. After you resieve the NPC's data please respond with only his exact reponse of what the NPC would say, never add anything else becides that, no system information. make it like a conversation. Here is the data:"
intro_to_past_dialog = "| That information was information about the character you will be speaking as. now here all the past dailog you will need to consider before responding:"

#prompt compoents for cheecks
prompt_check_prompt = "you are to response with the exact word \'yes\' or \'no\' based on if the reponse you are given doesnt look like an exact response from a NPC in game. first we will feed you some information on the NPC incuding potential dialog, then when we tell you to verify the exact reponse. the game takes place in medieval times, a bad reponse ALSO includes talk of modern day events, or technology, or information. remember if the exact words arent exactly as a character would say then say no. if the words data or NPC are used anywhere in the response section say \'no\'"
intro_to_past_dialog_check = "| That information was information about the character you will be varifing the newest response of. now here all the past dailog you will need to consider varifing the newest response:"
intro_to_response = "| ok that was some chracter information and dialog, here is that information I was speaking of that would like you to varify only this newest infomation, nothing before this, remember to reply with with exactly\'no\' or \'yes\' everytime:"


loaded_npc = npc_1
User_Input = ""
past_dialog = "None"
while User_Input != "exit":
    Var555 = False
    bad_responses = []
    while Var555 == False:
      response = ollama.chat(model='llama3.1', messages=[
        {
          'role': 'user',
          'content': prompt+loaded_npc+intro_to_past_dialog+past_dialog+"|ok now provide exactly what the character says in response"
        },
      ])
      response = response['message']["content"]

      #response_check = ollama.chat(model='llama3.1', messages=[
      #  {
      #    'role': 'user',
      #    'content': prompt_check_prompt+loaded_npc+intro_to_past_dialog_check+past_dialog+intro_to_response+response,
      #  },
      #])
      #if response_check['message']["content"] == "yes" or response_check['message']["content"] == "Yes":
      #  Var555 = True
      #  if past_dialog == "None":
      #      past_dialog = ""
      #      past_dialog = past_dialog+response
      #  else:
      #     past_dialog = past_dialog+"NPC:"+response+"\n"
      #     past_dialog = past_dialog+"Player:"+User_Input+"\n"
      #else:
      #  bad_responses.append(response)




      Var555 = True
    if past_dialog == "None":
      past_dialog = ""
      past_dialog = past_dialog+response
    else:
      past_dialog = past_dialog+"NPC:"+response+"\n"


    print(response)
    User_Input = input("\nEnter your response here or type \'exit\' to leave the converation: ")
    Var555 = False
    past_dialog = past_dialog+"Player:"+User_Input+"\n"

print(response)
#print(response_check['message']["content"])