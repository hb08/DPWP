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
            reason = self.request.GET['reason']
            email = self.request.GET['email']
            message = self.request.GET['message']

            # Messages to Print
            # Build site body by concat pre set text and user input
            site.body = site.text["thanks_head"] + contact + site.text["thanks_start"] + reason
            site.body += site.text["thanks_mes"] + message + site.text["thanks_close"]
            # Add in personalized response
            if response == "phone":
                site.body += site.text["appr"] + site.text["con"] + phone + "</p>" + site.text["link"]
            elif response == "email":
                site.body += site.text["appr"] + site.text["con"] + email + "</p>" + site.text["link"]
            else:
                site.body += site.text["appr"] + "</p>" + site.text["link"]
        # Otherwise if this is a new page
        else:
            # Show the form
            site.body = site.contact_form

        # Print full page to browser
        self.response.write(site.header + site.body_start + site.body + site.closer)
        test = self.request.get_all('reason')
        print test

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
