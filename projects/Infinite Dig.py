import time,mcpi.minecraft as minecraft #Imports Mojules
mc = minecraft.Minecraft.create() #Connects to Minecraft

while True:#starts infinite loop
    pos = mc.player.getPos()#stes pos as the players cooridinates
    x = pos.x#sets x to the x value gotten from players position
    y = pos.y#sets x to the x value gotten from players position
    z = pos.z#sets x to the x value gotten from players position
    if y < -10:#checks to see if the y cooridinates
        mc.player.setPos(x,y+20,z)#teleports the player to 10 blocks above their current position
