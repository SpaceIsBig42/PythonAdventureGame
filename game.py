#This is just a fun test of programming, Public Domain.

from map import *
from player import *

class Game():

    """Oh geez, the Game class. Where to begin. Refactoring, perhaps?
       The game class is within scope when it deals with the interaction
       between two objects, e.g a Player and a Tile class."""
    
    def __init__(self, gamemap=Map(), player=Player(), playerLocation=None):
        self.gamemap = gamemap
        self.player = player
        self.playerLocation = playerLocation

    def getLocation(self, locationName):
        """Gets a location from maplist using a name"""
        return self.gamemap.maplist[locationName]

    def getCurrentLocation(self):
        """Gets the current player location. Should be depreciated, TODO."""
        return self.gamemap.maplist[self.player.location]

    def moveDirection(self, direction):
        """Tries to move the player in a certain direction.
           Returns True if successful, otherwise False."""
        if self.getCurrentLocation().exits[direction] is not None:
            self.movePlayer(self.getCurrentLocation().exits[direction])
            return True
        else:
            return False

    def printDescription(self, full=True):
        """Prints the current locations.
           Also accepts a "full" option, if True then it also
           prints the current locations giveDescription()"""
        
        print(self.getCurrentLocation().name)
        if full:
            print(self.getCurrentLocation().giveDescription())
        
    def movePlayer(self, movelocation):
        """Sets the players location to movelocation."""
        self.player.location = movelocation

    def givePlayerItem(self, itemToGet):
        """Takes a string, and asks the player to take that item."""
        item = self.getCurrentLocation().giveItem(itemToGet.lower())
        if item != None:
            self.player.addItem(item)
            return True
        else:
            return False

    def dropItem(self, itemToDrop):
        """Takes a string, and gets the player to drop that item."""
        item = self.player.getitemref(itemToDrop)
        if item != None:
            self.getCurrentLocation().flooritems.append(item)
            self.player.loseItem(item)
            return True
        else:
            return False
    
