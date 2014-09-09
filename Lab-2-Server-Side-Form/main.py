#!/usr/bin/env python
'''
Harmony Betancourt
Sept 8th 2014
Design Patterns for Web Programming
Simple Form
'''
import webapp2
from sites import Site


class MainHandler(webapp2.RequestHandler):
    def get(self):
        site = Site()

        # If the page has a Get request
        if self.request.GET:
            # Set all the variables to user inputs
            contact = self.request.GET['contact']
            phone = self.request.GET['phone']
            response = self.request.GET['response']
            email = self.request.GET['email']
            message = self.request.GET['message']

            # Messages to Print
            thanks = "<br/>We read every message we receive, and will give yours the consideration it deserves."
            # Set Body with beginning of message
            b = "Thank you, " + contact + ", for your " + " message of <span>'" + message + "'</span> " + thanks
            site.body = b + "<br/>We will be in contact by " + response
            # Add in personalized response
            if response == "phone":
                site.body += " at number " + phone
            elif response == "email":
                site.body += " at email address " + email
        # Otherwise
        else:
            # Show the form
            site.body = site.contact_form

        # Print Result Page
        self.response.write(site.header + site.body + site.closer)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
