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

        # Print Result Page
        self.response.write(site.print_page)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
