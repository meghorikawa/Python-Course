# Exercise 2 Readme

This is an applicaton that is run in the command line. It uses pandas to filter flight information to calculate the average/max, distance/delays depending on the parameters.

## Basic Functions:

**statistic:** Which measure do you want to computer? Maximum value (max) or average (avg)

**Variable:** flight distance in miles (distance) or delay (arrival delay in minutes.

**tsvfile:** This defines the filename or filepath for the TSV file containing the dataset "flights.tsv"

## Optional Data Filters

**--carrier:** This argument contains the two digit airline carrier code

**--origin:** This argument defines the departure airport with the 3 digit airport code

**--date:** This argument is used to filter flights based on their departure date. The program is able to process both ISO compatible (YYYY-MM-DD) and German equivalient (DD.MM.YYYY)

## A sample call is as follows:

python flightspy.py --carrier DL --origin LAX --date 2019-01-03 max delay flights.tsv

**output:** 191
