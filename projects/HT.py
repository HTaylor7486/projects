import mcpi.minecraft as minecraft,time
mc = minecraft.Minecraft.create()
#x,y,z = mc.player.getPos()
x = int(raw_input("please enter x"))
y = int(raw_input("please enter y"))
z = int(raw_input("please enter z"))
def h(x,y,z):
    mc.setBlocks(x+2,y,z,x+2,y+6,z,35,5)
    mc.setBlocks(x+6,y,z,x+6,y+6,z,35,5)
    mc.setBlocks(x+3,y+3,z,x+5,y+3,z,35,5)
def t(x,y,z):
    mc.setBlocks(x+2,y,z,x+10,y+5,z,35,5)
    mc.setBlocks(x+8,y+6,z,x+12,y+6,z,35,5)
def l(x,y,z):
    mc.setBlocks(x+2,y,z,x+2,y+6,z,35,5)
    mc.setBlocks(x+3,y,z,x+6,y,z,35,5)
l(x,y,z)
h(x,y,z)
t(x,y,z)
