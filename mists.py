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


def MakeRoom(roomId,description,challengeType):
    newroom = Room(roomId,description,challengeType)
    RoomDict[roomId] = newroom
    return newroom


#--- Level 1 Rooms
entryHallRoom = MakeRoom("Entry Hall", "You stand on a sandy beach outside the lair of a Great Dragon. ",ChallengeType.NoChallenge)
emptyRoom1 = MakeRoom("Empty Room 1", "There is a great hall filled with art mostly depicting a large dragon. What looks like it was a map has been burned, and ripped beyond repair.",ChallengeType.NoChallenge)
puzzleRoom1 = MakeRoom("Puzzle Room 1", "You have entered a puzzle room.",ChallengeType.Puzzle)
puzzleRoom1.Actions.append(RoomAction("Solve Puzzle","1", ResultType.DoorsOpen,"You solved the sphynx puzzle. Nice Job, yes we are going to make this part harder, don't worry."))
cryptRoom = MakeRoom("Crypt Room", "You walk into a crypt filled with many coffins. They look like they have beeen here for thousands of years.",ChallengeType.MakeDiscovery)
cryptRoom.Actions.append(RoomAction("Open Casket","1",ResultType.Die,"A spirit drifts upward, and enters you, it compels you to enter the largest tomb, and close it. When you gain control of your body again you find that you are locked inside. You suffocate to death."))
treasureRoom = MakeRoom("Treasure Room", "Here is a room with a pillar in the center. On it is a bag full of coins.",ChallengeType.NoChallenge)
treasureRoom.Item = Item(ItemType.Money, "bag of coins")
emptyRoom2 = MakeRoom("Empty Room 2", "You enter an empty room.",ChallengeType.NoChallenge)
goblinCrossingRoom = MakeRoom("Goblin Crossing", "Ahead you see a large bridge.",ChallengeType.Monster)
goblinCrossingRoom.Actions.append(RoomAction("Give Goblin Coins", "1", ResultType.DoorsOpen,"The Goblin steps aside and lets you pass."))
emptyRoom3 = MakeRoom("Empty Room 3", "You enter an empty room.",ChallengeType.NoChallenge)
trollCaveRoom = MakeRoom("Troll Cave","Here lies a large troll. You wake him, and he blocks the way forward.",ChallengeType.Monster)
trollCaveRoom.Actions.append(RoomAction("Attack Troll","1", ResultType.DoorsOpen,"The Troll dies, and your weapon gets stuck in the troll."))
armoryRoom = MakeRoom("Armory Room","There is an abandoned Armory here. The armor racks are all empty, with the exception of one rusted Dagger",ChallengeType.NoChallenge)
armoryRoom.Item = Item(ItemType.Weapon,"Rusted Dagger")
emptyRoom4 = MakeRoom("Empty Room 4", "You enter an empty room.",ChallengeType.NoChallenge)
sphynxRoom = MakeRoom("Sphynx Room", "Here lies a large sphynx. All doors close and the sphynx tells you a riddle.",ChallengeType.Puzzle)
sphynxRoom.Actions.append(RoomAction("Solve Puzzle","1", ResultType.DoorsOpen,"You solved the sphynx puzzle. Nice Job, yes we are going to make this part harder, don't worry."))
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
emptyRoom21 = MakeRoom("Empty Room 2.1","#### ENTERING LEVEL 2 ####\n Welcome to Level 2! You enter an empty Room",ChallengeType.NoChallenge)
emptyRoom21.IsFirstOfLevel = True
pitFall21 = MakeRoom("Pitfall Room 2.1","While walking into this room the floor drops and you die", ChallengeType.DieImmediately)
bankRoom = MakeRoom("Bank Room","A huge vast room lies ahead. As you step into this establishment, you hear the echo of your feet on marble floors. There is a vault here, but it looks like it requires a key.",ChallengeType.NoChallenge)
oldMarketplace21 = MakeRoom("Old Marketplace","This large square room is what looks like was once a vast marketplace. The smell of rotting fruit corrodes the air.",ChallengeType.NoChallenge)
puzzleRoom21 = MakeRoom("Puzzle Room 2.1","Solve puzzle ...",ChallengeType.Puzzle)
puzzleRoom21.Actions.append(RoomAction("Solve Puzzle","1", ResultType.DoorsOpen,"You solved the sphynx puzzle. Nice Job, yes we are going to make this part harder, don't worry."))
armory21 = MakeRoom("Armory 2.1","There is an abandoned Armory here. The armor racks are all empty, with the exception of an old bow and arrow",ChallengeType.NoChallenge)
armory21.Item = Item(ItemType.Weapon,"Bow and Arrow")
poisonDartHall21 = MakeRoom("Poison Dart Hall","There are many statues in this hall. While looking at a statue a dart comes flying out of his mouth and strikes you, as do many others from around you.",ChallengeType.DieImmediately)
emptyRoom22 = MakeRoom("Empty Room 2.2","You enter an empty room.",ChallengeType.NoChallenge)
sphynxRoom21 = MakeRoom("Sphynx Room 2.1", "Here lies a large sphynx. All doors close and the sphynx tells you a riddle.",ChallengeType.Puzzle)
sphynxRoom21.Actions.append(RoomAction("Solve Puzzle", "1", ResultType.DoorsOpen,"You solved the sphynx puzzle. Nice Job, yes we are going to make this part harder, don't worry."))
armory22 = MakeRoom("Armory 2.2","There is an abandoned Armory here. The armor racks are all empty, with the exception of a small spiky mace",ChallengeType.NoChallenge)
armory22.Item = Item(ItemType.Weapon,"small spiky mace")
trollCaveRoom21 = MakeRoom("Troll Cave 2.1","Here lies a large troll. You wake him, and he blocks the way forward.",ChallengeType.Monster)
trollCaveRoom21.Actions.append(RoomAction("Attack Troll", "1", ResultType.DoorsOpen,"The Troll dies, and your weapon gets stuck in the troll."))
puzzleRoom22 = MakeRoom("Puzzle Room 2.2","Solve puzzle ...",ChallengeType.Puzzle)
puzzleRoom22.Actions.append(RoomAction("Solve Puzzle","1", ResultType.DoorsOpen,"You solved the sphynx puzzle. Nice Job, yes we are going to make this part harder, don't worry."))
galleryRoom21 = MakeRoom("Old Gallery", "Strange colorful art covers the walls. The vigor has not drained out of these paintings, and it looks untouched by time",ChallengeType.MakeDiscovery)
galleryRoom21.Actions.append(RoomAction("Search Room", "1", ResultType.DoorsOpen,"While looking cloesly at the paintingd you reach out to touch one. it moves and shakes slightly. Behind it you discover a seceret pasage leading east."))
undergroundGarden = MakeRoom("Underground Garden","In this silent room lies glowing strange plants, nothing overgrown, it looks like it was trimmed just yesterday.",ChallengeType.NoChallenge)
undergroundGarden.Actions.append(RoomAction("carefully feel plant","1",ResultType.Die,"The flower-shaped plant you decide to touch first explodes in a ball of acid, disintegrating you."))
undergroundGarden.Actions.append(RoomAction("examine plants","2",ResultType.Die,"One of the plants draws your attention, and you find yourself fixated on its butiflul tendrils. As you brush one of them, the plant explodes in a ball of acid, disintegrating you."))
armory23 = MakeRoom("Armory 2.3", "There is an abandoned Armory here. The armor racks are all empty, with the exception of a short rusty sword.",ChallengeType.NoChallenge)
armory23.Item = Item(ItemType.Weapon,"short rusty sword")
pitFall22 = MakeRoom("Pitfall Room 2.2","While walking into this room the floor drops and you die", ChallengeType.DieImmediately)
traproom21 = MakeRoom("Trap room","You enter a square room with crushed bones on the ground. Before you can think of much else, the doors close and lock. the ceiling starts to fall, crushing you to death.", ChallengeType.DieImmediately)
AddConnection(sphynxRoom,emptyRoom21,'n')
AddConnection(emptyRoom21,pitFall21,'e')
AddConnection(emptyRoom21,bankRoom,'n')
AddConnection(bankRoom,oldMarketplace21,'n')
AddConnection(oldMarketplace21,puzzleRoom21,'w')
AddConnection(puzzleRoom21,armory21, 's')
AddConnection(armory21,poisonDartHall21,'s')
AddConnection(oldMarketplace21,emptyRoom22,'n')
AddConnection(emptyRoom22,sphynxRoom21,'w')
AddConnection(sphynxRoom21,armory23,'n')
AddConnection(armory23,trollCaveRoom21,'e')
AddConnection(trollCaveRoom21,galleryRoom21,'e')
AddConnection(trollCaveRoom21,puzzleRoom22,'n')
AddConnection(undergroundGarden,armory22,'s')
AddConnection(oldMarketplace21,undergroundGarden,'e')
AddConnection(undergroundGarden,pitFall22,'n')
AddConnection(emptyRoom22,pitFall22,'e')
AddConnection(galleryRoom21,pitFall22,'s')
AddConnection(galleryRoom21,traproom21,'n')

