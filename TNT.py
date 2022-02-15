from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x-1, y-1, z-1, x+1, y-100, z+1, 46, 1)