__author__ = 'Harmony Betancourt'
'''
    Created for Design Patterns for Web Programming
    Project: Madlib
    Purpose: Create a mad lib that collects user information and populates the output
'''
# Variables for set text in dictionary
messages = {"greeting": "Welcome to the MadLibs Game!", "goodbye": "Thanks for playing!", "start": "It was only ", "two": " days before Halloween when the dead rose from their graves. ", "three": " was prepared. With a ", "four":  " as a weapon.", "five": " With the help of ", "six": "who weilded a hardcover copy of ", "seven": " managed to kill the ", "eight":  "zombies between Full Sail University and the military zone. There were", "nine": " other survivors, all members of the ", "ten": " team. It was going to be a very hard year for ", "eleven": " year old ", "end": ", a very hard year indeed."}

# FUNCTION: Collect User Input in Lists
def getNumbers():
    a =int(raw_input('What is your favorite number?   '))
    b =int(raw_input('How old are you?   '))
    c =int(raw_input('Pick a number between 1 and 20   '))
    return [a, b, c]

def getWords():
    a = str(raw_input('What is your name?   '))
    b = str(raw_input('What item is immediately to your right?   '))
    c = str(raw_input('What is the last book you read?  '))
    d = str(raw_input('Who is your favorite actor?  '))
    e = str(raw_input('What is your favorite sport?   '))
    f = str(raw_input('What is your favorite color?   '))
    together = [a, b, c, d, e, f]
    return together

# FUNCTION: Create New Number
def newNum(age, pick):
    import random
    ran = random.randint(1, 10)
    print ran
    if age>pick:
        return age/ran
    else:
        return pick/ran


# Populate User Input as numbers array and words dictionary
numbers = getNumbers()
newNum(numbers[1], numbers[2])
words = getWords()



# For loop to turn all numbers into strings and extend to words array
for number in numbers:
    a = str(number)
    words.extend(a)

# Favorite Number, Name, favorite color, item, Name, actor, book, added, random number, sport, age, name




















