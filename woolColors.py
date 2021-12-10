from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def getWoolState(color):
    if color == "pink":
        blockState = 6
    elif color == "purple":
        blockState = 10
    elif color == "orange":
        blockState = 1
    elif color == "green":
        blockState = 13
    elif color == "red":
        blockState = 14
    elif color == "blue":
        blockState = 11
    return blockState
        
colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)
    