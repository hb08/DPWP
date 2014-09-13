#!/usr/bin/env python
'''
name
date
class
assignment
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
