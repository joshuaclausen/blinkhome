


from time import sleep
from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
from blinkpy.helpers.util import json_load
from datetime import datetime
from time import sleep


blink = Blink()
auth = Auth(json_load("./saved_secrets.json"))
blink.auth = auth
blink.start()




blink.save("./saved_secrets.json")

while(True):
    for name, camera in blink.cameras.items():
        print(name)                   # Name of the camera
        print(camera.attributes)      # Print available attributes of camera
        camera = blink.cameras[''+ name + '']
        camera.snap_picture()
        blink.refresh()
        now = datetime.now()
        cur_time = now.strftime("%Y_%m_%d_%H_%M_%S")
        camera.image_to_file('./' + name + '_' + cur_time +'.jpg')

    sleep(30)


