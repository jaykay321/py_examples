class Character():
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana
    def __repr__(self):
        return self.name + ": " + str(self.health) + " " + str(self.mana)

    @property
    def hp(self):
        return self.fhealth

    @name.setter
    def 

class NPC(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health, mana)
