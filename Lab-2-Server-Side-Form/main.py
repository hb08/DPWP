#!/usr/bin/env python
'''
Harmony Betancourt
Sept 8th 2014
Design Patterns for Web Programming
Simple Form
'''
import webapp2
class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Heading for the page is doctype, header, and opening body tag
        heading = ''' <!DOCTYPE HTML>
        <html>
            <head>

            </head>
            <body>
        '''
        # Declare body, but don't give it an actual variable yet, that is in a function later
        body = ''

        # Closing for body tag, footer, and html
        closer = '''
            </body>
            <footer>

            </footer>
        </html>
        '''
        # Contact Form created
        contact_form = ''' <form>
            <label>Name:</label>
            <input type="text" name="contact" />
            <label>Phone:</label>
            <input type="phone" name="phone" />
            <label>Email:</label
            <input type="email" name="email"/>

            <label>Reason for Contact:</label>
            <select>
                <option value="question" name="reason">Question</option>
                <option value="comment" name="reason">Comment</option>
                <option value="concern" name="reason">Concern</option>
                <option value="personal" name="reason">Personal</option>
            </select>

            <label>Respond By:</label>
            <input type="checkbox" name="contact" value="email">Email<br/>
            <input type="checkbox" name="contact" value="phone">Phone<br/>
            <input type="checkbox" name="contact" value="none">No Response Needed.

            <textarea name="message" placeholder="Your message here" maxlength="1000">

            <textarea>
        </form
        '''
        # If the page has a Get request
        if self.request.GET:
            # Set all the variables
            name = self.request.GET['name']
            phone = self.request.GET['phone']
            email = self.request.GET['email']
            reason = self.request.GET['reason']
            contact = self.request.GET['contact']
            message = self.request.GET['message']
            # Set Body with beginning of message
            body = "Thank you, " + name + ", for your message of " + message + "<br/>We read every message we recieve, and will give yours the consideration it deserves."
            # Add in personalized response
            if contact == "phone":
                body = body + "<br/>We will be in contact by " + contact + " at number " + phone
            elif contact == "email":
                body = body + "<br/>We will be in contact by " + contact + " at email address " + email
        # Otherwise
            else:
            # Show the form
            body = contact_form

        # Print Result Page
        self.response.write(heading + body + closer)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
