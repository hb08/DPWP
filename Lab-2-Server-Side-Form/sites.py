class Site(object):
    def __init__(self):
        self.title = "Contact Us!"
        self.css = "css/style.css"
        # Heading for the page is doctype, header, and opening body tag
        self.header = """
        <!DOCTYPE HTML>
            <html>
             <head>
                 <title>{self.title}</title>
                <link href="{self.css}" rel="Stylesheet" type="text/css" />
             </head>
             <body>"""
        # Declare body, but don't give it an actual variable yet, that is in a function later
        self.body = " "

        # Closing for body tag, footer, and html
        self.closer = """
            </body>
            <footer>

            </footer>
        </html>"""

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
            b = "Thank you, " + contact + ", for your " + " message of <span>'" + message + "'</span> " + thanks
            # Add in personalized response
            if contact == "phone":
                self.body = b + "<br/>We will be in contact by " + response + " at number " + phone
            elif contact == "email":
                self.body = b + "<br/>We will be in contact by " + response + " at email address " + email
        # Otherwise
        else:
            # Show the form
            self.body = self.contact_form

        # Contact Form created
            self.contact_form = """ <form>
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
            </form>"""

    def print_page(self):
        site = self.header + self.body + self.closer
        site = site.format(**locals())
        return site