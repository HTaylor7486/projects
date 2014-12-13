#import time,random,picamera
name = ""#sets name to nothing
while name == "":#checks to see if name is = nothing
    name = input("what is your name? ---")#sets name to user input
#print("good morning " + name)
#print("Good morning %s" %name)
#print("Good morning {0}".format(name))
password = "hi_there"#sets password to hi_there
guess = input("{0} do you know the password --- ".format (name))#sets guess to user input
while guess != password: #checks to see if guess does not = password
    print("boooo")#prints booooo
    guess = input("{0} do you know the password --- ".format (name))#sets guess to user input
else:
    print("well done {0}".format (name))#prints message
    
