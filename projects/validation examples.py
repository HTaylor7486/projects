#import time,random,picamera
name = ""
while name == "":
    name = input("what is your name? ---")
#print("good morning " + name)
#print("Good morning %s" %name)
#print("Good morning {0}".format(name))
password = "hi_there"
guess = input("{0} do you know the password --- ".format (name))
while guess != password: 
    print("boooo")
    guess = input("{0} do you know the password --- ".format (name))
else:
    print("well done {0}".format (name))
    
