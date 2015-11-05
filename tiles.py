from items import *
class Room():
    """Room base class"""
    def __init__(self, name, description, flooritems=[],
                 exits={"N": None, "E": None, "S": None, "W": None,
                        "UP": None, "DOWN": None}):
        
        self.name = name
        self.description = description
        self.flooritems = flooritems
        self.exits = exits

        if "N" not in self.exits:
            self.exits["N"] = None
        if "E" not in self.exits:
            self.exits["E"] = None
        if "S" not in self.exits:
            self.exits["S"] = None
        if "W" not in self.exits:
            self.exits["W"] = None
        if "UP" not in self.exits:
            self.exits["UP"] = None
        if "DOWN" not in self.exits:
            self.exits["DOWN"] = None
        
    def __str__(self):
        return "Room: {0}".format(self.name)

    def giveDescription(self):
        toDescription = self.description
        for x in range(0, len(self.flooritems)):
            toDescription += "\n{0}".format(self.flooritems[x].floordescription)
        return toDescription

    def giveItem(self, item):
        for x in range(0, len(self.flooritems)):
            if self.flooritems[x].name.upper() == item.upper():
                itemToGive = self.flooritems[x]

                del self.flooritems[x]

                return itemToGive
            
        return None


