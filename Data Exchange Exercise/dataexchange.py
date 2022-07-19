import json

with open("players.json", "r")as file:
    playerdata = json.load(file)
print(playerdata)

tw_names = []

#add the goalies to the list
for player in playerdata:
    if player["position"] =="TW":
        tw_names.append(player["name"])

# remove duplicates in the list by converting to set, this will also order the set
tw_names = set(tw_names)

for name in sorted(tw_names):
    print(name)
