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
    """

        # Content place holder
        self._content = '''
        '''

        # Close body, html
        self.footer = """
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
        print self._format_results

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
        for item in arr:  # Prints each array on a line | type, name, placeholder, submit first
            self._form += '<input type="' + item[0] + '" name="' + item[1]
            # Just in case there are more or less than 3 variables in the item array
            try:  # Check for the ability to put in the placeholder item
                self._form += '" placeholder="' + item[2] + '" />'  # If possible, put in the placeholder and close
            except:  # If you can't, end it now
                self._form += '" />'
        self._form += self._form_close  # Final form is everything so far with the closing form tag
        self.content = self.form  # Adds full form to content

    @property
    def format_results(self):  # Getter for results
        # Formatting and simplifying
        formatted = "<div class='rg'>"  # Begin formatting
        f_end = "</div>"
        username = "Username: " + self.v.results['us'] + "<br/>"  # Add label and break
        new_gender = "Gender: " + self.v.results['g'].capitalize() + "<br/>"  # Add label, capitalize, and break
        email = "Email: " + self.v.results['e'] + "<br/>"  # Add label and break
        dob = time.strftime('%B %d %Y', time.localtime(self.v.results['dob']))  # DOB now is local readable time
        bday = "Birthday: " + dob + "<br/>"  # Add label and break
        phone = "Phone Number: " + self.v.results['p'] + "<br/>"  # Add label and break
        cell = "Mobile Number: " + self.v.results['c'] + "<br/>"  # Add label and break
        image_ready = '<img src="' + self.v.results['i'] + '" alt="Your Pretty Picture" /><br/>'  # format image

        # Return results
        formatted += image_ready + new_gender + username + bday + email + phone + cell + self.v.results['a'] + f_end
        return formatted

    # Override default page
    def page(self):
        # Add in form and results
        return self.header + self.content + self.format_results + self.footer