# --- Level S1 Rooms
trollCaveroomS1 = MakeRoom("Troll Cave S.1","#### ENTERING SECERET LEVEL ####\n Here lies a large troll. You wake him, and he blocks the way forward.",ChallengeType.Monster)
trollCaveroomS1.Actions.append(RoomAction("Attack Troll", "1", ResultType.DoorsOpen,"The Troll dies, and your weapon gets stuck in the troll."))
puzzleRoomS1 = MakeRoom("Puzzle Room S.1","Solve puzzle ...",ChallengeType.Puzzle)
puzzleRoomS1.Actions.append(RoomAction("Solve Puzzle","1", ResultType.DoorsOpen,"You solved the sphynx puzzle. Nice Job, yes we are going to make this part harder, don't worry."))
sphynxRoomS1 = MakeRoom("Sphynx Room S.1", "Here lies a large sphynx. All doors close and the sphynx tells you a riddle.",ChallengeType.Puzzle)
sphynxRoomS1.Actions.append(RoomAction("Solve Puzzle", "1", ResultType.DoorsOpen,"You solved the sphynx puzzle. Nice Job, yes we are going to make this part harder, don't worry."))
emptyRoomS1 = MakeRoom("Empty Room S.1","You enter an empty room.",ChallengeType.NoChallenge)
AddConnection(galleryRoom21,trollCaveroomS1,'e')
AddConnection(trollCaveroomS1,puzzleRoomS1,'e')
AddConnection(puzzleRoomS1,sphynxRoomS1,'e')
AddConnection(sphynxRoomS1,emptyRoomS1,'e')

