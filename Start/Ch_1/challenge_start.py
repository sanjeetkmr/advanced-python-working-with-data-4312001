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
        return q

        
def getSig(q):
    signi = q["properties"]["sig"]
    if signi is None:
        return 0
    else:       
        return int(signi)


maxnoquake =  list(filter(isQuake, data["features"]))
print(f"Total quakes: {len(maxnoquake)}")

#Print total quake felt by at least 100 people
feltquake  = list(filter(getFelt100, data["features"]))
print(f"Total quakes felt by at least 100 people: {len(feltquake)}")

# Print most felt report events
most_felt = max(data["features"], key=getSig )
print(f"Most felt reports : M {most_felt['properties']['sig']} - {most_felt['properties']['place']}")

print("The 10 most significant events were:")
# print 10 most significant event
data["features"].sort(key=getSig, reverse=True)
for i in range (0,10):
    print(f"""Event : {data['features'][i]['properties']['title']} Significance {data['features'][i]['properties']['sig']} : {data['features'][i]['properties']['felt']}""")