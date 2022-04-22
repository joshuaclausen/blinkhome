# prereq is the blinkpy package installed via pip3
# pip3 install blinkpy
# run this with "python3 main.py"


from time import sleep
from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
from blinkpy.helpers.util import json_load
from datetime import datetime
from time import sleep

# init
blink = Blink()

# load the auth file - if the file doesn't exist, it just asks for creds
# later we save the file use future use
auth = Auth(json_load("./saved_secrets.json"))

# authorize with blink
blink.auth = auth

# start things up
blink.start()


# save the auth file, now that we've logged in
blink.save("./saved_secrets.json")


# now do an infinite loop
while(True):

    # loop through all cameras in the account
    for name, camera in blink.cameras.items():
        print(name)                   # Name of the camera
        print(camera.attributes)      # Print available attributes of camera

        # load up the current camera - note we are concatenating the camera name - it didn't work without doing it this way
        camera = blink.cameras['' + name + '']

        # tell the camera to take a new picture
        camera.snap_picture()

        # refresh with the blink service, so later we can get the image
        blink.refresh()

        # get the current time, so we can add it to the file name
        now = datetime.now()
        cur_time = now.strftime("%Y_%m_%d_%H_%M_%S")

        # get the image and save it as a new file with the timestamp
        camera.image_to_file('./' + name + '_' + cur_time +'.jpg')

    # wait awhile
    sleep(10)


