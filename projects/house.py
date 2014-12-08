import mcpi.minecraft as minecraft,time
mc = minecraft.Minecraft.create()

x,y,z = mc.player.getPos()
def house(x,y,z):
    mc.setBlocks(x+1,y,z+1,x+5,y+4,z+7,5)
    mc.setBlocks(x+2,y+1,z+2,x+4,y+3,z+6,0)
    mc.setBlocks(x+3,y+1,z+1,x+3,y+2,z+1,0)
    mc.setBlocks(x+2,y,z+1,x+4,y,z+6,45)
    #mc.setBlocks(x,y,z,x,y,z,)
for h in (0,8,16,24,32):
    for f in (0,10,20,30):
        for g in (-5,1,7,13):
            house(h,g,f)
