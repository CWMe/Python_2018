from Python_Character import Character

class Dragon(Character):
    maxhp = 10
    hp = 10
    defense = 1
    def __init__(self, name = "Dragon"):
        Character.__init__(self, name)