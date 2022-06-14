#This was an exercise for my class that didn't allow the use of any of the sort functions of python or any packages or comprehensions. 
s = input("Please input your sentence here to count the 2 most common letters")
#we need to make all letters lowercase
s=s.lower()
#delete spaces
s=s.replace(" ","")
#delete punctuation
s=s.replace("!","")
s=s.replace(".","") 

#create variables to store the 3 most freq values
num_1 = 3
ltr_1 = " "
num_2 = 2
ltr_2 = " "
num_3 = 1
ltr_3 = " "


#use loop to go through string and find the 3 most common characters.
for character in s:
    if s.count(character) >= num_1:
        num_1 = s.count(character)
        ltr_1 = character
    if s.count(character) < num_1 and s.count(character) >= num_2:
        num_2 = s.count(character)
        ltr_2 = character
    if s.count(character) < num_2 and s.count(character) >= num_3:
        num_3 = s.count(character)
        ltr_3 = character
        
print(f"The three most common characters are {ltr_1}:{num_1}, {ltr_2}:{num_2}, and {ltr_3}:{num_3}. ")
