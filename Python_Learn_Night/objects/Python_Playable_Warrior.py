from Python_Character import Character

class Warrior(Character):
    maxhp = 8
    hp = 8
    attack = 3
    defense = 1
    def __init__(self, name = "Warrior"):
        Character.__init__(self, name)