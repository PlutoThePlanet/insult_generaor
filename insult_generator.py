from random import choice

#lists
adjectives = ['wet', 'big']
nouns = ['turnip', 'dog']

#user input
name = input('What is your name?')
print ('Hello ' + name)

age = input('How old are you?')
if (age < 16):
    print ('young')
else:
    print ('old')


#functions
def printInsult (name, age):
    count = 0
    if (count == 0):
        print (name + ', you are a ' + age + ' ' + choice(adjectives) + ' ' + choice(nouns))
        count+1
    else:
        userAnswer = input('can you take any more?')
        while (userAnswer != 'no'):
            print (name + ', you are a ' + age + ' ' + choice(adjectives) + ' ' + choice(nouns))


#print insult(s)
printInsult(name, age)