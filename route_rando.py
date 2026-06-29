import random

#level sets

level_1 = "Corneria"
level_2 = random.choice(["Sector Y", "Meteo"])

def find_level_3():
    set = None
    if level_2 == "Sector Y":
        set = ["Aquas", "Katina"]
    else:
        set = ["Katina", "Fichina"]
    return random.choice(set)

level_3 = find_level_3()

def find_set_4():
    set = None
    if level_3 == "Aquas":
        set = ["Zoness"]
    else:
        set = ["Solar", "Sector X"]
    return random.choice(set)

level_4 = find_set_4()

def find_level_5():
    set = None
    if level_4 == "Zoness":
        set = ["Sector Z", "Macbeth"]
    elif level_4 == "Solar":
        set = ["Macbeth"]
    else:
        set = ["Sector Z", "Macbeth", "Titania"]
    return random.choice(set)

level_5 = find_level_5()

def find_level_6():
    set = None
    if level_5 == "Titania":
        set = ["Bolse"]
    else:
        set = ["Area 6", "Bolse"]
    return random.choice(set)

level_6 = find_level_6()

level_7 = None
if level_6 == "Bolse":
    level_7 = "Venom"
else:
    level_7 = "Venom2"


route = [level_1, level_2, level_3, level_4, level_5, level_6, level_7, ""]

#Global restrictions (no max, no logic to prevent conflicts)
restrictions = [
    "No bombs.",
    "No charge shots.",
    "No laser upgrades. (Die once if you have any from previous levels.)",
    "Eliminate any available non-route-essential wingmen.",
    "Break at least one wing if possible.",
    "If wings break, don't fix them.",
    "Beat medal threshold by 10% or more.",
    "Lowest score allowed by route (Bosses don't count).",
    "No barrel rolls.",
    "No advanced maneuvers (Somersaults/U-turns).",
    "Avoid supply rings.",

]

def set_restriction(set):
    restrictions = set
    added_restrictions = []
    for i in restrictions:
        if random.randint(1,100) > 90:
            added_restrictions.append(i)
    if added_restrictions == []:
        return "No restrictions."
    else:
        return f"\n* ".join(added_restrictions)
        
