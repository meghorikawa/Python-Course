def collatz_function(number):
    while number != 1: #to make sure the code doesn't get stuck in an endless loop
        if number % 2 == 0: #even number
            number=number//2
        else: #odd numbers
            number=(number*3)+1
        print(number)

collatz_function(10)