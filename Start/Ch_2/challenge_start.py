# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import os.path

# open the data file and load the JSON
with open(os.path.dirname(__file__) +'/'+"../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
