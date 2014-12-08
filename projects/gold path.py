import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
while True:
    x,y,z = mc.player.getPos()
    block = mc.getBlock(x,y-1,z)
    
    if block == 0:
        pass
    else:
        mc.setBlock(x,y-1,z,41)
        
    
