from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x = 100
y = 10
z = 100

mc.player.setTilePos(x, y, z)

time.sleep(10)

x = 75
y = 44
z = 75

mc.player.setTilePos(x, y, z)

  
