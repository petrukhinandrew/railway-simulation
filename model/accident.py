class Accident:
    def __init__(self, hardness):
        self.hardness = hardness
        self.msg = self.generate_msg()


    def generate_msg(self):
        if self.hardness == 1:
            return "Electricity is broken, will be fixed in a moment"
        elif self.hardness == 2:
            return "Machinist otravilsya, skoraya priedet i poedem dal'she"
        elif self.hardness == 3:
            return "Annushku namotalo na koleso, pridetsya podozhdat\'"
        else:
            return "Koronavirus razigralsya v vagone, zhdem brigadu iz SES"
