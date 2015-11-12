from items import *

#This is just a fun test of programming, Public Domain.

class Player():
    
    """The player class deals with storing information about
       the player, inventory, hitpoints, and so forth.
       The player class should mostly deal with itself, not
       with other classes, so a hypothetical "attackEnemy(enemy)"
       method would be out of scope, and should go in Game."""
    
    def __init__(self, inventory=[], hp=50, location=None):
        self.inventory = inventory
        self.hp = hp #hitpoints
        self.location = location #Location, playerLocation, location.
    
    def __str__(self):
        #Changes what you get when you print a Player object,
        #for debug purposes. This is not an excuse to print(player)
        #in actual methods!
        return "Player: HP = {0}".format(self.hp)

    def addItem(self, item):
        """Adds an item to the players inventory."""
        self.inventory.append(item)

    def loseItem(self, item):
        
        """Makes the player lose an item. The method checks if the
           item to lose "item" is in the inventory. If it is, it
           removes the item and returns True. Otherwise, returns False."""
        
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        else:
            return False

    def getitemref(self, item):

        """This method takes a string e.g "sword", and if an item
           with that (lowercase) name is in the inventory,
           it returns that. Otherwise, it returns None."""
        
        for x in range(0, len(self.inventory)):
            if self.inventory[x].name.lower() == item:
                return self.inventory[x]
            else:
                return None
