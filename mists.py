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


def MakeRoom(roomId,description,challengeType=None):
    newroom = Room(roomId,description,challengeType)
    RoomDict[roomId] = newroom
    return newroom


#--- Level 1 Rooms
entryHallRoom = MakeRoom("Entry Hall", "You stand on a sandy beach outside the lair of a Great Dragon. ")
emptyRoom1 = MakeRoom("Empty Room 1", "There is a great hall filled with art mostly depicting a large dragon. What looks like it was a map has been burned, and ripped beyond repair.")
puzzleRoom1 = MakeRoom("Puzzle Room 1", "You have entered a puzzle room.",ChallengeType.Puzzle)
puzzleRoom1.Actions.append(RoomAction("Solve Puzzle","s", ResultType.DoorsOpen,"You solved the sphynx puzzle. Nice Job, yes we are going to make this part harder, don't worry."))
cryptRoom = MakeRoom("Crypt Room", "You walk into a crypt filled with many coffins. They look like they have beeen here for thousands of years.")
cryptRoom.Actions.append(RoomAction("Open Casket","o",ResultType.Die,"A spirit drifts upward, and enters you, it compels you to enter the largest tomb, and close it. When you gain control of your body again you find that you are locked inside. You suffocate to death."))
treasureRoom = MakeRoom("Treasure Room", "Here is a room with a pillar in the center. On it is a bag full of coins.")
treasureRoom.Item = Item(ItemType.Money, "bag of coins")
emptyRoom2 = MakeRoom("Empty Room 2", "You enter an empty room.")
goblinCrossingRoom = MakeRoom("Goblin Crossing", "Ahead you see a large bridge.",ChallengeType.Monster)
goblinCrossingRoom.Actions.append(RoomAction("Give Goblin Coins", "g", ResultType.DoorsOpen,"The Goblin steps aside and lets you pass."))
emptyRoom3 = MakeRoom("Empty Room 3", "You enter an empty room.")
trollCaveRoom = MakeRoom("Troll Cave","Here lies a large troll. You wake him, and he blocks all exits to the room")
trollCaveRoom.Actions.append(RoomAction("Attack Troll","a", ResultType.DoorsOpen,"The Troll dies, and your weapon gets stuck in the troll."))
armoryRoom = MakeRoom("Armory Room","There is an abandoned Armory here. The armor racks are all empty, with the exception of one rusted Dagger")
armoryRoom.Item = Item(ItemType.Weapon,"Rusted Dagger")
emptyRoom4 = MakeRoom("Empty Room 4", "You enter an empty room.")
sphynxRoom = MakeRoom("Sphynx Room", "Here lies a large sphynx. All doors close and the sphynx tells you a riddle.",ChallengeType.Puzzle)
sphynxRoom.Actions.append(RoomAction("Solve Puzzle","s", ResultType.DoorsOpen,"You solved the sphynx puzzle. Nice Job, yes we are going to make this part harder, don't worry."))
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
puzzleRoom21 = MakeRoom("Puzzle Room 2.1","Solve puzzle ...",ChallengeType.Puzzle)
puzzleRoom21.Actions.append(RoomAction("Solve Puzzle","s", ResultType.DoorsOpen,"You solved the sphynx puzzle. Nice Job, yes we are going to make this part harder, don't worry."))
armory21 = MakeRoom("Armory 2.1","There is an abandoned Armory here. The armor racks are all empty, with the exception of an old bow and arrow")
armory21.Item = Item(ItemType.Weapon,"Bow and Arrow")
poisonDartHall21 = MakeRoom("Poison Dart Hall","There are many statues in this call. While looking at a statue a dart comes flying out of his mouth and strikes you, as do many others from around you.")
poisonDartHall21.InstantDeath = True
emptyRoom22 = MakeRoom("Empty Room 2.2","You enter an empty room.")
sphynxRoom21 = MakeRoom("Sphynx Room 2.1", "Here lies a large sphynx. All doors close and the sphynx tells you a riddle.",ChallengeType.Puzzle)
sphynxRoom21.Actions.append(RoomAction("Solve Puzzle", "s", ResultType.DoorsOpen,"You solved the sphynx puzzle. Nice Job, yes we are going to make this part harder, don't worry."))
armory22 = MakeRoom("Armory 2.2","There is an abandoned Armory here. The armor racks are all empty, with the exception of a small spiky mace")
trollCaveRoom2 = MakeRoom("Troll Cave 2","Here lies a large troll. You wake him, and he blocks all exits to the room")
trollCaveRoom2.Actions.append(RoomAction("Attack Troll", "a", ResultType.DoorsOpen,"The Troll dies, and your weapon gets stuck in the troll."))
armory22.Item = Item(ItemType.Weapon,"small spiky mace")
AddConnection(sphynxRoom,emptyRoom21,'n')
AddConnection(emptyRoom21,pitFall,'e')
AddConnection(emptyRoom21,bankRoom,'n')
AddConnection(bankRoom,oldMarketplace,'n')
AddConnection(oldMarketplace,puzzleRoom21,'w')
AddConnection(puzzleRoom21,armory21, 's')
AddConnection(armory21,poisonDartHall21,'s')
AddConnection(oldMarketplace,emptyRoom22,'n')
AddConnection(emptyRoom22,sphynxRoom21,'w')
AddConnection(sphynxRoom21,armory22,'n')
 
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
    if CurrentRoom.InstantDeath:
        ProcessDeath()
        return
    print("There is a door to the ",end='')
    if CurrentRoom.ConnectionNorth is not None:
        print("n=North,",end='')
    if CurrentRoom.ConnectionEast is not None:
        print("e=East,",end='')
    if CurrentRoom.ConnectionSouth is not None:
        print("s=South,",end='')
    if CurrentRoom.ConnectionWest is not None:
        print("w=West,",end='')
    print('\b ')
    if CurrentRoom.Item is not None:
        print("Item found in room, p=pick up: "+ CurrentRoom.Item.Name )
    # if CurrentRoom.ChallengeType is not None:
    #     print("Challenge: ",CurrentRoom.ChallengeType)
    if len(CurrentRoom.Actions) >0:
        print("Available Actions: ",end='')
        counter = 1
        for a in CurrentRoom.Actions:
            print("a" + str(counter) + "=" + a.Name + ",",end='')
            counter +=1
        print('\b ')
    print(Fore.LIGHTBLACK_EX + "                Additional Commands: q=quit,i=inventory")

