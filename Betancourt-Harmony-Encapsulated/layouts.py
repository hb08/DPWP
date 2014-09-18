from chars import Char  # Get Char class from chars


class Layout(object):  # Class to create layout
    def __init__(self):
        self.c = Char()  # Get characters from the chars page

        # Page header - Doctype through end of Header
        self.header = '''<!DOCTYPE HTML>
        <head>
            <title>The New Freedom League</title>
            <link rel="stylesheet" href="css/style.css">
        </head>
        <body>
            <div class="wrapper">
            <header>
                <h1><a href="#">Claremont Academy Admin Zone</a></h1>
                <h2>Team Roster: Freedom League</h2>
                <nav>
                    <a href="#">Admin HQ</a>
                    <a href="#">More Teams</a>
                </nav>
            </header>
        '''

        # Footer - Close Wrapper Div, Body Div, and full footer, end HTML
        self.footer = '''</div>
            </body>
            <footer>
                <p>Created by and for Claremont Academy Admin 2014&copy;</p>
            </footer>
        </html> '''

    # Print Layout to Page
    def print_layout(self):
        # Page layout is header, filler, and footer
        page = self.header + self.filler_content() + self.footer
        # Return it all, with locals filled in
        return page.format(**locals())

    # Set filler content
    def filler_content(self):
        formatted = ""  # Empty Format container
        # Cycle through every character in list
        for x in self.c.chars_list:
            age = str(x.age)  # Age is changed to a string
            # Set up the buttons
            buttons = '''<a>
                <h2>{x.code_name}</h2>
                <p>{x.descrip}</p>
                <span class="hide">
                    <p>Name: {x.name}</p>
                    <p>Age: {x.age}</p>
                    <p>Total Missions: {x.missions}</p>
                    <p>Total Victories: {x.victory}</p>
                    <p>Success Rate: {x.success_rate}%</p>
                    <p class="note">Status: {x.get_status}</p>
                </span>
            </a>'''
            # Format it all with the locals
            formatted += buttons.format(**locals())
        # Return the formatted stuff
        return formatted