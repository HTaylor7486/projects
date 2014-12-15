import mcpi.minecraft as minecraft,time#imports modual
mc = minecraft.Minecraft.create()#sets the minecraft modual to mc

x,y,z = mc.player.getPos()sets players postion to x,y,z
def house(x,y,z):#makes a function called house with the paraminters x,y,z
    mc.setBlocks(x+1,y,z+1,x+5,y+4,z+7,5)#sets blocks
    mc.setBlocks(x+2,y+1,z+2,x+4,y+3,z+6,0)#sets blocks
    mc.setBlocks(x+3,y+1,z+1,x+3,y+2,z+1,0)#sets blocks
    mc.setBlocks(x+2,y,z+1,x+4,y,z+6,45)#sets blocks
    #mc.setBlocks(x,y,z,x,y,z,)
for h in (0,8,16,24,32):#sets h to a list of numbers for eveytime the program runs
    for f in (0,10,20,30):#sets f to a list of numbers for eveytime the program runs
        for g in (-5,1,7,13):#sets g to a list of numbers for eveytime the program runs
            house(h,g,f)#runs the house function
