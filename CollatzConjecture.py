#This is an exercise done for my intro to programming course. The idea is to design a program that uses the Collatz Conjecture. It operates in the following way:
#You pick any natural number greater than 0, you will alternate between the following two steps. if the number is even you will divide by 2 if the number is odd you will multiply it by 3 then add 1
#No matter which number you start with the final 3 numbers output will be 4, 2, 1
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
