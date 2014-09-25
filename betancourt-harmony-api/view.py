""" This class handles how the data from the model is shown to the user """
from model import RgModel  # Import RGModel from model page
import time  # Will translate epoch format for dob into something readable, spoke to instructor before POC submitted


# ABSTRACT CLASS - USED TO CREATE ALL LAYOUTS
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

    def page(self):  # When called, return header, content, and footer
        return self.header + self.content + self.footer

    @property
    def content(self):  # Getter for Content
        # Add in General header
        gen_header = '''<header>
            <h1>Hello!</h1>
            <h2>My name is...</h2>
        </header>'''
        self._content = gen_header + self._content  # When called on, gets general page header plus content to follow
        return self._content  # Returns newly compiled content

    @content.setter  # Setter for content
    def content(self, more):
        self._content = self._content + more  # Content is content plus whatever needs to be added


class IndexPage(Layout):  # Makes a layout object called IndexPage
    def __init__(self):  # Initialize the IndexPage class
        super(IndexPage, self).__init__()  # Initialize the Layout class INHERITS FROM LAYOUT ABSTRACT CLASS
        self.v = RgModel()  # Imported Model
        self.__form_content = []  # Private and Protected
        self._form = '<form method="GET">'  # Form opening tag, rest filled in with getter/setter
        self._format_results = ''  # Protected and formatted results, filled in by setter

        # Form closing tag and reminder
        self._form_close = '''<p class="error">Remember to select a gender!</p>
        </form>
        '''
        # Intro info for main page
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
        # Error for special cases where form setup allows invalid info
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
        arr.append(['submit', 'Who Am I?'])  # Add in the submit button after rest of data is sent by main page
        for item in arr:  # Prints each array on a line
            new = '<input type="' + item[0] + '" value="' + item[1] + '"'  # Start with input type and value
            try:  # If possible, put in the name, and close input
                new += ' name="' + item[2] + '"' + ' id="' + item[1] + '" />'
                # Add in label around input to create a clickable label
                new = '<label for="' + item[1] + '">' + new + item[1].capitalize() + '</label>'
                self._form += new
            except:  # If you can't, add only close input
                self._form += new + ' />'  # Close input
        self._form += self._form_close  # Final form is everything so far with the closing form tag

    @property
    def format_results(self):  # Getter for results
        # Formatting and simplifying
        formatted = "<div class='rg'>"  # Begin formatting
        f_end = "</div>"  # End of div.rg

        # Add label span and break to username
        username = "<p class='rgl'>Username:</p><p> " + self.v.results['us'] + "</p>"
        # Add label span, capitalize gender, and add break
        new_gender = "<p class='rgl'>Gender:</p><p> " + self.v.results['g'].capitalize() + "</p>"
        # Add label span and break to email
        email = "<p class='rgl'>Email:</p><p> " + self.v.results['e'] + "</p>"
        # DOB now is local readable time
        dob = time.strftime('%B %d %Y', time.localtime(self.v.results['dob']))  # Only instance of time being used
        # Add label span and break
        bday = "<p class='rgl'>Birthday:</p><p> " + dob + "</p>"
        # Add label span and break
        phone = "<p class='rgl'>Phone Number:</p><p> " + self.v.results['p'] + "</p>"
        # Add label span and break
        cell = "<p class='rgl'>Cell Number:</p><p> " + self.v.results['c'] + "</p>"
        # Format image with src and alt
        image_ready = "<img src='" + self.v.results['i'] + "' alt='Your Pretty Picture' />"
        # Format name with special paragraph class for css
        n = "<p class='name'>" + self.v.results['n'] + " </p>"
        # Format Address
        add = "<p class='rgl'>Address:</p><p> " + self.v.results['a'] + "</p>"

        # Return results
        formatted += n  # Start with Name
        # Add in content in a left div
        formatted += "<div id='left'>" + image_ready + "</div>"  # Only image for now
        # Add contents into right div and close rg class
        formatted += "<div id='right'>" + username + new_gender + email + bday + phone + cell + add + "</div>" + f_end

        # Adds results  to content
        return formatted

    # POLYMORPHISM USED TO CHANGE CONTENT OF PAGE
    def page(self):  # New page layout
        # P contains what will be printed, so far header and content
        p = self.header + self.content
        if self.v.userinput:  # If there is user input
            if self.v.userinput == "None":  # If the user puts in anything other than what is allowed by radio buttons
                p += self.intro + self.error + self.form  # Display error
            else:  # If the user puts in anything allowed by radio buttons
                p += self.format_results + self.form  # Add in form results and form
        else:  # If there is no input, just put in the form
            p += self.intro + self.form
        # Always add the footer to the end
        p += self.footer
        # Return final product
        return p
