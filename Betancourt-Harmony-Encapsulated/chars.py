class Char(object):
    def __init__(self):
        # First Char
        self.raven = Character()
        self.raven.name = "Duncan McNeil"
        self.raven.code_name = "The Raven"
        self.raven.age = 57
        self.raven.descrip = "Hardly Human Headmaster"
        self.raven.missions = 1243
        self.raven.victory = 1241

        self.clio = Character()
        self.clio.name = "Laia Eavening"
        self.clio.code_name = "Clio"
        self.clio.age = 15
        self.clio.descrip = "Beloved Bookworm"
        self.clio.missions = 12
        self.clio.victory = 8

        self.qilin = Character()
        self.qilin.name = "Yvette Van De Voorst"
        self.qilin.code_name = "Qilin"
        self.qilin.age = 18
        self.qilin.descrip = "The Last Unciorn"
        self.qilin.missions = 47
        self.qilin.victory = 47

        self.toon = Character()
        self.toonname = "Rudy DeMarca"
        self.tooncode_name = "Toon"
        self.toonage = 15
        self.toondescrip = "Artistic Intent"
        self.toonmissions = 23
        self.toonvictory = 18

        self.atlanta = Character()
        self.atlantaname = "Vijana Ravana Romana"
        self.atlantacode_name = "Atlanta"
        self.atlantaage = 18
        self.atlantadescrip = "Psychic Gypsy Werewolf"
        self.atlantamissions = 19
        self.atlantavictory = 18


class Character(object):
    def __init__(self):
        self.name = ""
        self.code_name = ""
        self.age = 0
        self.descrip = ""
        self.missions = 0
        self.victory = 0
        self.__status = "PC"

    def success_rate(self):
        sr = self.victory/self.missions
        return sr


