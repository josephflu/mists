from enum import Enum

#--- Define Room Class
class ResultType(Enum):
    Die = 0            # Instantly Die
    DoorsOpen = 1      # Doors in the current room open
    SetDefaultRoom = 2 # After passing a level, the default room after death changes

class RoomAction:
    def __init__(self,name,resultType,resultDescription):
        self.Name = name
        self.ResultType = resultType    
        self.ResultDescription = resultDescription

class ItemType:
    Weapon=0 # Weapon to fight Enemy
    Money=1    # Money

class Item:
    def __init__(self,itemType,name):
        self.ItemType = itemType
        self.Name = name

class Room:
    def __init__(self,roomId,description,areDoorsOpen=True):
        self.RoomID = roomId
        self.Description = description
        self.ConnectionNorth = None
        self.ConnectionSouth = None
        self.ConnectionEast = None
        self.ConnectionWest = None
        self.Item = None
        self.Action = None
        self.AreDoorsOpen = areDoorsOpen
        self.InstantDeath = False
        self.IsFirstOfLevel = False

    def DisplayId(self):
        print(self.RoomID)


def AddConnection(room1,room2, direction):
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


