#create a program that will take an input string and character, c and count how frequent that character appears in the string.
s = input("Enter string: ")
c = input("Enter character: ")
s=s.lower()
character_count={}

for x in s: 
    if x not in character_count:
        character_count[x]= 1
    else:
        character_count[x]=character_count[x]+1
        
print(f"The character occurs {character_count.get(c)} times.")       
                