#Level-specific restrictions (max 1 per level)
level_restrictions = {
    "Corneria": {
        "Meteo": [
            "Do not destroy any of Granga's limbs.",
            "Save Falco, beat him through all but the last arch.",
            "Don't save Falco, fly through the arches anyways."
    ],
        "Sector Y":[
            "Beat Falco through the arches.",
            "One-cycle the carrier's second phase."
        ]
    },
    "Sector Y": {
        "Katina": [
            "Go up at the path split.",
            "Go down at the path split.",
            "Wait for the Shogun Warlord to stand on the ship before defeating it.",
            "Get both of Peppy's compliments and remain under the Aquas threshold.",
            "Get Falco to insult you at least once.",
            "Spawn the 1Up."
        ],
        "Aquas": [
            "Go up at the path split.",
            "Go down at the path split.",
            "Wait for the Shogun Warlord to stand on the ship before defeating it.",
            "Get Falco to insult you at least once.",
            "Spawn the 1Up."
        ]
    },
    "Meteo": { 
        "Katina": [
            "Do not save Peppy when he gets chased.",
            "Do not save Slippy when he gets chased.",
            "Only shoot asteroids.",
            "In the warp, only shoot asteroids."
            "Destroy the rock containing the gold supply ring before Falco does."
    ],
        "Fichina": [
            "Do not save Peppy when he gets chased.",
            "Do not save Slippy when he gets chased.",
            "Get hit by each of the Crusher's attacks at least once. (Including the shield itself.)",
            "Destroy the rock containing the gold supply ring before Falco does.",
    ]
    },
    "Aquas": {
    "Zoness": [
        "No torpedoes until Bacoon.",
        "No lasers until Bacoon.",
        "No firing at all until Bacoon.",
        "No schmoovement allowed (no barrel rolls).",
    ]},
    "Katina": {
        "Solar": [
            "Destroy all Cornerian fighters.",
            "Destroy 3 or fewer Cornerian fighters.",
            "Destroy the core with 5 seconds or less on the timer.",
            "Shoot Bill at least 5 times.",
            "Only shoot Saucerer's core. (No allied or enemy fighters, no hatches.)",
        ],
        "Sector X": [
            "Get 0 points.",
            "Destroy all Cornerian fighters.",
            "Destroy 3 or fewer Cornerian fighters.",
            "Shoot Bill at least 5 times.",
            "Do not damage the Saucerer.",
            "Destroy all the hatches, do not touch the core."
        ]
    },
    "Fichina": {
        "Solar": [
            "Defeat Pigma first.",
            "Defeat Andrew first.",
            "Defeat Leon first.",
            "Defeat Wolf first.",
            "Win with no more than 10 seconds on the timer.",
            "Get no more than 44 points."
        ],
        "Sector X": [
            "Do not attack ANY member of Star Wolf.",
            "Spare only Pigma.",
            "Spare only Andrew.",
            "Spare only Leon",
            "Spare only Wolf.",
            "Leave with 0 points."
        ],
    },
    "Zoness": {
        "Sector Z": [
            "Shoot Katt each time she appears.",
            "Break the Sarumarine's periscope and make him fire blindly at least once.",
        ],
        "Macbeth": [
            "Get spotted immediately.",
            "Get spotted by the last searchlight.",
            "Shoot Katt each time she appears.",
            "Break the Sarumarine's periscope and make him fire blindly at least once.",
        ]
    },
    "Solar": {
        "Macbeth": [
            "Break Vulcain's left (your right) arm first.",
            "Break Vulcain's right (your left) arm first.",
            "Ignore Slippy when he gets chased.",
            "Ignore Falco when he gets chased.",
            "Do not shoot any rocks.",
            "Do not collect any supply rings."
        ]
    },
    "Sector X": {
        "Titania": [
            "Shoot slippy at least once before he becomes Smackie the Frog.",
            "Go left.",
            "Go right.",
            "Go right and ignore Peppy.",
            "Fly through all but one warp gate.",
            "Do not bomb the mines.",
            "Ignore Peppy when he gets chased early."
        ],
        "Macbeth": [
            "Don't defeat Spyborg until Slippy tries to help.",
            "Go left.",
            "Go right.",
            "Fly through all but one warp gate.",
            "Do not bomb the mines.",
            "Ignore Peppy when he gets chased early.",
            "Go right and ignore Peppy."
        ],
        "Sector Z": [
            "Do not bomb the mines.",
            "Ignore Peppy when he gets chased early.",
            "In the warp, don't shoot anything."
        ]
    },
    "Macbeth": {
        "Area 6": [
            "Do not directly attack The Forever Train.",
            "Don't shoot any rocks.",
            "No hovering.",
            "Don't shoot anything but the switches.",
            "Hover into at least two ceilings.",
        ],
        "Bolse": [
            "Ignore wingmen while fighting Mechbeth.",
            "Shoot all 8 switches and ignore the track switcher.",
            "No hovering.",
            "Don't shoot any rocks.",
            "Don't damage the train, other than Mechbeth."
        ]
    },
    "Titania": {
        "Bolse": [
            "No rolling.",
            "No hovering.",
            "Let Goras regenerate at least once.",
            "Don't shoot any rocks."
        ]
    },
    "Sector Z": {
        "Area 6": [
            "Fly into Great Fox at least once.",
            "Bro trash is off-limits.",
            "Let your wingmen last-hit at least one missile (if available).",
            "Let your wingmen last-hit ALL missiles (if available).",
            "Ignore your wingmen entirely.",
            "Make ROB say 'Bracing for impact.' at least once."
        ],
        "Bolse":  [
            "Lose to the first missile.",
            "Lose to the second wave of missiles.",
            "Lose to the last missile.",
            "Fly into Great Fox at least once.",
            "Bro trash is off-limits.",
            "Ignore your wingmen entirely."
        ]
    },
    "Area 6": {
        "Venom2": [
            "Destroy all 5 missiles without using bombs.",
            "Ignore both Great Fox calls.",
            "Ignore Andross' call.",
            "Do not bomb the mines.",
            "Do not save Slippy.",
            "Do not save Peppy.",
            "Do not save Falco.",
            "Do not save any wingmen.",
            "Break no more than one of Gorgon's tentacles per cycle."
        ]
    },
    "Bolse": {
        "Venom": [
            "Destroy the energy towers going counterclockwise.",
            "Do not touch any members of Star Wolf.",
            "Defeat only Star Wolf (if present) and the core.",
            "Attack nothing but the towers and the core."
        ]
    },
    "Venom": [
        f"Maze path: {random.choice(["R", "L"])}, {random.choice(["R", "L"])}, {random.choice(["R", "L"])}, {random.choice(["R", "L"])},",
        "Enter Golemech's temple with both wings broken.",
        "Break at least one wing during Golemech.",
        "Do a somersault during Golemech without damaging yourself.",
        "Let Andross chew on the arwing at least once.",
        "Don't touch or destroy the lasers in Andross' tunnel."
    ],
    "Venom2": [
        "Defeat Pigma first.",
        "Defeat Andrew first.",
        "Defeat Leon first.",
        "Defeat Wolf first.",
        "Kill all available wingmen before attacking Star Wolf.",
        "Let Andross chew on the arwing at least once.",
        "Get the 1-Up.",
        "Take the long tunnel path.",
        "Get grabbed by Andross' brain at least once."
    ]
}
      
print(f"\nIf restrictions conflict, cancel them out and do whatever you want.\n")
print(f"Only take level exits that align with the given route (ex: if level 2 is Meteo, only fight Granga).\n")
for i in range(len(route)-2):
    print(f"================== Level {i + 1} ==================\n")
    print("")
    print(route[i].upper() + " -> " + route[i+1].upper(), f"\n")
    print("* " + set_restriction(restrictions))
    print(f"\nLevel-specific restriction: ", random.choice(level_restrictions[route[i]][route[i+1]] + ["No restrictions."]))
    print("")

print(f"================== Level 7 ==================\n")
print("")
print(f"VENOM\n")
print("* " + set_restriction(restrictions))
print(f"\nLevel-specific restriction: ", random.choice(level_restrictions[level_7] + ["No restrictions."]))
