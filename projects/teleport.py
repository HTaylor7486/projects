import time,random,mcpi.minecraft as minecraft#imports moduals
mc = minecraft.Minecraft.create()#sets the minecraft modual to mc

time.sleep(5)#pauses the program
mc.postToChat("telport starting")#posts a message to chat
time.sleep(1)#pauses the program
mc.postToChat("Teleport in 3...")#posts a message to chat
time.sleep(1)#pauses the program
mc.postToChat("Teleport in 2...")#posts a message to chat
time.sleep(1)#pauses the program
mc.postToChat("Teleport in 1...")#posts a message to chat
time.sleep(1)#pauses the program
mc.postToChat("Teleport starting")#posts a message to chat
def rand():#defines a function
    a = random.randint(0,50)#sets a to a random number
    b = random.randint(0,50)#sets b to a random number
    c = random.randint(0,50)#sets c to a random number
    return a,b,c#returns a,b,c
def tel():#defines a function
    time.sleep(1)#pauses the program
    a,b,c = rand()#sets a,b,c to outcome of random 
    mc.player.setPos(a,b,c)#sets player position to a,b,c
    time.sleep(1)#pauses the program
    a,b,c = rand()#sets a,b,c to outcome of random
    mc.player.setPos(a,b,c)#sets player position to a,b,c
    time.sleep(1)#pauses the program
    a,b,c = rand()#sets a,b,c to outcome of random
    mc.player.setPos(a,b,c)#sets player position to a,b,c

while True:#starts infinte loop
    tel()#runs tel

time.sleep(2)#pauses the program
mc.postToChat("Teleport complete")#posts a message to chat

