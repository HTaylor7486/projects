import picamera,time#iports moduals
name = input('please enter your name')#sets name to user input
with picamera.PiCamera() as camera:#sets picam modual to camera
    camera.resolution = (1024,768)#sets resolution
    camera.start_preview()#starts preview

    time.sleep(2)#pauses the program
    camera.capture( name +'.jpeg')#captures picture
