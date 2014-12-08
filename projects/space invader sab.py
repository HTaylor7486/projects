import time,mcpi.minecraft as minecraft,random#imports moduals
mc = minecraft.Minecraft.create()#makes connection to game
def spaced(h,x,y,z):#makes function
    r = random.randint(0,15)#sets random number
    for b in (3,9):
        mc.setBlock(x-6+b,15+h,z+12,35,r)
    for b in (4,8):
        mc.setBlock(x-6+b,14+h,z+12,35,r)
    for b in (3,4,5,6,7,8,9):
        mc.setBlock(x-6+b,13+h,z+12,35,r)
    for b in (2,3,5,6,7,9,10):
        mc.setBlock(x-6+b,12+h,z+12,35,r)
    for b in (1,2,3,4,5,6,7,8,9,10,11):
        mc.setBlock(x-6+b,11+h,z+12,35,r)
    for b in (1,3,4,5,6,7,8,9,11):
        mc.setBlock(x-6+b,10+h,z+12,35,r)
    for b in (1,3,9,11):
        mc.setBlock(x-6+b,9+h,z+12,35,r)
    for b in (4,5,7,8):
            mc.setBlock(x-6+b,8+h,z+12,35,r)
def spaceu(h,x,y,z):#defines function
    r = random.randint(0,15)#sets random number
    for b in (3,9):
        mc.setBlock(x-6+b,15+h,z+12,35,r)
    for b in (1,4,8,11):
        mc.setBlock(x-6+b,14+h,z+12,35,r)
    for b in (1,3,4,5,6,7,8,9,11):
        mc.setBlock(x-6+b,13+h,z+12,35,r)
    for b in (1,2,3,5,6,7,9,10,11):
        mc.setBlock(x-6+b,12+h,z+12,35,r)
    for b in (1,2,3,4,5,6,7,8,9,10,11):
        mc.setBlock(x-6+b,11+h,z+12,35,r)
    for b in (2,3,4,5,6,7,8,9,10):
        mc.setBlock(x-6+b,10+h,z+12,35,r)
    for b in (3,9):
        mc.setBlock(x-6+b,9+h,z+12,35,r)
    for b in (2,10):
        mc.setBlock(x-6+b,8+h,z+12,35,r)
h = 30#sets h to 30
while True:#starts infinte loop
    x,y,z = mc.player.getTilePos()#gets players position
    spaced(h,x,y,z)#runs spaced function
    time.sleep(0.5)#pauses the program
    a,b,c = mc.player.getTilePos()#gets a seond set of the player coordinates
    mc.setBlocks(x-6,8+h,z+12,x+6,16+h,z+12,0)#clears space invader
    if h > 12:#checks to see if h is smaller than 12
        h = h -1#takes 1 away from h if it is smaller than 12
    else:
        pass
    x,y,z = mc.player.getTilePos()#gets players coordinates
    spaceu(h,x,y,z)#runs spaseu
    time.sleep(0.5)#pauses the program
    a,b,c = mc.player.getTilePos()#gets a second set of the players coordinates
    mc.setBlocks(x-6,8+h,z+12,x+6,16+h,z+12,0)#clears the space invader
    if h > 12:#checks h again
        h = h -1#takes 1 away from h if it is smaller than 12
    else:
        mc.setBlock(x,8+h,z+12,13)#if h is smaller than 12 places a gravel block

