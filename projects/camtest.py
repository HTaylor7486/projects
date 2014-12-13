import picamera,time#imports moduals
for run in range(5):#sets run to 1-5 every time block runs
    name = input('please enter your name')#sets name to user input
    with picamera.PiCamera() as camera:#sets picam modual to camera
        camera.resolution = (1024,768)#sets cam resalution
        camera.start_preview()#starts preview
        
        time.sleep(2)#pauses the program
        camera.capture( name +'.jpeg')#takes photo and names it to your name .jpeg
