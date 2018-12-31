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
    Monster=0 # Use item on monster to defeat and open doors
    Puzzle=1  # Answer a puzzle to open doors
    DieImmediately=2 # If an action is taken, die
    MakeDiscovery=3  # find a hidden door or item

class ItemType:
    Weapon=0 # Weapon to fight Enemy
    Money=1    # Money

class Item:
    def __init__(self,itemType,name):
        self.ItemType = itemType
        self.Name = name

class Room:
    def __init__(self,roomId,description,challengeType=None):
        self.RoomID = roomId
        self.Description = description
        self.ConnectionNorth = None
        self.ConnectionSouth = None
        self.ConnectionEast = None
        self.ConnectionWest = None
        self.Item = None
        self.Actions = []
        self.AreDoorsOpen = challengeType != ChallengeType.Puzzle and challengeType != ChallengeType.Monster
        self.InstantDeath = False
        self.IsFirstOfLevel = False
        self.ChallengeType = challengeType

    def DisplayId(self):
        print(self.RoomID)


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


