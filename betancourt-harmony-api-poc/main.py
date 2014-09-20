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


class MainHandler(webapp2.RequestHandler):
    def get(self):
        test = '''
<!DOCTYPE HTML>
<html>
    <head>
        <link rel="stylesheet" href="css/style.css">
        <title>Proof Of Concept</title>
    </head>
    <body>
        <img src="img/floating.jpg" alt="YAML Fail" />
    </body>
</html>
'''
        self.response.write(test)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
