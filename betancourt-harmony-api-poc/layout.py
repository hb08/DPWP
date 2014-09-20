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
        self._form_start = '<form method="GET">'
        self._form_close = '</form>'
        self.__form_content = []  # Private and Protected
        self._form = ''

    @property
    def form_content(self):  # Getter for form_content
        pass

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

    # Override default page
    def page(self):
        return self.header + self.content + self._form_start + self._form + self._form_close + self.footer
