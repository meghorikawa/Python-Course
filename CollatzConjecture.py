x=input()
x = int(x)
while x != 1: #to make sure the code doesn't get stuck in an endless loop
    if x % 2 == 0: #even number
        x=x//2
        print(x)
    else: #odd numbers
        x=(x*3)+1
        print(x)
print("The End!")