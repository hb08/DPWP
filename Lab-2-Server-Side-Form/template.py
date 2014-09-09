class Site(object):
    def __init__(self):
        self.title = "Welcome!"
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
        self.body =

        # Closing for body tag, footer, and html
        self.closer = """
            </body>
            <footer>

            </footer>
        </html>"""
        self.page = self.header + self.body + self.closer
