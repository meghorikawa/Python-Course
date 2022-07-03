import argparse

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

import pandas as pd

#open tsv file


dataframe = pd.read_csv('flights.tsv',sep = '\t') 
dataframe.head(5)
