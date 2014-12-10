import picamera,time#imports moduals
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
    name = "1"
    while name == "":  
        name = input("what is your name?")
    hair = "blonde"
    while not hair in ["blonde","brown","ginger","no hair"]:
        hair = input ("what hair colour do you have? (blonde/brown/ginger/no hair)")
    hat = "y"
    while not hat in ["y","n"]:
        hat = input("do you have a hat? (y/n)")
    eye = "green"
    while not eye in ["green","brown","blue"] :
        eye = input("what is your eye colour")
    gender = "m"
    while not gender in ["m","f"] :
        gender = input("what is your gender?(m/f)")
    fhair = "y"
    while not fhair in ["y","n"]:
        fhair = input("do you have facial hair?(y/n)")
    glass = "y"
    while not glass in ["y","n"]:
        glass = input("do you have glasses?(y/n)")
    charprof = [name,hair,hat,eye,gender,fhair,glass]
    getpic(name)
    return charprof
def save():
    prof = getchar()
    with open("profiles.txt",mode = "a", encoding = "utf-8") as my_file:
        for item in prof:
            my_file.write(item+",")
        my_file.seek(-1)
        my_file.write("\n")
