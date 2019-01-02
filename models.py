from enum import Enum

#--- Define Room Class
class ResultType(Enum):
    Die = 0            # Instantly Die
    DoorsOpen = 1      # Doors in the current room open

class RoomAction:
    def __init__(self,name,command,resultType,resultDescription):
        self.Name = name
        self.Command = command
        self.ResultType = resultType    
        self.ResultDescription = resultDescription

class ChallengeType(Enum):
    NoChallenge=0
    Monster=1 # Use item on monster to defeat and open doors
    Puzzle=2  # Answer a puzzle to open doors
    DieImmediately=3 # If an action is taken, die
    MakeDiscovery=4  # find a hidden door or item

class ItemType:
    Weapon=0 # Weapon to fight Enemy
    Money=1    # Money

class Item:
    def __init__(self,itemType,name):
        self.ItemType = itemType
        self.Name = name

class Room:
    def __init__(self,roomId,description,challengeType):
        self.RoomID = roomId
        self.Description = description
        self.ConnectionNorth = None
        self.ConnectionSouth = None
        self.ConnectionEast = None
        self.ConnectionWest = None
        self.Item = None
        self.Actions = []
        self.IsFirstOfLevel = False
        self.ChallengeType = challengeType
        self.IsDefeated = (challengeType != ChallengeType.Puzzle) and (challengeType != ChallengeType.Monster)
        self.EntryDoor = None

    def IsDoorOpen(self,direction):
        return direction == self.EntryDoor or self.IsDefeated
    
    def IsOpen(self,direction):
        if self.IsDoorOpen(direction):
            return "open"
        return "closed"

def AddConnection(room1,room2,direction):
    if direction == 'n':
        room1.ConnectionNorth = room2.RoomID
        room2.ConnectionSouth = room1.RoomID        
    elif direction == 'e':
        room1.ConnectionEast = room2.RoomID
        room2.ConnectionWest = room1.RoomID
    elif direction == 's':
        room1.ConnectionSouth = room2.RoomID
        room2.ConnectionNorth = room1.RoomID
    elif direction == 'w':
        room1.ConnectionWest = room2.RoomID
        room2.ConnectionEast = room1.RoomID
    else:
        raise Exception("{} is not a valid direction".format(direction))
    opposite = {'n':'s','e':'w','s':'n','w':'e'}
    if room2.EntryDoor is None:
        room2.EntryDoor = opposite[direction] #set entry door



