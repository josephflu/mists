import math
import sys
from enum import Enum

print("Welcome to Mists of Horizon.")
print("You enter a small empty room.")
print("Choices: n = North, e = East, q = Quit")

levelmap = {"e":"East", "n":"North", "s": "South", "w":"West"}

class Room:
    RoomID = 0
    RoomType = None
    ConnectionNorth = None
    ConnectionSouth = None
    ConnectionEast = None
    ConnectionWest = None

    def DoStuff(self, var2):
        self.X = self.X + 1

#myroom = Room(4)
#myroom.DoStuff(1)

class RoomType(Enum):
     Troll = 1
     Sphynx = 2
     PoisonDart = 3

#print(repr(RoomType.Troll))


def parse(arg):
    print("you chose: {}".format(arg))
    if line == "q":
        print("See ya, thanks for playing!")
        quit()
    if line == "e":
        print("You enter the dragon's layer. you win")
    if line == "n":
        print("You enter the pit of dispair. You lose. you are back at the begining")

def f(x):
    return {
        'a': 1,
        'b': 2 
    }.get(x, 9)

myvar = f('c')

while True:
    line = input()
    parse(line)

# dictionary with default value get.
def f(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)

myvar = f('c')

#print items in Dictionary
for item in RoomDict:
    print(item + " " + str(RoomDict[item].RoomType))


#levelmap = {"e":"East", "n":"North", "s": "South", "w":"West"}


#print("This is the name of the script: ", sys.argv[0])

# if len(sys.argv) > 1 :
#     print("2nd arg: ", sys.argv[1]) 

# print("Number of arguments: ", len(sys.argv))
# print("The arguments are: " , str(sys.argv))

# #const cars = ["🚗", "🚙", "🚕🚕🚕"];

# print("hi")

# myvar = ""

# x = 5
# y = 7=
# print(x + y)

# print("The value of PI is approximately {!r}.".format(x))

