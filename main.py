# KFC Chat Bot
# Programmer - Martin Rozik
# Chat bot that takes customers order for KFC Botany Downs

#Import library random
import random
#import random integer
from random import randint

#list of names used by BOT
bot_names = ["Mark", "Pheobe", "Sally", "Micheal", "Denise",
             "Ellen", "Eric", "Moana", "Lewis", "Lara"]

def welcome ():
    num = randint (0,9)
    name = (bot_names[num])
    print("*** Welcome to Dream Pizza ***")
    print("*** My name is", name, "***")
    print("*** I will be here to help you order your delicious Dream Pizza ***")










def main():
    welcome()


main()