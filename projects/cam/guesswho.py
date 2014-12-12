import picamera,time,json#imports moduals
def getpic(name="null"):#defines function
    try:#trys to run code block
        with picamera.PiCamera() as camera:#runs code block with the pi cam
            q = "n"#sets q to n
            while q == "n":#starts loop 
                camera.start_preview()#starts cam preview
                time.sleep(3)#pauses the program
                camera.capture("{0}.jpeg".format (name))#takes a pic with and sets 
                camera.stop_preview()
                q = input("is the image okay? (y/n) ")
                filename = ("{0}.jepg".format (name))
        print("Your file is called {0}.jpeg".format (name))
        return filename
    except picamera.exc.PicameraMMALError:
        print("Your camera is not working please connect and restart the program")

def getchar():
    name = ""
    while name == "":  
        name = input("what is your name?")
    hair = ""
    while not hair in ["blonde","brown","ginger","no hair"]:
        hair = input ("what hair colour do you have? (blonde/brown/ginger/no hair)")
    hat = ""
    while not hat in ["y","n"]:
        hat = input("do you have a hat? (y/n)")
    eye = ""
    while not eye in ["green","brown","blue"] :
        eye = input("what is your eye colour")
    gender = ""
    while not gender in ["m","f"] :
        gender = input("what is your gender?(m/f)")
    fhair = ""
    while not fhair in ["y","n"]:
        fhair = input("do you have facial hair?(y/n)")
    glass = ""
    while not glass in ["y","n"]:
        glass = input("do you have glasses?(y/n)")
    charprof = [name,hair,hat,eye,gender,fhair,glass]
    getpic(name)
    return charprof
        
def save():
    charprof = getchar()
    with open("profiles.txt",mode = "w") as my_file:
        json.dump(charprof,my_file)
save()
