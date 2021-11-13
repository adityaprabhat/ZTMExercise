from random import randint
import sys

while True:
    lower,upper = int(sys.argv[1]), int(sys.argv[2])
    number = randint(lower,upper)
    # print(number)
    try:
        user_input = int(input("Please enter a number between 1 and 10: "))
        if(number == user_input):
            print("Congrats!!!!!")
            break
    except ValueError:
        print("Please enter a number")
    

        
    