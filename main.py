# KFC Chat Bot
# Programmer - Martin Rozik
# Chat bot that takes customers order for KFC Botany Downs

#Import library random
import random
#import random integer
from random import randint

#list of names used by BOT
bot_names = ["Joshua", "Makee", "Gabby", "Catherine", "Jake",
             "Micheal", "John", "Gareth", "Sione", "Keola"]



# Constant variables for low and high number for menus
LOW = 1 
HIGH = 2 

# Function validates integers
# Takes parameters of low and high numbers and question
# While loop until correct input is recived then returns inout to original function
# Input must be integer between low and high parameters
# Value error results in error message and new input request
def integer_validation(low, high, question):
    while True:
        try:    
            num =int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print("This is not a valid number, please enter 1 or 2")
        except ValueError:    
            print("That is not a valid number, please enter 1 or 2")
            (f"Please enter {LOW} or {HIGH}: ")


def welcome ():
    num = randint (0,9)
    name = (bot_names[num])
    print("*** Welcome to KFC ***")
    print("*** My name is", name, "***")
    print("*** I will be here to assist you order any of your Finger licking needs ***")
    
# Function allowing users to choose either click and collect or delivery
# Input request sent to integer_validation function for validation
# Valid input is returned and sent to if statements for appropriate action

def pickup_delivery():
    del_pick = ""
    print("Would you like click and collect or delivery?")
    question = (f"Please enter {LOW} or {HIGH}: ")
    print("Enter 1 for click and collect")
    print("Enter 2 for delivery")
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        print("Click and collect")
    elif del_pick == 2:
        print("Delivery")






def main():
    welcome()
    pickup_delivery()


main()