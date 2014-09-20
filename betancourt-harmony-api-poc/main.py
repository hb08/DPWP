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
from layout import IndexPage


class MainHandler(webapp2.RequestHandler):
    def get(self):
        i = IndexPage()
        # Send an array full of arrays to the input setter | type, name, placeholder, submit first
        i.form_content = [['submit', 'Submit'], ['text', 'gender', 'Gender']]
        if self.request.GET:
            i.userinput = self.request.GET['gender']
            i.results = i.userinput

        self.response.write(i.page())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
