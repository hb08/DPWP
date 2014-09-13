
import webapp2
#import pages # Whole file
from pages import Page  # Get Page class from pages

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "My Page!"
        p.css = "css/style.css"
        p.body = "Apples!"
        self.response.write(p.whole_page)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
