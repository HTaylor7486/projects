import time,mcpi.minecraft as minecraft#imports moduals
mc = minecraft.Minecraft.create()#sets the minecraft modual to mc
while True:#starts infinite loop
    x,y,z = mc.player.getPos()#sets the players coords to x,y,z
    block = mc.getBlock(x,y-1,z)#finds out what the block is below the player and sets it to block
    
    if block == 0:#checks if block is = to 0
        pass#does nothing
    else:
        mc.setBlock(x,y-1,z,41)#sets block to gold
        
    