# --- Process Current Room
def ProcessDeath():
    global CurrentRoom
    print(Fore.RED + 'YOU DIED!')
    CurrentRoom = DefaultRoom
    ProcessCurrentRoom()

def ProcessCurrentRoom():
    print()
    print(Fore.BLUE + "                ####### " + CurrentRoom.RoomID + " #######")
    print(CurrentRoom.Description)
    if CurrentRoom.ChallengeType == ChallengeType.DieImmediately:
        ProcessDeath()
        return
    print("There is a door to the ",end='')
    if CurrentRoom.ConnectionNorth is not None:
        print("n=North({}),".format(CurrentRoom.IsOpen('n')),end='')
    if CurrentRoom.ConnectionEast is not None:
        print("e=East({}),".format(CurrentRoom.IsOpen('e')),end='')
    if CurrentRoom.ConnectionSouth is not None:
        print("s=South({}),".format(CurrentRoom.IsOpen('s')),end='')
    if CurrentRoom.ConnectionWest is not None:
        print("w=West({}),".format(CurrentRoom.IsOpen('w')),end='')
    print('\b ')

    if CurrentRoom.IsDefeated:
        if CurrentRoom.ChallengeType == ChallengeType.Monster:
            print("This monster has been defeated")
        elif CurrentRoom.ChallengeType == ChallengeType.Puzzle:
            print("This puzzle has been defeated")
    if CurrentRoom.Item is not None:
        print("Item found in room, p=pick up: " + CurrentRoom.Item.Name)
    if len(CurrentRoom.Actions) >0:
        print("Available Actions: ",end='')
        for a in CurrentRoom.Actions:
            print(a.Command + "=" + a.Name + ",",end='')
        print('\b ')

    print(Fore.LIGHTBLACK_EX + "                Additional Commands: q=quit,i=inventory")

