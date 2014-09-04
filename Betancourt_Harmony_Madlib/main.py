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
    c =int(raw_input('Pick a number between 1 and 20   '))
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

# Create a fourth number
if numbers[1]>numbers[2]:
    numbers.append(numbers[1] + numbers[2])
else:
    numbers.append(numbers[0] + numbers[1])

# Function to put it all together
def createML(numbers, words):
    message = '''
        "Hello, my name is {words.name}, and I never leave the house without my {words.item}. Let me tell you exactly why. I was walking to bookclub. I'd already skipped it {numbers[0]} times, but that night we were talking about {words.book}! I was in a hurry, and ran into {words.actor}! I was just about to ask for a picture, when a riot broke down after the local {words.sport} team lost! {words.actor} and I were torn apart by the crowd. That's when I saw it! A {words.color} {words.item}. I quickly grabbed the {words.color} {words.item}, spun it over my head {numbers[2]} times, and threw it. Like magic, it landed at the feet of {words.actor}. Never in my {numbers[1]} years of life did I expect that {words.actor} would sign it, then crowdsurf the rioting {words.sport} fans to deliver it to me. We fell in love amidst the chaos, and that, children, is how I met {words.actor}, and we've been happily married for the past {numbers[3]} years."
    '''
    message = message.format(**locals())
    return message

madlib = createML(numbers, words)

print madlib













