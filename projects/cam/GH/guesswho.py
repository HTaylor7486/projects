import picamera,time,json#imports moduals
def getpic(name="null"):#defines function
    try:#trys to run code block
        with picamera.PiCamera() as camera:#runs code block with the pi cam
            q = "n"#sets q to n
            while q == "n":#starts loop 
                camera.start_preview()#starts cam preview
                time.sleep(3)#pauses the program
                camera.capture("{0}.jpeg".format (name))#takes a pic with and sets it to name.jpeg
                camera.stop_preview()#stops cam preview
                q = input("is the image okay? (y/n) ")#sets q to user input
                filename = ("{0}.jepg".format (name))#sets file name to name.jepg
        print("Your file is called {0}.jpeg".format (name))#prints message
        return filename
    except picamera.exc.PicameraMMALError:#if code block gives this error run block beneath
        print("Your camera is not working please connect and restart the program")#prints message

def getchar():#defines function
    name = "h"#sets name to nothing
    while name == "":  #checks to see#checks if name is = to nothing
        name = input("what is your name?")#prints message
    hair = "blonde"#sets hair to nothing
    while not hair in ["blonde","brown","ginger","no hair"]:#checks to see if hair is =  to something on a list
        hair = input ("what hair colour do you have? (blonde/brown/ginger/no hair)")#sets hair to user input
    hat = "y"#sets hat to nothing
    while not hat in ["y","n"]:#checks to see if hat is =  to something on a list
        hat = input("do you have a hat? (y/n)")#sets hat to user input
    eye = "green"#sets eye to nothing
    while not eye in ["green","brown","blue"] :#checks to see if eye is =  to something on a list
        eye = input("what is your eye colour")#sets eye to user input
    gender = "m"#sets gender to nothing
    while not gender in ["m","f"] :#checks to see if gender is =  to something on a list
        gender = input("what is your gender?(m/f)")#sets gender to user input
    fhair = "n"#sets fhair to nothing
    while not fhair in ["y","n"]:#checks to see if fahir is =  to something on a list
        fhair = input("do you have facial hair?(y/n)")#sets fhair to user input
    glass = "y"#sets glass to nothing
    while not glass in ["y","n"]:#checks to see if glass is =  to something on a list
        glass = input("do you have glasses?(y/n)")#sets glass to user input
    charprof = [name,hair,hat,eye,gender,fhair,glass]#sets charprof to list of all chars 
    getpic(name)#runs getpic wit name
    return charprof
        
def save(x):
    prof = getchar()
    x.append(prof)
    with open("profiles.txt",mode = "w") as my_file:
        json.dump(charprof,my_file)
        
def load():
    try:
        with open("profiles.txt",mode = "r") as my_file:
            charprof = json.load(my_file)
    except IOError:
        print("No profiles found, making new")
        charprof = []
    print(charprof)
    return charprof

charprof = load()
save(charprof)
