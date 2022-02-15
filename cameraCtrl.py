from time import sleep
from picamera import PiCamera
import datetime 

camera = PiCamera()

def take_still():
    camera.start_preview()
    sleep(1)
    out_file_name = str(datetime.datetime.now())
    out_file_name = 'pictures/'+out_file_name[:-7]+'.jpg'
    camera.capture(out_file_name)
    return
