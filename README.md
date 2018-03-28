
Super Mario Bros Level 1 from justinmeister adapted to run on robotstreamer.com by rgiuly



This game is an example of how to interface with robotstreamer. It uses websockets to communicate.



To stream video, which is done with a separate script (using old_send_video in the robostreamer/robotstreamer repo) here's bat file I use in Windows to keep it running:

:loop
rem python runmyrobot/old_send_video.py 84736686 0 --screen-capture --kbps 250 --audio-input-device "Microphone (HD Webcam C270)"
python robotstreamer/old_send_video.py 203 0 --screen-capture --kbps 250 --audio-input-device "Microphone (HD Webcam C270)"
timeout 2
goto loop

Note: My screen is made available as a camera input to make this work.




=============

Notes on the game:

An attempt to recreate the first level of Super Mario Bros.

![screenshot](https://raw.github.com/justinmeister/Mario-Level-1/master/screenshot.png)

CONTROLS: 

Arrow keys for direction

'a' for jump

's' for action (fireball, run)


DEPENDENCIES:

Pygame 1.9.1 (Python 2)

Pygame 1.9.2 (Python 3) - a little trickier to get going.

To install dependencies for Python 2.x:

	pip install -r requirements.txt

VIDEO DEMO:

http://www.youtube.com/watch?v=HBbzYKMfx5Y
   
DISCLAIMER:

This project is intended for non-commercial educational purposes.
