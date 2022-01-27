from mcpi.minecraft import Minecraft
mc = Minecraft.create()

toDoList = open("toDoFile.txt", "r")

for line in toDoList:
    mc.postToChat(toDoFile.read())