def ProcessAction(action):
    if CurrentRoom.AreDoorsOpen:
        print("Doors are already open")
        return
    if len(CurrentRoom.Actions) == 0:
        print("There are no actions to take in this room")
        return
    # if len(action) < 2 or action[0] != "a":
    #     print("invalid action, example: 'a1' or 'a3'")
    #     return
    # if len(action) == 0 or action[0] != "a":
    #     print("invalid action, must start with 'a'")
    #     return
    selectedAction = None
    for a in CurrentRoom.Actions:
        if a.Command == action:
            selectedAction = a
    if selectedAction is None:
        print("action '"+ action +"' is not valid")
        return
    if selectedAction.ResultType == ResultType.Die:
        print("oops, you did " + selectedAction.Name + ". " + CurrentRoom.Action.ResultDescription)
        ProcessDeath()
        return
    if selectedAction.ResultType == ResultType.DoorsOpen:
        if CurrentRoom.ChallengeType ==  ChallengeType.Monster:        
            if len(Inventory) == 0:
                print("You do not have an item in your inventory to use against the moster")
                return
            else:
                useditem = Inventory.pop()
                print("You used " + useditem)

        print(selectedAction.ResultDescription)
        print("The doors open")
        CurrentRoom.AreDoorsOpen = True


    # if CurrentRoom.Action is not None:
    #     if CurrentRoom.Action.ResultType == ResultType.Die:
    #         print("oops, you did " + CurrentRoom.Action.Name + ". " + CurrentRoom.Action.ResultDescription)
    #         ProcessDeath()
    #         return

    #     elif CurrentRoom.Action.ResultType == ResultType.DoorsOpen:
    #         print("You opened the doors")
    #         CurrentRoom.AreDoorsOpen = True
    # else:
    #     print("No actions available")

def ProcessCommand(command):
    global CurrentRoom
    global DefaultRoom
    validroomId = None
    command = command.lower()
    if command is None or len(command) < 1:
        raise Exception("invalid command")
    if command == "q":
        print("See ya, thanks for playing!")
        quit()
    elif command == "n":
        if CurrentRoom.ConnectionNorth is not None:
            validroomId = CurrentRoom.ConnectionNorth
        else:
            print("Can't move North")
    elif command == "e":
        if CurrentRoom.ConnectionEast is not None:
            validroomId = CurrentRoom.ConnectionEast
        else:
            print("Can't move East")
    elif command == "s": 
        if CurrentRoom.ConnectionSouth is not None:
            validroomId = CurrentRoom.ConnectionSouth
        else:
            print("Can't move South")
    elif command == "w":
        if CurrentRoom.ConnectionWest is not None:
            validroomId = CurrentRoom.ConnectionWest
        else:
            print("Can't move West")
    elif command == "i":
        if len(Inventory)>0 :
            print("Inventory:" + ','.join(str(i.Name) for i in Inventory))
        else:
            print("Inventory is empty")
    elif command == "p":
        if CurrentRoom.Item is not None:
            print(Fore.BLUE + "You have picked up a " + CurrentRoom.Item.Name)
            Inventory.append(CurrentRoom.Item)
            CurrentRoom.Item = None
        else:
            print("Nothing to pick up")
    elif len(command) > 0 and command[0] == "a": # example: a1
        ProcessAction(command)
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

DefaultRoom = entryHallRoom
#DefaultRoom = sphynxRoom # Default room after Death
CurrentRoom = DefaultRoom # Current room player is in

ProcessCurrentRoom()

while True:
    line = input()
    ProcessCommand(line)
