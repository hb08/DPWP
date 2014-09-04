#one lined comments
'''
Doc strings should label all functions
'''

# User Input --------------------------------------------------------
'''
response = raw_input("Enter your name   ")
print "Hello",response
'''

# Concat --------------------------------------------------------
'''
#birth_year = 1987
#current_year = 2014
#age = current_year - birth_year
#print "You are " + str(age) + " years old"
## int(var) to make variable an integer
'''

# Ifs --------------------------------------------------------
'''
#if age > 30: # Condition begins after if and ends at colon
   # print "And you look good!"
#elif age > 25:
   # print "You're amazing!"
#else:
   # pass # Can never leave empty, must have something indented after any if/elif/else! Use pass
'''

# Arrays --------------------------------------------------------
'''
#pets = ["Chester", "Leona", "Kaiju", "Hugh"]
#print "I have a dog named " + pets[0]
'''
# Dictionary (Associated Array)
'''
#family = dict() #create dictionary
#family = {"Mom":"Melody", "Dad":"BC", "Brother":"Brent", "Husband":"John"}
#print "My dad is " + family["Dad"]
'''


# Loops --------------------------------------------------------

# While
'''
#i = 0
#while i<9:
#    print "The count is", i+1
#    i +=1
'''
# For
'''
#for i in range(0,9):
#    print "The count is", i+1
#    i +=1
'''
# For Each
'''
bands = ["Placebo", "Portishead", "Ludo"]
for b in bands:
    print "I love the band",b
'''

# Functions --------------------------------------------------------
'''
def calcArea(h,w):
    area = h * w # Can never leave empty, must have something indented after def, use pass
    return area

a = calcArea(20,40)
print "The area is " + str(a) + "ft^2"
'''

# Variable Manipulation --------------------------------------------------------
weight = 118
height = 64
message = '''
Your height is {height} and your weight is {weight}
'''
message = message.format(**locals()) # Formats with the locals method, which looks inside ''' and the {} with variable names
print message
