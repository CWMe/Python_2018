from Python_Character import Character

class Mage(Character):
    maxhp = 6
    hp = 6
    attack = 2
    def __init__(self, name = "Mage"):
        Character.__init__(self, name)