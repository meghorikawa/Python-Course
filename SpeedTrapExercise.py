from numpy import append

#Write a program that creates and outputs a dictionary where counties are used as keys and the values
#are the average speeds of the vehicles from this county.
#Here is a sample of what the output should look like if you only used the entries from dictionary
#speed_trap :
#{"TÜ": 39.25, "RT": 41.5, "K": 51.0, "LEO": 40.0}

speed_trap = [
{"time": "12:43:17", "speed": 37, "license_plate": "TÜ-TL1234"},
{"time": "12:44:01", "speed": 35, "license_plate": "TÜ-FL999"},
{"time": "12:44:57", "speed": 45, "license_plate": "RT-ZZ321"},
{"time": "12:47:13", "speed": 51, "license_plate": "K-FC48"},
{"time": "12:44:57", "speed": 38, "license_plate": "RT-R777"},
{"time": "12:51:01", "speed": 42, "license_plate": "TÜ-XY1"},
{"time": "12:51:29", "speed": 40, "license_plate": "LEO-Z4"},
{"time": "12:54:00", "speed": 43, "license_plate": "TÜ-AB656"},
# and many more
]

#results dictionary
result = {}

#we need to go through the dictionary 
for vehicle in speed_trap:
    #find the county and append into list. 
    i=vehicle["license_plate"].index("-")
    #use slicing to save the county abreheviation 
    county=vehicle["license_plate"][0:i]
    #need to set a variable to consider speed
    speed=vehicle["speed"]
    #make sure to save the county abrevehations into a list
    if county in result.keys():
        #add speed to existing list
        result[county].append(speed)
    else:
        #append dictionary
        result[county]=[speed]

#Last thing to do is replace lists with their average values.
for county, speeds in result.items():
    result[county] = sum(speeds)/len(speeds)

#complete
print(result)