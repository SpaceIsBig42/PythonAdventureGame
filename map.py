#This is just a fun test of programming, Public Domain.

from tiles import *

class Map():
    """Map base class, currently barebones, may change if
       maps are read from files rather than hardcoded in
       main.py."""
    
    def __init__(self,
                 maplist={"default": Room("MAP UNINITED", "default")}
                 ):

        #Maybe an explanation of what maplist does should go here;
        #maplist is a dictionary, with a string ID (typically the
        #lowercase name of a room) as the key, and a Room object
        #as the value. Thus, if you want to reference a specific
        #Room object in maplist, you can just do maplist[name].
        
        self.maplist = maplist
        
