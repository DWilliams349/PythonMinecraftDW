from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x, y, z, x - 15, y-15, z-15, 15)
mc.setBlocks(x-1, y-1, z-1, x-14, y-14, z-14, 0)
mc.setBlocks(x-1, y-1, z-1, x-14, y-14, z-14, 152)