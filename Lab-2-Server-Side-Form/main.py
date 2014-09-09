#!/usr/bin/env python
'''
Harmony Betancourt
Sept 8th 2014
Design Patterns for Web Programming
Simple Form
'''
import webapp2
from template import Site

class MainHandler(webapp2.RequestHandler):
    def get(self):

        # Contact Form created
        contact_form = ''' <form>
            <label>Name:</label>
            <input type="text" name="contact" />
            <label>Phone:</label>
            <input type="phone" name="phone" />
            <label>Email:</label>
            <input type="text" name="email" />

            <label>Reason for Contact:</label>
            <select name="reason">
                <option value="question">Question</option>
                <option value="comment">Comment</option>
                <option value="concern">Concern</option>
                <option value="personal">Personal</option>
            </select>

            <label>Respond By:</label>
            <input type="checkbox" name="response" value="email"/>Email<br/>
            <input type="checkbox" name="response" value="phone"/>Phone<br/>
            <input type="checkbox" name="response" value="none"/>No Response Needed.

            <textarea name="message" placeholder="Type here" maxlength="1000"> </textarea>
            <input type="submit" value="Submit"/>
        </form>
        '''
        # If the page has a Get request
        if self.request.GET:
            # Set all the variables to user inputs
            contact = self.request.GET['contact']
            phone = self.request.GET['phone']
            response = self.request.GET['response']
            email = self.request.GET['email']
            message = self.request.GET['message']
            # As a Select, Reason needs to be put into an if statement
            reason = self.request.get_all('reason')
            for r in reason:
                print r
            # Messages to Print
            thanks = "<br/>We read every message we recieve, and will give yours the consideration it deserves."
            # Set Body with beginning of message
            body = "Thank you, " + contact + ", for your " + " message of <span>'" + message + "'</span> " + thanks
            # Add in personalized response
            if contact == "phone":
                body = body + "<br/>We will be in contact by " + response + " at number " + phone
            elif contact == "email":
                body = body + "<br/>We will be in contact by " + response + " at email address " + email
        # Otherwise
        else:
            # Show the form
            body = contact_form

        # Print Result Page
        self.response.write(heading + body + closer)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
