#!/usr/bin/env python
"""
Harmony Betancourt
9/19/14
Design Patterns For Web Programming
Proof Of Concept

Description:
Utilizes the Random User Generator Api from randomuser.me as a continuation of the API assignment
MVC Formatting Used
"""
import webapp2
from view import IndexPage  # Import from View


class MainHandler(webapp2.RequestHandler):
    """ Serves as Controller class """
    def get(self):
        i = IndexPage()
        # Send an array full of arrays to the input setter | type, name, placeholder, submit first
        i.form_content = [['submit', 'submit'], ['text', 'gender', 'Gender']]
        # If the user submits imput
        if self.request.GET:
            i.v.userinput = self.request.GET['gender']  # Set gender
            i.v.results = i.v.userinput  # Set results with gender
        # Print out the page for all to see
        self.response.write(i.page())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
