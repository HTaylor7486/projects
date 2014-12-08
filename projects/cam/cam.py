import time,picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    for filename in camera.capture(''+'.jpeg'):
        print('captured %s' % filename)
        
