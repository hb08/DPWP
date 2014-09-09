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
        # Format Header with locals
        self.header = self.header.format(**locals())

        # Declare body, but don't give it an actual variable yet, that is in a function later
        self.body = " "

        # Closing for body tag, footer, and html
        self.closer = """<footer>Made by Harmony</footer>
            </body>
        </html>"""

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

