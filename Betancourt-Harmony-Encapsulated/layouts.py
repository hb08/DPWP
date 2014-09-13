from chars import Char  # Get Char class from chars


class Layout(object):
    def __init__(self):
        self.c = Char()
        # Layout
        self.header = '''<!DOCTYPE HTML>
        <head>
            <title>Title</title>
        </head>
        <body>
            <header>
                <h1>Header</h1>
                <nav>
                    <ul>
                        <li>Nav Item</li>
                        <li>Nav Item</li>
                    </ul>
                </nav>
            </header>

        '''

        self.content = '''
        <div class="wrapper">
            <p>This is {self.c.raven.name}</p>
        </div>
        '''

        self.footer = '''</body>
        <footer>
            <p>Footer</p>
        </footer>
    </html>

        '''

    # Print Layout to Page
    def print_layout(self):
        page = self.header + self.content + self.footer
        return page.format(**locals())







