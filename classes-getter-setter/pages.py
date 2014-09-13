class Page(object):
    def __init__(self):
        self.__title = "Welcome!"  # Private
        self.__css = "css/style.css"  # Private
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="Stylesheet" type="text/css" />
    </head>
    <body>
        """
        self.__body = "Welcome to my OOP Python page!"
        self.close = """
    </body>
</html>
        """

        self.whole_page = ""

    def update(self):
        self.whole_page = self.head + self.body + self.close
        self.whole_page = self.whole_page.format(**locals())

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, new_body):
        self.__body = new_body
        self.update()

    @property  # Must have this, even if we don't use getter
    def title(self):
        return self.__title  # Allows locals

    @title.setter
    def title(self, new_title):
        self.__title = new_title
        self.update()

    @property  # Must have this, even if we don't use getter
    def css(self):
        return self.__css  # Allows locals

    @css.setter
    def css(self, new_css):
        self.__css = new_css
        self.update()