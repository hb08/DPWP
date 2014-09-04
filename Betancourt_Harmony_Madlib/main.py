__author__ = 'Harmony Betancourt'
'''
    Created for Design Patterns for Web Programming
    Project: Madlib
    Purpose: Create a mad lib that collects user information and populates the output
'''
# Begin with welcome
print "Welcome to the Madlib Game.\nLet's get started!"

# Functions to Collect Information
def getNumbers():
    a =int(raw_input('What is your favorite number?   '))
    b =int(raw_input('How old are you?   '))
    c =int(raw_input('Pick a number between 1 and 100   '))
    return [a,b,c]

def getWords():
    a = str(raw_input('What is your name?   '))
    b = str(raw_input('What item is immediately to your right?   '))
    c = str(raw_input('What is the last book you read?  '))
    d = str(raw_input('Who is your favorite actor?  '))
    e = str(raw_input('What is your favorite sport?   '))
    f = str(raw_input('What is your favorite color?   '))
    return {"name": a, "item": b, "book": c, "actor": d, "sport": e, "color": f}

# Populate User Input as numbers array and words dictionary
numbers = getNumbers()
words = getWords()












