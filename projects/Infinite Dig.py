import time,mcpi.minecraft as minecraft #Imports Mojules
mc = minecraft.Minecraft.create() #Connects to Minecraft

while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    if y < -10:
        mc.player.setPos(x,y+20,z)
