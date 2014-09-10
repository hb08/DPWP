#!/usr/bin/env python
'''
Harmony Betancourt
Sept 8th 2014
Design Patterns for Web Programming
Simple Form
'''
import webapp2
from sites import Site  # Import everything from sites.py


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Everything in sites.py is saved as site variable
        site = Site()

        # If the page has a Get request
        if self.request.GET:
            # Set all the variables to user inputs
            contact = self.request.GET['contact']  # User name
            phone = self.request.GET['phone']  # User phone
            response = self.request.GET['response']  # User response method
            reason = self.request.GET['reason']  # User reason for message
            email = self.request.GET['email']  # User email
            message = self.request.GET['message']  # User message

            # Build site body by concat preset text and user input. To avoid length error, break into two portions
            site.body = site.text["thanks_head"] + contact + site.text["thanks_start"] + reason  # Intro through reason
            site.body += site.text["thanks_mes"] + message + site.text["thanks_close"]  # Message through closing span
            # Add in personalized response
            if response == "phone":
                # If the response method is phone, then put in number to verify and link a small COA
                site.body += site.text["appr"] + site.text["con"] + phone + "</p>" + site.text["link"]
            elif response == "email":
                # If the response method is email, then put in address to verify and link a small COA
                site.body += site.text["appr"] + site.text["con"] + email + "</p>" + site.text["link"]
            else:
                # If the response method is none, then don't just appreciate and link a small COA
                site.body += site.text["appr"] + "</p>" + site.text["link"]
        # Otherwise if this is a new page
        else:
            # Show the form
            site.body = site.contact_form

        # Print full page to browser
        self.response.write(site.header + site.body_start + site.body + site.closer)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
