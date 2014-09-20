#!/usr/bin/env python
"""
Harmony Betancourt
9/19/14
Design Patterns For Web Programming
Proof Of Concept

Description:
Utilizes the Random User Generator Api from randomuser.me
"""
import webapp2
from layout import Layout

class MainHandler(webapp2.RequestHandler):
    def get(self):
        l = Layout()
        self.response.write(l.page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
