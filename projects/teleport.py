import time,random,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

time.sleep(5)
mc.postToChat("telport starting")
time.sleep(1)
mc.postToChat("Teleport in 3...")
time.sleep(1)
mc.postToChat("Teleport in 2...")
time.sleep(1)
mc.postToChat("Teleport in 1...")
time.sleep(1)
mc.postToChat("Teleport starting")
def rand():
    a = random.randint(0,50)
    b = random.randint(0,50)
    c = random.randint(0,50)
    return a,b,c
def tel():
    time.sleep(1)
    a,b,c = rand()
    mc.player.setPos(a,b,c)
    time.sleep(1)
    a,b,c = rand()
    mc.player.setPos(a,b,c)
    time.sleep(1)
    a,b,c = rand()
    mc.player.setPos(a,b,c)

while True:
    tel()

time.sleep(2)
mc.postToChat("Teleport complete")

