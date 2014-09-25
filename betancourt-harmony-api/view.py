""" This class handles how the data from the model is shown to the user """
from model import RgModel
import time  # Will translate epoch format for dob into something readable


class Layout(object):  # Class to create layout
    def __init__(self):
        # Doctype through opening body tag
        self.header = """
<!DOCTYPE HTML>
<html>
    <head>
        <link rel="stylesheet" href="css/style.css">
        <title>Proof Of Concept</title>
    </head>
    <body>
        <div class='wrapper'>
    """

        # Content place holder
        self._content = '''
        '''

        # Close body, html
        self.footer = """
        <footer>
            <p>Created by Harmony 2014&copy;</p>
        </footer>
        </div>
    </body>
</html>
"""

    def page(self):
        return self.header + self.content + self.footer

    @property
    def content(self):  # Getter for Content
        # Add in General header
        gen_header = '''<header>
            <h1>Hello!</h1>
            <h2>My name is...</h2>
        </header>'''
        self._content = gen_header + self._content
        return self._content

    @content.setter  # Setter for content
    def content(self, more):
        self._content = self._content + more  # Content is content plus whatever needs to be added


class IndexPage(Layout):  # Makes a layout object called IndexPage
    def __init__(self):  # Initialize the IndexPage class
        super(IndexPage, self).__init__()  # Initialize the Layout class to inherit
        self.v = RgModel()  # Imported View
        self._form_close = '</form>'  # Form closing tag
        self.__form_content = []  # Private and Protected
        self._form = '<form method="GET">'  # Form opening tag, rest filled in with getter/setter
        self._format_results = ''
        self.intro = '''
        <h3>I'd rather not say...</h3>
        <p>We live in a world where we are constantly asked for personal information, but told not to give it.</p>
        <p>If you want to listen to music, without giving your real address, peruse a dating site, without giving your
        real name and phone number, or even if you are just stuck creating realistic information for fantasy characters,
        this random user generator can help by creating random and fake information needed to help someone in a hurry.
        </p>
        <p>Enter a gender below, or click the button for random fake user information.</p>
        </p>
        '''

    @property
    def form(self):  # Getter for form
        return self._form  # Returns private form

    @property
    def form_content(self):  # Getter for form_content
        return self.__form_content  # Returns private and protected form content

    @form_content.setter
    def form_content(self, arr):
        # Change the private form close variable
        self.__form_content = arr
        for item in arr:  # Prints each array on a line
            self._form += '<input type="' + item[0] + '"'  # Start with input type
            if item[0] == "submit":  # If it's a submit button
                self._form += ' value="' + item[1] + '"'  # Add in the value with text
            else:  # Otherwise check if there are more or less than 3 variables in the item array
                try:  # If possible, put in the placeholder and name
                    self._form += '" placeholder="' + item[2] + '" name="' + item[1]
                except:  # If you can't, add only the name
                    self._form += '" name="' + item[1]
            self._form += '" />'  # Close input
        self._form += self._form_close  # Final form is everything so far with the closing form tag

    @property
    def format_results(self):  # Getter for results
        # Formatting and simplifying
        formatted = "<div class='rg'>"  # Begin formatting
        f_end = "</div>"
        # Add label and break to username
        username = "<p><span>Username:</span> " + self.v.results['us'] + "</p>"
        # Add label, capitalize gender, and add break
        new_gender = "<p><span>Gender:</span> " + self.v.results['g'].capitalize() + "</p>"
        # Add label and break to email
        email = "<p><span>Email:</span> " + self.v.results['e'] + "</p>"
        # DOB now is local readable time
        dob = time.strftime('%B %d %Y', time.localtime(self.v.results['dob']))
        # Add label and break
        bday = "<p><span>Birthday:</span> " + dob + "</p>"
        # Add label and break
        phone = "<p><span>Phone Number:</span> " + self.v.results['p'] + "</p>"
        # Add label and break
        cell = "<p><span>Mobile Number:</span> " + self.v.results['c'] + "</p>"
        # Format image
        image_ready = "<img src='" + self.v.results['i'] + "' alt='Your Pretty Picture' />"
        # Name
        n = "<p class='name'>" + self.v.results['n'] + " </p>"
        # Address
        add = "<p><span>Address:</span> " + self.v.results['a'] + "</p>"

        # Return results
        formatted += n  # Start with Name
        # Add in content in a left div
        formatted += "<div id='left'>" + username + new_gender + email + bday + phone + cell + add + "</div>"
        # Add image into right div and close rg class
        formatted += "<div id='right'>" + image_ready + "</div>" + f_end

        return formatted  # Adds results  to content

    # Override default page
    def page(self):
        p = self.header + self.content
        if self.v.userinput:
            p += self.format_results + self.form
        else:
            p += self.intro + self.form

        p += self.footer
        return p
