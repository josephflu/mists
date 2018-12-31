import math
import sys
from enum import Enum
from models import *
from colorama import init, Fore, Back, Style

init(autoreset=True) #colorama initialzation


#--- Global Variables
CurrentRoom = None
RoomDict = {}
Inventory =[]


def MakeRoom(roomId,description, areDoorsOpen = True):
    newroom = Room(roomId,description,areDoorsOpen)
    RoomDict[roomId] = newroom
    return newroom


#--- Level 1 Rooms
entryHallRoom = MakeRoom("Entry Hall", "You stand on a sandy beach outside the lair of a Great Dragon. ")
emptyRoom1 = MakeRoom("Empty Room 1", "There is a great hall filled with art mostly depicting a large dragon. What looks like it was a map has been burned, and ripped beyond repair.")
puzzleRoom1 = MakeRoom("Puzzle Room 1", "You have entered a puzzle room.", False)
puzzleRoom1.Action = RoomAction("Solve Puzzle", ResultType.DoorsOpen,"You solved the sphynx puzzle. Nice Job, yes we are going to make this part harder, don't worry.")
cryptRoom = MakeRoom("Crypt Room", "You walk into a crypt filled with many coffins. They look like they have beeen here for thousands of years.")
cryptRoom.Action = RoomAction("Open Casket",ResultType.Die,"A spirit drifts upward, and enters you, it compels you to enter the largest tomb, and close it. When you gain control of your body again you find that you are locked inside. You suffocate to death.")
treasureRoom = MakeRoom("Treasure Room", "Here is a room with a pillar in the center. On it is a bag full of coins.")
treasureRoom.Item = Item(ItemType.Money, "bag of coins")
emptyRoom2 = MakeRoom("Empty Room 2", "You enter an empty room.")
goblinCrossingRoom = MakeRoom("Goblin Crossing", "Ahead you see a large bridge.",False)
goblinCrossingRoom.Action = RoomAction("Give Goblin Coins", ResultType.DoorsOpen,"The Goblin steps aside and lets you pass.")
emptyRoom3 = MakeRoom("Empty Room 3", "You enter an empty room.")
trollCaveRoom = MakeRoom("Troll Cave","Here lies a large troll. You wake him, and he blocks all exits to the room")
trollCaveRoom.Action = RoomAction("Attack Troll", ResultType.DoorsOpen,"The Troll dies, and your weapon gets stuck in the troll.")
armoryRoom = MakeRoom("Armory Room","There is an abandoned Armory here. The armor racks are all empty, with the exception of one rusted Dagger")
armoryRoom.Item = Item(ItemType.Weapon,"Rusted Dagger")
emptyRoom4 = MakeRoom("Empty Room 4", "You enter an empty room.")
sphynxRoom = MakeRoom("Sphynx Room", "Here lies a large sphynx. All doors close and the sphynx tells you a riddle.",areDoorsOpen=False)
sphynxRoom.Action = RoomAction("Solve Puzzle", ResultType.DoorsOpen,"You solved the sphynx puzzle. Nice Job, yes we are going to make this part harder, don't worry.")
AddConnection(entryHallRoom,emptyRoom1,'w')
AddConnection(emptyRoom1,puzzleRoom1,'n')
AddConnection(puzzleRoom1,cryptRoom,'n')
AddConnection(puzzleRoom1,treasureRoom,'e')
AddConnection(treasureRoom,goblinCrossingRoom,'n')
AddConnection(treasureRoom,emptyRoom2,'s')
AddConnection(goblinCrossingRoom,emptyRoom3,'e')
AddConnection(emptyRoom3,trollCaveRoom,'n')
AddConnection(emptyRoom3,armoryRoom,'s')
AddConnection(trollCaveRoom,emptyRoom4,'w')
AddConnection(emptyRoom4,sphynxRoom,'n')


