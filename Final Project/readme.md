# Exercise 3 - Final Project (in progress)

This is the final project for the course where I was required to code an application that can be run from the command line. Using flight data and parameters entered by the user the program would output data in a visualized manner (either a bar graph or map). 

## Visualizations

Two types of visualizations:

**airlines** - A barplot that will show total number of miles each airline had flown on a given day (using plotnine library). This will be output as a png file
**states** - A choropleth map of the U.S. that shows how many flights have departed from each state on a given day(using folium library). this will be output as an html file. 


## Arguments

the program accepts four agruments: 

**visualization**
**date**
**tsvfile**
**outputfile**


## Sample Program Calls 

python flights.py --visualization airlines --date 2019-01-10 -tsvfile flights_visualization.tsv --outputfile image
