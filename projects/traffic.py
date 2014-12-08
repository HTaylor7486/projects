import time,mcpi.minecraft as minecraft,mcpi.block as Block
mc = minecraft.Minecraft.create()

#mc.player.setPos(0,0,0)
black = 7
red = 14
yellow = 1
green = 5

#x = 0
#y = 0
#z = 0
def tra(x,y,z):
    mc.setBlock(x,y,z,35,black)
    mc.setBlock(x,y+1,z,35,black)
    mc.setBlock(x,y+2,z,35,black)
    mc.setBlock(x,y+3,z,35,black)
    mc.setBlock(x,y+4,z,35,black)
    mc.setBlock(x,y+5,z,35,black)
def red(x,y,z):
    mc.setBlock(x,y+5,z,35,red)
def gre(x,y,z):
    mc.setBlock(x,y+3,z,35,green)
def yel(x,y,z):
    mc.setBlock(x,y+4,z,35,yellow)
def final(x,y,z):
    tra(x,y,z)
    red(x,y,z)
    time.sleep(5)
    yel(x,y,z)
    time.sleep(2)
    tra(x,y,z)
    gre(x,y,z)
    time.sleep(5)
    tra(x,y,z)
    yel(x,y,z)
    time.sleep(4)
#final(x,y,z)

#mc.setBlock(x,y,z,35,black)
#mc.setBlock(x,y+1,z,35,black)
#mc.setBlock(x,y+2,z,35,black)
#mc.setBlock(x,y+3,z,35,black)
#mc.setBlock(x,y+4,z,35,black)
#mc.setBlock(x,y+5,z,35,black)
def tra1():
    mc.setBlock(0,0,0,35,black)
    mc.setBlock(0,1,0,35,black)
    mc.setBlock(0,2,0,35,black)
    mc.setBlock(0,3,0,35,black)
    mc.setBlock(0,4,0,35,black)
    mc.setBlock(0,5,0,35,black)
def red1():
    mc.setBlock(0,5,0,35,red)
def gre1():
    mc.setBlock(0,3,0,35,green)
def yel1():
    mc.setBlock(0,4,0,35,yellow)

def final1():
    tra1()
    red1()
    time.sleep(5)
    yel1()
    time.sleep(2)
    tra1()
    gre1()
    time.sleep(5)
    tra1()
    yel1()
    time.sleep(4)
while True:
    final1()



    
