# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json
import os.path



# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open(os.path.dirname(__file__) +'/'+"../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
    
def isQuake(q):
    if q["properties"]["type"] == "earthquake":
        return True
    return False

def getFelt100(q):
    if q["properties"]["felt"] is not None and q["properties"]["felt"] >= 100:
        return True
    return False
        
def getSig(q):
    if q["properties"]["sig"] == "none":
        return 0
    return int(q["properties"]["sig"])



maxnoquake =  list(filter(isQuake, data["features"]))
print(len(maxnoquake))
for i in range (1, 5):
    print(maxnoquake[i]["properties"]["gap"])


#Print total quake felt by at least 100 people
feltquake  = list(filter(getFelt100, data["features"]))
print(len(feltquake))

print("Printing 10 most sig")
# print 10 most significant event
data["features"].sort(key=getSig, reverse=True)
for i in range (0,10):
    print(data["features"][i]["properties"]["sig"])