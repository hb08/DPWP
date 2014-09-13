#!/usr/bin/env python
# Create transcript

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        t = Transcript()  # First student
        t.grade1 = 90
        t.grade2 = 100
        t.quiz1 = 75
        t.quiz2 = 99
        t.final_grade = 99  # To Change the private Final Grade
        self.response.write("Tommy's final grade is " + str(t.final_grade) + "<br/>")  # Can only access property for final grade, not the class final grade

        s = Transcript()  # Second student
        s.grade1 = 45
        s.grade2 = 80
        s.quiz1 = 66
        s.quiz2 = 76
        s.calc_grade()
        self.response.write("Sam's final grade is " + str(s.final_grade) + "<br/>")




class Transcript(object):
    def __init__(self):
        self.grade1 = 0
        self.grade2 = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.final_exam = 0
        self.__final_grade = 0  # PRIVATE - Two underscores before final grade

    # Getter
    @property  # Decorator
    def final_grade(self):
        return self.__final_grade

    # Setter
    @final_grade.setter
    def final_grade(self, new_final_grade):
        self.__final_grade = new_final_grade

    def calc_grade(self):
        # Calculate Final Grade
        self.__final_grade = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2 + self.final_exam)/5
        return self.__final_grade

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
