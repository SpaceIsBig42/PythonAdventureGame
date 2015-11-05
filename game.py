from map import *
from player import *

class Game():
    def __init__(self, gamemap=Map(), player=Player(), playerLocation=None):
        self.gamemap = gamemap
        self.player = player
        self.playerLocation = playerLocation

    def getLocation(self, locationName):
        return self.gamemap.maplist[locationName]

    def getCurrentLocation(self):
        return self.gamemap.maplist[self.playerLocation]

    def moveDirection(self, direction):
        if self.getCurrentLocation().exits[direction] is not None:
            self.movePlayer(self.getCurrentLocation().exits[direction])
            return True
        else:
            return False
        
    def movePlayer(self, location):
        self.playerLocation = location

    def givePlayerItem(self, itemToGet):
        item = self.getCurrentLocation().giveItem(itemToGet.lower())
        if item != None:
            self.player.addItem(item)
            return True
        else:
            return False

    def dropItem(self, itemToDrop):
        item = self.player.getitemref(itemToDrop)
        if item != None:
            self.getCurrentLocation().flooritems.append(item)
            self.player.dropitem(item)
            return True
        else:
            return False
    
