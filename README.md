# blinkhome


Purpose: periodically take pictures from all cameras so we can make a time lapse video

# Prereqs
- python3 (or python2)
- blinkpy installed via pip
```
pip3 install blinkpy
```
- Runs on Windows, Linux, and MacOS.


# How to run
```
python3 main.py
```

- It's a simple script that you need to run once manually.
- The blinkpy package prompts for username/password/2fa, then this script saves the resulting creds in a file name saved_secrets.json in the same directory.
- The next time the script runs, it will just load up those creds and run without needing user input.


# Extending
- Right now it is hard-coded to take a picture every 10 seconds, but that could be made variable very easily.




# Convert images to video

Use ffmpeg command line
```
sudo apt install ffmpeg -y
ffmpeg -framerate 30 -pattern_type glob -i 'Patio*.jpg' -c:v libx264 -pix_fmt yuv420p out.mp4
```
