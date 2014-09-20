import urllib2  # Python classes and code needed to request/recieve/open url info
import json

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
    <body>"""
        # Content place holder
        self.content = ''
        # Close body, html
        self.footer = """
    </body>
</html>
"""

    def page(self):
        return self.header + self.content + self.footer


class IndexPage(Layout):  # Makes a layout object called IndexPage
    def __init__(self):  # Initialize the IndexPage class
        super(IndexPage, self).__init__()  # Initialize the Layout class to inherit
        self._form_close = '</form>'
        self.__form_content = []  # Private and Protected
        self._form = '<form method="GET">'
        self._userinput = ''
        self._results = ''

    @property
    def form(self):  # Getter for form
        return self._form

    @property
    def form_content(self):  # Getter for form_content
        return self.__form_content

    @property
    def userinput(self):
        return self._userinput

    @userinput.setter  # Set user input value
    def userinput(self, g):
        self._userinput = g

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

    @property
    def results(self):  # Getter for results
        return self._results

    @results.setter  # Set the API in motion
    def results(self, g):
        gender = g
        url = "http://api.randomuser.me/?gender=" + gender
        # Assemble request
        request = urllib2.Request(url)
        # Use urllib2 to create object to get url
        geturl = urllib2.build_opener()
        # Use url to get result - request info from API
        fromapi = geturl.open(request)
        self._results = "Working"

    # Override default page
    def page(self):
        return self.header + self.content + self.form + self._form_close + self.results + self.footer
