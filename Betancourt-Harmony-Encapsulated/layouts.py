from chars import Char  # Get Char class from chars


class Layout(object):  # Class to create layout
    def __init__(self):
        self.c = Char()  # Get characters from the chars page

        # Page header - Doctype through end of body header
        self.header = '''<!DOCTYPE HTML>
        <head>
            <title>The New Freedom League</title>
            <link rel="stylesheet" href="css/style.css">
            <script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
            <script src="js/script.js"></script>
        </head>
        <body>
            <div class="wrapper">
            <header>
                <h1><a href="#">Claremont Academy Admin Zone</a></h1>
                <h2>Team Roster: Freedom League</h2>
                <nav>
                    <a href="#"><span id="leftArrow"></span>Admin HQ</a>
                    <a href="#">More Teams<span id="rightArrow"></a>
                </nav>
            </header>
        '''

        # Content Frame - Title panel and start charList class
        self.content = ''' <div id="titlePanel">
            <p>The Freedom League has long been established as the mascot of Freedom City, Texas.
            With an ever-changing roster of super heroes willing to sacrifice their time, energy, and even lives,
            they have earned the respect and love of the city they defend.
        </div>
        <div id="charList">
        '''

        # Footer - Close charList, wrapper, body, and full footer, end HTML
        self.footer = '''</div>
        </div>
            </body>
            <footer>
                <p>Background image from <a href="http://www.morguefile.com/">MorgueFile</a>.
                <p>All other images created by Harmony for Claremont Academy 2014&copy;</p>
            </footer>
        </html> '''

    # Print Layout to Page
    def print_layout(self):
        # Page layout is header, content, filler, and footer
        page = self.header + self.content + self.filler_content() + self.footer
        # Return it all, with locals filled in
        return page.format(**locals())

    # Set filler content
    def filler_content(self):
        formatted = ""  # Empty Format container
        # Cycle through every character in list
        for x in self.c.chars_list:
            # Set up the buttons
            buttons = '''<a class="charChard">
                <h2>{x.code_name}</h2>
                <img src="img/peeps/{x.code_name}.jpg" alt="{x.code_name}" />
                <h3>{x.descrip}</h3>
                <span class="panel hide">
                    <img src="img/costumes/{x.code_name}.jpg" alt="{x.code_name} Costume" />
                    <p class="name"><span class="label">Name:</span> {x.name}</p>
                    <p><span class="label">Age:</span> {x.age}</p>
                    <p><span class="label">Total Missions:</span> {x.missions}</p>
                    <p><span class="label">Total Victories:</span> {x.victory}</p>
                    <p><span class="label">Success Rate:</span> {x.success_rate}%</p>
                    <p class="note">Status: {x.get_status}</p>
                </span>
            </a>
            '''
            # Format it all with the locals
            formatted += buttons.format(**locals())
        # Return the formatted stuff
        return formatted