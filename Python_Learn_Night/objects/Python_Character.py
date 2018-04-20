class Character():
    maxhp = 5
    hp = 5
    attack = 2
    defense = 0
    name = ""
    def __init__(self, name):
        self.name = name
    def getHP(self):
        return str(self.hp) +"/"+str(self.maxhp) 