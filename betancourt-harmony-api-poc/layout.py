class Layout(object):  # Class to create layout
    def __init__(self):
        # Doctype through opening body tag
        self.header = '''
<!DOCTYPE HTML>
<html>
    <head>
        <link rel="stylesheet" href="css/style.css">
        <title>Proof Of Concept</title>
    </head>
    <body>'''
        # Content place holder
        self.content = ''
        # Close body, html
        self.footer = '''
    </body>
</html>
'''
        self.page = self.header + self.content + self.footer