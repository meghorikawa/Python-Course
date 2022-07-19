import argparse
from ast import Pass
from datetime import date, datetime
from re import A
from sqlite3 import Date
from time import strptime
import pandas as pd
import os

# Parsing arguments. You must not modify these lines!
parser = argparse.ArgumentParser()
parser.add_argument("statistic", choices=["avg", "max"], help="Which statistic should be run?")
parser.add_argument("variable", choices=["distance", "delay"], help="What variable should be used for the calculation?")
parser.add_argument("tsvfile", help="Name of data file to be analyzed")
parser.add_argument("--carrier", dest="carrier", help="Comma-separated list of airline codes for those airlines whose flights should be included")
parser.add_argument("--date", dest="date", help="Departure dates for flights to be included")
parser.add_argument("--origin", dest="origin", help="Departure dates for flights to be included")
args = parser.parse_args()

# Start here with the rest of the program....

#variables for arguments
stat = args.statistic
var = args.variable
airline = args.carrier
departure = args.date
origin = args.origin
file = args.tsvfile

#error and termination if file doesn't exist
if os.path.isfile(file) == False:
    print("ERROR_INVALID_FILE")
    exit()

#open tsv file 'flights.tsv'
dataframe = pd.read_csv(file,sep = '\t') 
#replace the negative values for delays with 0 
dataframe["DEPARTURE_DELAY"] = dataframe["DEPARTURE_DELAY"].mask(dataframe["DEPARTURE_DELAY"] < 0, 0)


#convert date input into a time object with formats YYYY-MM-DD or DD.MM.YYYY
if departure is not None:
    for x in departure:
        if departure.find('.') == 2:
            departure2 = datetime.strptime(departure, "%d.%m.%Y")
            c =  (dataframe["DEPARTURE_DAY"] == departure2.day) & (dataframe["DEPARTURE_MONTH"] == departure2.month) & (dataframe["DEPARTURE_YEAR"] == departure2.year)
        if departure.find('-') == 4:
            departure2 = datetime.strptime(departure, "%Y-%m-%d")
            c =  (dataframe["DEPARTURE_DAY"] == departure2.day) & (dataframe["DEPARTURE_MONTH"] == departure2.month) & (dataframe["DEPARTURE_YEAR"] == departure2.year)
        else:
            print("ERROR_INVALID_DATE")
            exit()

#list of airline carriers
airline_carriers = dataframe["CARRIER"].unique().tolist()

#list of origin airports
airports = dataframe["ORIGIN"].unique().tolist()

#NO_MATCHING_FLIGHTS error setup. 
if airline is not None or origin is not None: 
    if airline not in airline_carriers or origin not in airports:
        print("NO_MATCHING_FLIGHTS")
        exit()

#replace the variable entry to correspond to the correct column on the dataframe.
if var == "distance":
    var = "DISTANCE"
if var == "delay":
    var = "DEPARTURE_DELAY"

#variables to filter dataframe
a = (dataframe["CARRIER"] == airline)
b = (dataframe["ORIGIN"] == origin)

#conditional statements to filter the dataframe based on conditional input
if airline is not None and origin is not None and departure is not None:
    filteredDF = dataframe[a & b & c]
if airline is not None and origin is None and departure is None:    
    filteredDF = dataframe[a]
if airline is None and origin is not None and departure is None:    
    filteredDF = dataframe[b]
if airline is None and origin is None and departure is not None:    
    filteredDF = dataframe[c]
if airline is not None and origin is not None and departure is None:    
    filteredDF = dataframe[a & b]
if airline is not None and origin is None and departure is not None:    
    filteredDF = dataframe[a & c]
if airline is None and origin is not None and departure is not None:    
    filteredDF = dataframe[b & c]
if airline is None and origin is None and departure is None:
    filteredDF = dataframe

#need another if statement so that the final calculation can be made and printed
if stat == "avg":
    answer = round((filteredDF[var].mean()), 1)
    print(answer)
if stat == "max":
    answer = filteredDF[var].max()
    print(answer)
