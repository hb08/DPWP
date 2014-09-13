class Char(object):
    def __init__(self):
        # First Char
        raven = Character()
        raven.name = "Duncan McNeil"
        raven.code_name = "The Raven"
        raven.age = 57
        raven.descrip = "Hardly Human Headmaster"
        raven.missions = 1243
        raven.victory = 1241

        clio = Character()
        clio.name = "Laia Eavening"
        clio.code_name = "Clio"
        clio.age = 15
        clio.descrip = "Beloved Bookworm"
        clio.missions = 12
        clio.victory = 8

        qilin = Character()
        qilin.name = "Yvette Van De Voorst"
        qilin.code_name = "Qilin"
        qilin.age = 18
        qilin.descrip = "The Last Unciorn"
        qilin.missions = 47
        qilin.victory = 47

        toon = Character()
        toon.name = "Rudy DeMarca"
        toon.code_name = "Toon"
        toon.age = 15
        toon.descrip = "Artistic Intent"
        toon.missions = 23
        toon.victory = 18

        atlanta = Character()
        atlanta.name = "Vijana Ravana Romana"
        atlanta.code_name = "Atlanta"
        atlanta.age = 18
        atlanta.descrip = "Psychic Gypsy Werewolf"
        atlanta.missions = 19
        atlanta.victory = 18


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


