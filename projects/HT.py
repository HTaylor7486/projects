import mcpi.minecraft as minecraft,time#impots moduals
mc = minecraft.Minecraft.create()#sets the minecraft modual to mc
#x,y,z = mc.player.getPos()
x = int(raw_input("please enter x"))#sets x to an interger that is gotten from the user
y = int(raw_input("please enter y"))#sets y to an interger that is gotten from the user
z = int(raw_input("please enter z"))#sets z to an interger that is gotten from the user
def h(x,y,z):#makes a function called h
    mc.setBlocks(x+2,y,z,x+2,y+6,z,35,5)#sets blocks at the coordinates asked for + some set values
    mc.setBlocks(x+6,y,z,x+6,y+6,z,35,5)#sets blocks at the coordinates asked for + some set values
    mc.setBlocks(x+3,y+3,z,x+5,y+3,z,35,5)#sets blocks at the coordinates asked for + some set values
def t(x,y,z):#makes a function called t
    mc.setBlocks(x+2,y,z,x+10,y+5,z,35,5)#sets blocks at the coordinates asked for + some set values
    mc.setBlocks(x+8,y+6,z,x+12,y+6,z,35,5)#sets blocks at the coordinates asked for + some set values
def l(x,y,z):#makes a function called l
    mc.setBlocks(x+2,y,z,x+2,y+6,z,35,5)#sets blocks at the coordinates asked for + some set values
    mc.setBlocks(x+3,y,z,x+6,y,z,35,5)#sets blocks at the coordinates asked for + some set values
l(x,y,z)#calls the function l
h(x,y,z)#calls the function h
t(x,y,z)#calls the function t
