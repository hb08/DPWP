class Char(object):
    def __init__(self):
        # First Char
        self.chars_list = []  # Empty list to put characters into for iteration
        raven = Character()  # Create Character
        raven.name = "Duncan McNeil"  # Character's Real Name
        raven.code_name = "The Raven"  # Character's Code Name
        raven.age = 57  # Character's Age
        raven.descrip = "Hardly Human Headmaster"  # Brief Character/Powerset Description
        raven.missions = 1243  # Total missions attempted
        raven.victory = 1241  # Total missions accomplished successfully
        raven.set_status = "NPC"  # Status - should be PC (Player Character) unless changed specifically by Admin
        self.chars_list.append(raven)  # And add to list

        clio = Character()  # Create Character
        clio.name = "Laia Eavening"  # Character's Real Name
        clio.code_name = "Clio"  # Character's Code Name
        clio.age = 15  # Character's Age
        clio.descrip = "Beloved Bookworm"  # Brief Character/Powerset Description
        clio.missions = 12  # Total missions attempted
        clio.victory = 8  # Total missions accomplished successfully
        self.chars_list.append(clio)  # And add to list

        qilin = Character()  # Create Character
        qilin.name = "Yvette Van De Voorst"  # Character's Real Name
        qilin.code_name = "Qilin"  # Character's Code Name
        qilin.age = 18  # Character's Age
        qilin.descrip = "The Last Unciorn"  # Brief Character/Powerset Description
        qilin.missions = 47  # Total missions attempted
        qilin.victory = 47  # Total missions accomplished successfully
        self.chars_list.append(qilin)  # And add to list

        toon = Character()  # Create Character
        toon.name = "Rudy DeMarca"  # Character's Real Name
        toon.code_name = "Toon"  # Character's Code Name
        toon.age = 15  # Character's Age
        toon.descrip = "Artistic Intent"  # Brief Character/Powerset Description
        toon.missions = 23  # Total missions attempted
        toon.victory = 18  # Total missions accomplished successfully
        self.chars_list.append(toon)  # And add to list

        atlanta = Character()  # Create Character
        atlanta.name = "Vijana Ravana Romana"  # Character's Real Name
        atlanta.code_name = "Atlanta"  # Character's Code Name
        atlanta.age = 18  # Character's Age
        atlanta.descrip = "Psychic Gypsy Werewolf"  # Brief Character/Powerset Description
        atlanta.missions = 19  # Total missions attempted
        atlanta.victory = 18  # Total missions accomplished successfully
        self.chars_list.append(atlanta)  # And add to list


class Character(object):  # Each Character will have a
    def __init__(self):
        self.name = ""  # Birth Name
        self.code_name = ""  # Code Name
        self.age = 0  # Age
        self.descrip = ""  # Brief Description of power/character concept
        self.missions = 0  # Missions attempted
        self.victory = 0  # Missions successful
        self.__status = "PC"  # Status - PC (player character) Unless specifically changed to NPC (Non Player Character)

    @property
    def success_rate(self):  # Success Rate is calculated
        s = float(self.victory)/float(self.missions)  # Divide victory by missions with result as float
        s *= 100  # Times 100
        s = round(s, 2)  # Round off at 2 decimal points
        return str(s)  # Return the percentage

    @property # Get Status for everyone
    def get_status(self):
        return self.__status  # Return private Status

    @property  # Must have for Setter
    def set_status(self):
        return self.__status  # Return private Status

    # Setter
    @set_status.setter  # Change Status to what is input
    def set_status(self, new_status):
        self.__status = new_status











