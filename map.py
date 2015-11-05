from tiles import *
class Map():
    def __init__(self,
                 maplist={"default": Room("MAP UNINITED", "default")}
                 ):
        self.maplist = maplist
        
