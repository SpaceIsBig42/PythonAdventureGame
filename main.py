from game import *

gameRunning = True

itemsdictionary = {"stick": Item(name="Stick",
                                 description="A weird looking stick.",
               floordescription="You see here a weird looking stick.")}

directions = ["N", "E", "W", "S"] #Depreciated, use directionsynonyms
directionsynonyms = {"NORTH": "N", "EAST": "E", "WEST": "W", "SOUTH": "S",
                     "N": "N", "E": "E", "W": "W", "S": "S"}

takesynonyms = ["TAKE", "GET", "PICKUP"]

gameMap = Map({"HillTop": Room("Top of Hill", "You stand here on a hilltop.",
                               exits ={"E" : "Forest"},
                               flooritems=[itemsdictionary["stick"]]),
               "Forest": Room("Forest", "You are in a forest.",
                              exits = {"W" : "HillTop"})
               })
player = Player()
game = Game(gameMap, player, playerLocation="HillTop")

while gameRunning: #Main game loop
    print(game.getCurrentLocation().name)
    print(game.getCurrentLocation().giveDescription())
    answer = input("> ").upper().split(" ")

    if answer[0] in directionsynonyms or answer[0] == "GO":
        if answer[0] == "GO":
            if answer[1] in directionsynonyms:
                direction = directionsynonyms[answer[1]]
            else:
                print("I don't understand, you want to go {0}?".format(answer[1]))
        elif answer[0] in directionsynonyms:
            direction = directionsynonyms[answer[0]]
            
        if game.moveDirection(direction) is True:
            pass
        else:
            print("You can't go that way.")

    elif answer[0] in takesynonyms:
        if game.givePlayerItem(answer[1]) != False:
            print("You take the {0}.".format
                  (player.inventory[len(player.inventory)-1].name.lower()))
        else:
            print("There's nothing called a {0} here.".format(answer[1]))
    elif answer[0] == "INVENTORY":
        print("Your inventory:")
        if len(player.inventory) != 0:
            for x in range(0, len(player.inventory)):
                print(player.inventory[x].name)
        else:
            print("You have nothing but the clothes on your back.")
            
    elif answer[0] == "CHEAT":
        exec(input("cheatprompt> "))

    elif answer[0] == "DROP":
        if len(answer) > 0:
            success = game.dropItem(answer[1].lower())
            if success:
                print("You dropped the {}.".format(answer[1].lower()))
            else:
                print("Ypu don't have a {}.".format(answer[1].lower()))
        else:
            print("What do you want to drop?")
        
    else:
        print("I don't understand.")

    print("")
    
    
