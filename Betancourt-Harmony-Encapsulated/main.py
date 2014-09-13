#!/usr/bin/env python
"""
Harmony Betancourt
9/10/14
Design Patterns For Web Programming
Encapsulated Calculator
"""
import webapp2
#import other py files
from layouts import Layout  # Get Char class from chars


class MainHandler(webapp2.RequestHandler):
    def get(self):
        l = Layout()
        self.response.write(l.print_layout())
        #self.response.write(c.raven.name)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
