class Site(object):
    def __init__(self):
        # Variables for site info
        self.title = "Contact Us!"
        self.css = "css/style.css"
        # Heading for the page is doctype, head, opening body and wrapper tags, and page heading
        self.header = """<!DOCTYPE HTML>
            <html>
             <head>
                 <title>{self.title}</title>
                <link href="{self.css}" rel="Stylesheet" type="text/css" />
             </head>
             <body>"""
        # Format Header with locals
        self.header = self.header.format(**locals())

        self.body_start = """<div id='wrapper'>
            <h1>{self.title}</h1>
            <nav>
                <ul>
                    <li><a href='#' id='home'><p>Home</p></a></li>
                    <li><a href='#' id='contact'><p>Contact</p></a></li>
                    <li><a href='#' id='location'><p>Locations</p></a></li>
                    <li><a href='#' id='work'><p>Work</p></a></li>
                </ul>
            </nav>
            """
        self.body_start = self.body_start.format(**locals())

        # Declare body, but don't give it an actual variable yet, that is done on if statement in main.py
        self.body = " "

        # Closing for body and wrapper tag, footer, and html
        self.closer = """</div>
                <footer>Made by Harmony<br/>Icons by <a href='http://azuresol.deviantart.com/'>Azuresol</a></footer>
            </body>
        </html> """

        # Contact Form created
        self.contact_form = """<h2>We'd love to hear from you!</h2>
         <form method="get">
            <div class="col">
                <div class="row">
                    <label>Name:</label>
                    <input type="text" name="contact" />
                </div>
                <div class="row">
                    <label>Phone:</label>
                    <input type="phone" name="phone" />
                    <label>Email:</label>
                    <input type="text" name="email" />
                </div>
                <div class="row">
                    <label class='sub'>Respond By:</label>
                    <label><input type="checkbox" name="response" value="email"/><p>Email</p></label>
                    <label><input type="checkbox" name="response" value="phone"/><p>Phone</p></label>
                    <label><input type="checkbox" name="response" value="none"/><p>No Response Needed.</p></label>
                </div>
            </div>
            <div class="col">
                <div class="row">
                    <label>Reason for Contact:</label>
                    <select name="reason">
                        <option value="question">Question</option>
                        <option value="comment">Comment</option>
                        <option value="concern">Concern</option>
                        <option value="personal">Personal</option>
                     </select>
                </div>
                <div class="row">
                    <label>Message:</label>
                    <textarea name="message" placeholder="Type here" maxlength="1000"> </textarea>
                </div>
            </div>
            <input type="submit" value="Submit"/>
        </form>"""

        # Static Text
        self.text = {
            'thanks_head': "<h2>Thank you!</h2><p class='ty'>",
            'thanks_start': ", we appreciate the ",
            'thanks_mes': " message you sent of: <br/> <span>",
            'thanks_close': "</span> ",
            'appr': "<br/>We read every message we receive, and will give yours the consideration it deserves.",
            'con': "<br/>We will contact you at ",
            'link': "<div class='tyLinks'><a href='http://localhost:12080'>Go Back</a><a href='#'>Home</a></div>"
        }


