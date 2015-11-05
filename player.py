from items import *

class Player():
    def __init__(self, inventory=[], hp=50):
        self.inventory = inventory
        self.hp = hp
    def __str__(self):
        return "Player: HP = {0}".format(self.hp)

    def addItem(self, item):
        self.inventory.append(item)

    def dropitem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        else:
            return False

    def getitemref(self, item):
        for x in range(0, len(self.inventory)):
            if self.inventory[x].name.lower() == item:
                return self.inventory[x]
            else:
                return None
