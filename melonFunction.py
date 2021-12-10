from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

def melon():
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlock(x, y -1, z, 103)
    

for x in range(100):
    melon()