# --- Level 2 Rooms
emptyRoom21 = MakeRoom("Empty Room 2.1","### ENTERING LEVEL 2 ####\n Welcome to Level 2! You enter an empty Room")
emptyRoom21.IsFirstOfLevel = True
pitFall = MakeRoom("Pitfall Room","While walking into this room the floor drops and you die")
pitFall.InstantDeath = True
bankRoom = MakeRoom("Bank Room","A huge vast room lies ahead. As you step into this establishment, you hear the echo of your feet on marble floors. There is a vault here, but it looks like it requires a key.")
oldMarketplace = MakeRoom("Old Marketplace","This large square room is what looks like was once a vast marketplace. The smell of rotting fruit corrodes the air.")
puzzleRoom21 = MakeRoom("Puzzle Room 2.1","Solve puzzle ...")
armory21 = MakeRoom("Armory 2.1","There is an abandoned Armory here. The armor racks are all empty, with the exception of an old bow and arrow")
armory21.Item = Item(ItemType.Weapon,"Bow and Arrow")
poisonDartHall21 = MakeRoom("Poison Dart Hall","There are many statues in this call. While looking at a statue a dart comes flying out of his mouth and strikes you, as do many others from around you.")
poisonDartHall21.InstantDeath = True
AddConnection(sphynxRoom,emptyRoom21,'n')
AddConnection(emptyRoom21,pitFall,'e')
AddConnection(emptyRoom21,bankRoom,'n')
AddConnection(bankRoom,oldMarketplace,'n')
AddConnection(oldMarketplace,puzzleRoom21,'w')
AddConnection(puzzleRoom21,armory21, 's')
AddConnection(armory21,poisonDartHall21,'s')

#--- Process Current Room
def ProcessDeath():
    global CurrentRoom
    print(Fore.RED + 'YOU DIED!')
    CurrentRoom = DefaultRoom
    ProcessCurrentRoom()

def ProcessCurrentRoom():
    print()
    print(Fore.BLUE + "                ####### " + CurrentRoom.RoomID + " #######")
    print(CurrentRoom.Description)
    print("There is a door to the ",end='')
    if CurrentRoom.ConnectionNorth is not None:
        print("North,",end='')
    if CurrentRoom.ConnectionEast is not None:
        print("East,",end='')
    if CurrentRoom.ConnectionSouth is not None:
        print("South,",end='')
    if CurrentRoom.ConnectionWest is not None:
        print("West,",end='')
    print('\b ')
    if CurrentRoom.InstantDeath:
        ProcessDeath()
        return
    if CurrentRoom.Item is not None:
        print("Item found in room: ",CurrentRoom.Item.Name)
    if CurrentRoom.Action is not None:
        print("Available Action: ",CurrentRoom.Action.Name)
    print("                Commands: n=North,e=East,s=South,w=West,p=Pick up Item,a=Do Action")


def ProcessCommand(arg):
    global CurrentRoom
    global DefaultRoom
    validroomId = None
    if line == "q":
        print("See ya, thanks for playing!")
        quit()
    elif line == "n":
        if CurrentRoom.ConnectionNorth is not None:
            validroomId = CurrentRoom.ConnectionNorth
        else:
            print("Can't move North")
    elif line == "e":
        if CurrentRoom.ConnectionEast is not None:
            validroomId = CurrentRoom.ConnectionEast
        else:
            print("Can't move East")
    elif line == "s": 
        if CurrentRoom.ConnectionSouth is not None:
            validroomId = CurrentRoom.ConnectionSouth
        else:
            print("Can't move South")
    elif line == "w":
        if CurrentRoom.ConnectionWest is not None:
            validroomId = CurrentRoom.ConnectionWest
        else:
            print("Can't move West")
    elif line == "i":
        if len(Inventory)>0 :
            print("Inventory:" + ','.join(str(i.Name) for i in Inventory))
        else:
            print("Inventory is empty")
    elif line == "p":
        if CurrentRoom.Item is not None:
            print(Fore.BLUE + "You have picked up a " + CurrentRoom.Item.Name)
            Inventory.append(CurrentRoom.Item)
            CurrentRoom.Item = None
        else:
            print("Nothing to pick up")
    elif line == "a":
        if CurrentRoom.Action is not None:
            if CurrentRoom.Action.ResultType == ResultType.Die:
                print("oops, you did " + CurrentRoom.Action.Name + ". " + CurrentRoom.Action.ResultDescription)
                ProcessDeath()
                return
            elif CurrentRoom.Action.ResultType == ResultType.DoorsOpen:
                print("You opened the doors")
                CurrentRoom.AreDoorsOpen = True
        else:
            print("No actions available")

    else:
        print("Invalid command")

    if validroomId is not None:
        if CurrentRoom.AreDoorsOpen: 
            CurrentRoom = RoomDict[validroomId]
            if CurrentRoom.IsFirstOfLevel:
                DefaultRoom = CurrentRoom
            ProcessCurrentRoom()
        else:
            print("Door is closed")

# --- Initialize and Start Game
print("Welcome to Mists of Horizon.")
print("Fearlessly you approach the dragon's lair. You know that what comes next could result in great pain, but you are determined to stop the dragon, to save your city and country. To avenge your family. ")

#CurrentRoom = entryHallRoom
DefaultRoom = sphynxRoom # Default room after Death
CurrentRoom = DefaultRoom # Current room player is in

ProcessCurrentRoom()

while True:
    line = input()
    ProcessCommand(line)
