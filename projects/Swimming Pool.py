import time,mcpi.minecraft as Minecraft #Imports Mojules
mc = Minecraft.Minecraft.create() #Connects to Minecraft
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x,y,z,x+10,y+3,z+25,20) #Builds the tank
mc.setBlocks(1,9,1,24,11,9,9) #Installs the water
