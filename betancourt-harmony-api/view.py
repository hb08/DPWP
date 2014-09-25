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
        <p>Enter a gender below, then the button for random fake user information.</p>
        </p>
        '''
        self.error = "<p class='error'>Please enter a gender before hitting the button!</p>"

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
        arr.append(['submit', 'Who Am I?'])
        for item in arr:  # Prints each array on a line
            self._form += '<input type="' + item[0] + '" value="' + item[1] + '"'  # Start with input type and value
            try:  # If possible, put in the Name and close input
                self._form += ' name="' + item[2] + '" />'
                self._form += '<label for="' + item[1] + '">' + item[1].capitalize() + '</label>'
            except:  # If you can't, add only close input
                self._form += ' />'  # Close input
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
        # Format image with labels and alt
        image_ready = "<img src='" + self.v.results['i'] + "' alt='Your Pretty Picture' />"
        # Format name with special paragraph class for css
        n = "<p class='name'>" + self.v.results['n'] + " </p>"
        # Format Address
        add = "<p><span>Address:</span> " + self.v.results['a'] + "</p>"

        # Return results
        formatted += n  # Start with Name
        # Add in content in a left div
        formatted += "<div id='left'>" + image_ready + "</div>"
        # Add contents into right div and close rg class
        formatted += "<div id='right'>" + username + new_gender + email + bday + phone + cell + add + "</div>" + f_end

        # Adds results  to content
        return formatted

    # Override default page
    def page(self):
        # P contains what will be printed, so far header and content
        p = self.header + self.content
        if self.v.userinput:  # If there is user input
            if self.v.userinput == "None":  # If the user didn't put in a gender
                p += self.intro + self.error + self.form
            else:
                p += self.format_results + self.form  # Add in form results and form
        else:  # If there is no input, just put in the form
            p += self.intro + self.form
        # Always add the footer to the end
        p += self.footer
        # Return final product
        return p
