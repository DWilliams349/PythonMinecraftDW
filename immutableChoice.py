from mcpi.minecraft import Minecraft
mc = Minecraft.create()
a = input("Do you want the blocks to be immutable? Y/N ")
if a == "Y":
    mc.setting("world_immutable", True)
    mc.postToChat("world_is_immutable")
else:
    mc.setting("world_immutable", False)
    mc.postToChat("world_is_mutable")