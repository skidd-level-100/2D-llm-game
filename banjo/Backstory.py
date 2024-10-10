from ollama import *
import banjo.Personalities

NPC_Data_Prompt = "\nThe following data contains thw characters name and triats:"

def get_backstory(name,age,traits):

    backstory_prompt = """Your role is to reply ONLY with the exact words decribing an NPCs backstory.
I only want you to say the NPCs backstory, no system relates comments or saying "here is your backstory".
keep in mind that the setting is in medieval times, no no talk aout future technology, and impliment medieval themes if applicable.
You response will be directly plugged into other systems and cant have non related text besides the backstory.
Please write an NPCs backstory given his or her triats, which will be provided shortly.
That being said keep the backstory light.
The content can not contain sexual or child abuse.
if content if of darker nature, be vague never specific.
Also the backstory doesnt always need to justify their behavior.
make sure you say it all in 3rd Person
please write one small paragraph for their childhood, and one for their adulthood also saying their durrent age.
Then after that say "[Likes/Dislikes]:" and name 5 likes or dislikes of this character not of each but total, each one labelled a like or dislike. meaning you could have 3 likes and 2 dislikes or 4 nd 1 or 2 and 3.
backstory does always need to explain how they got their traits.
Make this flow together.
"""

#smaller context model so you can generate faster
#   unc-llama-lexi_ctx_4
#      and
#   unc-llama-lexi
    response = generate("unc-llama-lexi_ctx_4",backstory_prompt+NPC_Data_Prompt+name+f" age:{age}; traits: {traits}")
    response = response["response"]
    return response



if __name__ == "__main__":
    traits = Personalities.Give_Personality(3,5)
    print(traits)
    print(get_backstory("Joe Robbins",25,traits))


#generate levels or skills based on backstory?
