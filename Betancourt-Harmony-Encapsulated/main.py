#!/usr/bin/env python
"""
Harmony Betancourt
9/10/14
Design Patterns For Web Programming
Encapsulated Calculator

Description:
This python program is for the Claremont Academy site, or any team based online RPG. It displays a
description of the team itself, shows the members of the team, and upon clicking on their image/name/description it
shows their stats - real name, age, number of missions they have been on, their victories, and the success rate as a
percentage. The success rate is calculated via a getter property. The status is a private variable, with a setter that
can be used to change it from the default of PC for player character, to NPC for non-player characters aka Admin run.
While I used characters and information from the game I currently run myself, this simple site is something I may
implement in the future for the game, and for future games I run.
"""
import webapp2
#import other py files
from layouts import Layout  # Get layout class from layouts.py


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Get Layout from Layout page
        l = Layout()
        # Print Layout to web page
        self.response.write(l.print_layout())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
