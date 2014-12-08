import time,mcpi.minecraft as minecraft#impots time and minecraft api
mc = minecraft.Minecraft.create()

while True:#sets loop
    pos = mc.player.getPos()#gets position
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlocks(x-1,y,z-1,x+1,y+1,z+1,0)#sets all the blocks around the player to air
        
