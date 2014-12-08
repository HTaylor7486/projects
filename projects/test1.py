import mcpi.minecraft as minecraft,time,random#imports stuff
mc = minecraft.Minecraft.create()#makes connection

mc.setBlocks(-30,-5,-30,30,30,30,0)#clears large section

for b in range(15):#makes a list of numbers
    for b2 in range(15):
        mc.postToChat(b)#posts b to chat
        mc.setBlock(b,b2,0,35,b)#makes a rainbow out of wool
        time.sleep(0.1)#pauses the program for 2 seconds
