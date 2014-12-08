import time,random,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
while True:#starts infinite loop
    x,y,z = mc.player.getPos()#sets xyz to the players position
    mc.setBlock(float(x+random.randint(-10,10)),50,float(z+random.randint(-10,10)),random.randint(12,13))#sets x and z to x/z plus a random number