def ProcessAction(action):
    global CurrentRoom
    if len(CurrentRoom.Actions) == 0:
        print("There are no actions to take in this room")
        return
    selectedAction = None
    for a in CurrentRoom.Actions:
        if a.Command == action:
            selectedAction = a
    if selectedAction is None:
        print("action '"+ action +"' is not valid for this room")
        return
    elif CurrentRoom.ChallengeType == ChallengeType.Monster:
        if CurrentRoom.IsDefeated:
            print("monster already defeated")
            return
        if len(Inventory) == 0:
            print("You do not have an item in your inventory to use against the monster")
            return
        else:
            useditem = Inventory.pop()
            print("You used " + useditem.Name)
    elif CurrentRoom.ChallengeType == ChallengeType.Puzzle:
        if CurrentRoom.IsDefeated:
            print("puzzle already solved")
            return
        #print("You solved the puzzle!")
    elif CurrentRoom.ChallengeType == ChallengeType.MakeDiscovery:
        if selectedAction.ResultType == ResultType.Die:
            print("oops, you did " + selectedAction.Name + ". " + selectedAction.ResultDescription)
            ProcessDeath()
            return        
        print("You made a discovery!")
    else:
        raise Exception("invalid challenge/action")
    
    print(selectedAction.ResultDescription)
    print("The doors open")
    CurrentRoom.IsDefeated = True
    #ProcessCurrentRoom()

def ProcessMovement(direction):
    global CurrentRoom,DefaultRoom
    validroomId = None
    if direction == "n":
        if CurrentRoom.ConnectionNorth is not None:
            validroomId = CurrentRoom.ConnectionNorth
        else:
            print("Can't move North")
    elif direction == "e":
        if CurrentRoom.ConnectionEast is not None:
            validroomId = CurrentRoom.ConnectionEast
        else:
            print("Can't move East")
    elif direction == "s": 
        if CurrentRoom.ConnectionSouth is not None:
            validroomId = CurrentRoom.ConnectionSouth
        else:
            print("Can't move South")
    elif direction == "w":
        if CurrentRoom.ConnectionWest is not None:
            validroomId = CurrentRoom.ConnectionWest
        else:
            print("Can't move West")
    if validroomId is not None:
        if CurrentRoom.IsDoorOpen(direction):
            CurrentRoom = RoomDict[validroomId]
            if CurrentRoom.IsFirstOfLevel:
                DefaultRoom = CurrentRoom
            ProcessCurrentRoom()
        else:
            print("Door is closed")
 
def ProcessCommand(command):
    global CurrentRoom
    global DefaultRoom
    validroomId = None
    command = command.lower()
    if command is None or len(command) < 1:
        print("invalid empty command")
    elif command == "q":
        print("See ya, thanks for playing!")
        quit()
    elif command in ["n","e","s","w"]:
        ProcessMovement(command)
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
    elif  command.isdigit(): # example: 1
        ProcessAction(command)
    else:
        print("Invalid command")


# --- Initialize and Start Game
print("Welcome to Mists of Horizon.")
print("Fearlessly you approach the dragon's lair. You know that what comes next could result in great pain, but you are determined to stop the dragon, to save your city and country. To avenge your family. ")

#DefaultRoom = entryHallRoom
DefaultRoom = armory23
#DefaultRoom = oldMarketplace21
#DefaultRoom = sphynxRoom # Default room after Death
CurrentRoom = DefaultRoom # Current room player is in

ProcessCurrentRoom()

while True:
    line = input()
    ProcessCommand(line)
