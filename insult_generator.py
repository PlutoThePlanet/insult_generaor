from random import choice
import time

#lists
adjectives = ['wet', 'big', 'dumb', 'stinky', 'lazy']
nouns = ['turnip', 'dog', 'goat', 'monke', 'booger']

#functions
def printInsult (name, age):
    print (name + ', you are a ' + age + ' ' + choice(adjectives) + ' ' + choice(nouns))
    

#program
name = input('What is your name?')
if name == 'paige':
    print('ඞ ඞ ඞ')
    quit()

age = input('How old are you?')
if (age < 16):
    age = 'young'
else:
    age = 'old'

choice = input('1: print insults at your demand\n 2: print insults endlessly\n 0: exit')
if(choice == 1):
    printInsult(name, age)
    cont = input('Can you handle more (y/n)')
    while cont != 'n':
        printInsult(name, age)
        cont = input('Can you handle more (y/n)')
    quit()
elif(choice == 2):
    while choice == 2:
        printInsult(name, age)
        time.sleep(3)
elif(choice == 0):
    quit()
else:
    print('not an option, try again')