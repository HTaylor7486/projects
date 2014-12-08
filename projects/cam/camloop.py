import picamera,time
def getpic(name="null"):
    try:
        with picamera.PiCamera() as camera:
            q = "n"
            while q == "n":
                camera.start_preview()
                time.sleep(3)
                camera.capture("{0}.jpeg".format (name))
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

