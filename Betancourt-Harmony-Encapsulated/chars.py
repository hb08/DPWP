class Char(object):
    def __init__(self):
        # First Char
        self.chars_list = []
        raven = Character()
        raven.name = "Duncan McNeil"
        raven.code_name = "The Raven"
        raven.age = 57
        raven.descrip = "Hardly Human Headmaster"
        raven.missions = 1243
        raven.victory = 1241
        self.chars_list.append(raven)

        clio = Character()
        clio.name = "Laia Eavening"
        clio.code_name = "Clio"
        clio.age = 15
        clio.descrip = "Beloved Bookworm"
        clio.missions = 12
        clio.victory = 8
        self.chars_list.append(clio)

        qilin = Character()
        qilin.name = "Yvette Van De Voorst"
        qilin.code_name = "Qilin"
        qilin.age = 18
        qilin.descrip = "The Last Unciorn"
        qilin.missions = 47
        qilin.victory = 47
        self.chars_list.append(qilin)

        toon = Character()
        toon.name = "Rudy DeMarca"
        toon.code_name = "Toon"
        toon.age = 15
        toon.descrip = "Artistic Intent"
        toon.missions = 23
        toon.victory = 18
        self.chars_list.append(toon)

        atlanta = Character()
        atlanta.name = "Vijana Ravana Romana"
        atlanta.code_name = "Atlanta"
        atlanta.age = 18
        atlanta.descrip = "Psychic Gypsy Werewolf"
        atlanta.missions = 19
        atlanta.victory = 18
        self.chars_list.append(atlanta)




class Character(object):
    def __init__(self):
        self.name = ""
        self.code_name = ""
        self.age = 0
        self.descrip = ""
        self.missions = 0
        self.victory = 0
        self.__status = "PC"

    @property
    def success_rate(self):
        s = float(self.victory)/float(self.missions)
        s *= 100
        s = round(s, 2)
        return str(s)

    @property  # Must have for Setter
    def status(self):
        pass

    # Setter
    @status.setter  # Change Status
    def status(self, m):
        self.__status = m










