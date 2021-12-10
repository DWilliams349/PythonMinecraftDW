import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def randomBlockLocations(blockType, repeats):
    count = 0
    while count <= repeats:
        x = random.randint(-127, 127)
        z = random.randint(-127, 127)
        y = mc.getHeight(x, z)
        mc.setBlock(x, y, z, blockType)
        count += 1
randomBlockLocations(57, 100)