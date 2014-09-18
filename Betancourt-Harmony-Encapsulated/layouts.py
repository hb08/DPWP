from chars import Char  # Get Char class from chars


class Layout(object):
    def __init__(self):
        self.c = Char()

        # Layout
        self.header = '''<!DOCTYPE HTML>
        <head>
            <title>The New Freedom League</title>
        </head>
        <body>
            <header>
                <h1><a href="#">Claremont Academy Admin Zone</a></h1>
                <h2>Team Roster: Freedom League</h2>
                <nav>
                    <a href="#">Admin HQ</a>
                    <a href="#">More Teams</a>
                </nav>
            </header>

        '''

        self.content = '''
        <div class="wrapper">
        '''

        self.footer = '''</body>
        <footer>
            <p>Created by and for Claremont Academy Admin 2014&copy;</p>
        </footer>
    </html>

        '''

    # Print Layout to Page
    def print_layout(self):
        page = self.header + self.content + self.filler_content() + self.footer
        return page.format(**locals())

    def filler_content(self):
        formatted = ""
        for x in self.c.chars_list:
            print x.success_rate
            age = str(x.age)
            buttons = '''<a>
                <h2>{x.code_name}</h2>
                <p>{x.descrip}</p>
                <span class="hide">
                    <p>Name: {x.name}</p>
                    <p>Age: {x.age}</p>
                    <p>Total Missions: {x.missions}</p>
                    <p>Total Victories: {x.victory}</p>
                    <p>Success Rate: {x.success_rate}%</p>
                </span>
            </a>'''
            formatted += buttons.format(**locals())
        return formatted






