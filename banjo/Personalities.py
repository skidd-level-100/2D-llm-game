import random

def Give_Personality(min,max,Catagory=0):
    Personalities = [
    #neutral list
        [
        ["Friendly", "Unfriendly"],
        ["Mean","Nice"],
        "Creative",
        "Ambitious",
        "Determined",
        "Sarcastic",
        "Self-conscious",
        ["Wise","Foolish"],
        ["Proud","Humble"],
        ["Violent","NonViolent"],
        ["Brave","Coward"],
        ["Selfish","Selfless"],
        ["Ruthless","Merciful"]
    ],
    #unfriendly list
        [
        "Unfriendly",
        "Mean",
        "Creative",
        "Ambitious",
        "Determined",
        "Sarcastic",
        "Self-conscious",
        ["Wise","Foolish"],
        ["Proud","Humble"],
        "Violent",
        ["Brave","Coward"],
        "Selfish",
        "Ruthless",
        ],
    #friendly list
        [
        "Friendly",
        "Nice",
        "Creative",
        "Ambitious",
        "Determined",
        "Sarcastic",
        "Self-conscious",
        ["Wise","Foolish"],
        ["Proud","Humble"],
        "NonViolent",
        ["Brave","Coward"],
        "Selfless",
        "Merciful"
        ]

    ]
    random_p_indexes = []
    for i in range(random.randint(min,max)):
        bad_selection = True
        while bad_selection == True:
            new_random_p = random.randint(1,len(Personalities[0]))-1
            if not new_random_p in random_p_indexes:
                bad_selection = False
        random_p_indexes.append(new_random_p)
    
    Selected_Personalities = ""
    for i in random_p_indexes:
        if type(Personalities[Catagory][i]) == list:
            Selected_Personalities = Selected_Personalities + Personalities[Catagory][i][random.randint(1,len(Personalities[Catagory][i]))-1]+","
        else:
            Selected_Personalities = Selected_Personalities + Personalities[Catagory][i]+","


    return Selected_Personalities
if __name__ =="__main__":
    print(Give_Personality(1,5,2))


#paint the story of this NPC from childhood to adulthood, including his modivation during it and what it is now.
#town, not generated by AI, due to repitition.
#details on the town, climate, surrounding land, 0-2 memories they have in their town.
#childhood in few sentences
#ocupation, it doesnt need to be normal it could, be was on the run, be creative and dont feel you need to fill in these requirements with normal inforamtion.
#events that happened during life
#Current life goals