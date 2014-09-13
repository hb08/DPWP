# Data Objects

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

        vijana = Character()
        vijana.name = "Vijana Ravana Romana"
        vijana.power = "Psychic Werewolf"
        vijana.age = 17
        vijana.code_name = "Atlanta"

        august = Character()
        august.name = "August Romano"
        august.power = "Werewolf"
        august.age = 82
        august.code_name = "Lupo"

        ash = Character()
        ash.name = "Ash McNeil"
        ash.power = "Thermokinesis"
        ash.age = 15
        ash.code_name = "Skadi"

        chars = [vijana, august, ash]
        print chars[0].power

class Character(object):
    def __init__(self):  # Constructor function, always needed
        self.name = ""
        self.power = ""
        self.age = 0
        self.code_name = ""

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
