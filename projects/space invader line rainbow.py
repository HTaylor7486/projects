import time,mcpi.minecraft as minecraft,random
mc = minecraft.Minecraft.create()
def rand():
    r = random.randint(0,15)
    return r
def spaced(h,x,y,z):
    r = rand()
    for b in (3,9):
        mc.setBlock(x-6+b,15+h,z+12,35,r)
    r = rand()
    for b in (4,8):
        mc.setBlock(x-6+b,14+h,z+12,35,r)
    r = rand()
    for b in (3,4,5,6,7,8,9):
        mc.setBlock(x-6+b,13+h,z+12,35,r)
    r = rand()
    for b in (2,3,5,6,7,9,10):
        mc.setBlock(x-6+b,12+h,z+12,35,r)
    r = rand()
    for b in (1,2,3,4,5,6,7,8,9,10,11):
        mc.setBlock(x-6+b,11+h,z+12,35,r)
    r = rand()
    for b in (1,3,4,5,6,7,8,9,11):
        mc.setBlock(x-6+b,10+h,z+12,35,r)
    r = rand()
    for b in (1,3,9,11):
        mc.setBlock(x-6+b,9+h,z+12,35,r)
    r = rand()
    for b in (4,5,7,8):
            mc.setBlock(x-6+b,8+h,z+12,35,r)
def spaceu(h,x,y,z):
    r = rand()
    for b in (3,9):
        mc.setBlock(x-6+b,15+h,z+12,35,r)
    r = rand()
    for b in (1,4,8,11):
        mc.setBlock(x-6+b,14+h,z+12,35,r)
    r = rand()
    for b in (1,3,4,5,6,7,8,9,11):
        mc.setBlock(x-6+b,13+h,z+12,35,r)
    r = rand()
    for b in (1,2,3,5,6,7,9,10,11):
        mc.setBlock(x-6+b,12+h,z+12,35,r)
    r = rand()
    for b in (1,2,3,4,5,6,7,8,9,10,11):
        mc.setBlock(x-6+b,11+h,z+12,35,r)
    r = rand()
    for b in (2,3,4,5,6,7,8,9,10):
        mc.setBlock(x-6+b,10+h,z+12,35,r)
    r = rand()
    for b in (3,9):
        mc.setBlock(x-6+b,9+h,z+12,35,r)
    r = rand()
    for b in (2,10):
        mc.setBlock(x-6+b,8+h,z+12,35,r)
h = 30
while True:
    x,y,z = mc.player.getTilePos()
    spaced(h,x,y,z)
    time.sleep(0.5)
    a,b,c = mc.player.getTilePos()
    mc.setBlocks(x-6,8+h,z+12,x+6,16+h,z+12,0)
    if h > 12:
        h = h -1
    else:
        pass
    x,y,z = mc.player.getTilePos()
    spaceu(h,x,y,z)
    time.sleep(0.5)
    a,b,c = mc.player.getTilePos()
    mc.setBlocks(x-6,8+h,z+12,x+6,16+h,z+12,0)
    if h > 12:
        h = h -1
    else:
        mc.setBlock(x,8+h,z+12,13)
#   if x != a or y != b or z != c:
#   else:
#       pass
#random.randrange


