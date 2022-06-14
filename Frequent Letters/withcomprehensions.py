#using comprehensions 
s =str(input("Please type a sentence here and I will give you the 3 most frequent letters:"))

top3= [t[1] for t in sorted([(frequency, moji) for moji, frequency in {moji: s.count(moji) for moji in s if moji != " "}.items()], reverse=True)[:3]]

print("The three most common characters are {} {} and {}" .format(top3[0],top3[1],top3[2]))
