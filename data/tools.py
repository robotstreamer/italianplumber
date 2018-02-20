__author__ = 'justinarmstrong'

import os
import pygame as pg
import random
from threading import Thread
import _thread
from time import sleep
import traceback
import time
from urllib.request import urlopen
#import urllib2
import urllib
import json
#from socketIO_client import SocketIO, LoggingNamespace
import uuid
import asyncio
import websockets




keybinding = {
    'action':pg.K_s,
    'jump':pg.K_a,
    'left':pg.K_LEFT,
    'right':pg.K_RIGHT,
    'down':pg.K_DOWN
}


#Your Robot ID is 17442106
#Your Camera ID is 95898781

infoServer = 'robotstreamer.com:6001'
robotID = '103'


def startControl():
    print("waiting a few seconds")
    time.sleep(7) #todo: only wait as needed (wait for interent)
    print("restarting loop")
    time.sleep(0.25)
    try:
        asyncio.new_event_loop().run_until_complete(handleControlMessages())
    except:
        print("error")
        traceback.print_exc()


async def handleControlMessages():

    controlHost = "robotstreamer.com"
    port = getControlHostPort()['port']
    print("connecting to port:", port)
    url = 'ws://%s:%s/echo' % (controlHost, port)

    async with websockets.connect(url) as websocket:

        print("connected to control service at", url)
        print("control websocket object:", websocket)
        
        while True:

            print("awaiting control message")
            
            message = await websocket.recv()
            print("< {}".format(message))
            j = json.loads(message)
            print(j)
            _thread.start_new_thread(handle_command, (j,))
        
        

def getWithRetry(url):

    for retryNumber in range(2000):
        try:
            print("GET", url)
            response = urlopen(url).read()
            break
        except:
            print("could not open url", url)
            traceback.print_exc()
            time.sleep(2)

    return response


##def identifyRobotId():
##    chatSocketIO.emit('identify_robot_id', robotID);
   
    

def getControlHostPort():

    url = 'http://%s/v1/get_endpoint/rscontrol_robot/%s' % (infoServer, robotID)
    response = getWithRetry(url)
    return json.loads(response)

    

def getChatHostPort():

    #todo, use the api
    return {"host":"robotstreamer.com", "port":"6776"}
    
    url = 'http://%s/get_chat_host_port/%s' % (infoServer, robotID)
    response = getWithRetry(url)
    return json.loads(response)
    
    
    

globalControl = []    
controlHostPort = getControlHostPort() 
chatHostPort = getChatHostPort()
#chatHostPort = {'host':'https://runmyrobot.com', 'port':8000}


##print "connecting to control socket.io", controlHostPort
##controlSocketIO = SocketIO(controlHostPort['host'], controlHostPort['port'], LoggingNamespace)
##print "finished using socket io to connect to control host port", controlHostPort


##print "connecting to chat socket.io", chatHostPort
##chatSocketIO = SocketIO(chatHostPort['host'], chatHostPort['port'], LoggingNamespace)
##print "finished using socket io to chat control host port", chatHostPort


#identifyRobotId()


# def handle_chat_message(args):

    # print "chat message received:", args
    # rawMessage = args['message']
    # withoutName = rawMessage.split(']')[1:]
    # message = "".join(withoutName)
    # urlRegExp = "(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"
    # if message[1] == ".":
       # exit()
    # #elif commandArgs.anon_tts != True and args['anonymous'] == True:
    # #   exit()   
    # #elif commandArgs.filter_url_tts == True and re.search(urlRegExp, message):
    # #   exit()
    # else:
        # filename = 'temp_tts_' + str(uuid.uuid4())
        # f = open('c:\\temp\\' + filename, 'w')
        # f.write(message)
        # f.close()
        # os.system('cscript "C:\\Program Files\\Jampal\\ptts.vbs" -v 30 < c:\\temp\\' + filename)
        # os.unlink('c:\\temp\\' + filename)

##def on_handle_chat_message(*args):
##   thread.start_new_thread(handle_chat_message, args)
          



##def on_handle_command(*args):
##    thread.start_new_thread(handle_command, args)

##controlSocketIO.on('command_to_robot', on_handle_command)

##def gotChatConnection():
##    print "got connection for chat"
##    identifyRobotId()
 
##chatSocketIO.on('connect', gotChatConnection)
##chatSocketIO.on('chat_message_with_name', on_handle_chat_message)
#chatSocketIO.on('chat_message_with_name', x)

    
# def handle_command(args):
    # #print "received", args
    # if 'robot_id' in args and args['robot_id'] == robotID:
        # print "received message:", args
        # ##print globalControl
        # ##for c in globalControl:
        # ##    print "FAKE KEY", c.fakeKey

        # if args['command'] == 'L':
            # if args['key_position'] == 'down':
                # for c in globalControl:
                    # c.fakeKey = 276
                # pg.event.post(pg.event.Event(pg.KEYDOWN, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))

            # if args['key_position'] == 'up':
                # for c in globalControl:
                    # c.fakeKey = 276
                # pg.event.post(pg.event.Event(pg.KEYUP, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))

                
        # if args['command'] == 'R':
            # if args['key_position'] == 'down':
                # for c in globalControl:
                    # c.fakeKey = 275
                # pg.event.post(pg.event.Event(pg.KEYDOWN, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))

            # if args['key_position'] == 'up':
                # for c in globalControl:
                    # c.fakeKey = 275
                # pg.event.post(pg.event.Event(pg.KEYUP, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))
                
                
                
        # if args['command'] == 'F':
            # if args['key_position'] == 'down':
                # for c in globalControl:
                    # c.fakeKey = 97
                # pg.event.post(pg.event.Event(pg.KEYDOWN, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))

            # if args['key_position'] == 'up':
                # for c in globalControl:
                    # c.fakeKey = 97
                # pg.event.post(pg.event.Event(pg.KEYUP, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))

                
        # # no used for robotstreamer        
        # if args['command'] == 'stop':
            # print "UP"
            # for c in globalControl:
                # c.fakeKey = None
            # pg.event.post(pg.event.Event(pg.KEYUP, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))

def handle_command(args):
        print("received message:", args)
        ##print globalControl
        ##for c in globalControl:
        ##    print "FAKE KEY", c.fakeKey

        if args['command'] == 'L':
            if args['key_position'] == 'down':
                for c in globalControl:
                    c.fakeKey = 276
                pg.event.post(pg.event.Event(pg.KEYDOWN, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))

            if args['key_position'] == 'up':
                for c in globalControl:
                    c.fakeKey = 276
                pg.event.post(pg.event.Event(pg.KEYUP, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))

                
        if args['command'] == 'R':
            if args['key_position'] == 'down':
                for c in globalControl:
                    c.fakeKey = 275
                pg.event.post(pg.event.Event(pg.KEYDOWN, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))

            if args['key_position'] == 'up':
                for c in globalControl:
                    c.fakeKey = 275
                pg.event.post(pg.event.Event(pg.KEYUP, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))
                
                
                
        if args['command'] == 'F':
            if args['key_position'] == 'down':
                for c in globalControl:
                    c.fakeKey = 97
                pg.event.post(pg.event.Event(pg.KEYDOWN, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))

            if args['key_position'] == 'up':
                for c in globalControl:
                    c.fakeKey = 97
                pg.event.post(pg.event.Event(pg.KEYUP, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))

                
        # no used for robotstreamer        
        if args['command'] == 'stop':
            print("UP")
            for c in globalControl:
                c.fakeKey = None
            pg.event.post(pg.event.Event(pg.KEYUP, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))

        
    
def pressKeys(control):
    while False:
        #control.fakeKey = random.choice((97, 275))
        control.fakeKey = random.choice((97,))
        pg.event.post(pg.event.Event(pg.KEYDOWN, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))
        sleep(0.5)

        control.fakeKey = None
        pg.event.post(pg.event.Event(pg.KEYUP, {'scancode':30, 'key':97, 'unicode':u'a', 'mod':0}))
        sleep(0.5)


##def waitForControlServer():
##    while True:
##        print "control waiting"
##        controlSocketIO.wait(seconds=10)        

##def waitForChatServer():
##    while True:
##        print "chat waiting"
##        chatSocketIO.wait(seconds=10)        
        
        
    
class Control(object):
    """Control class for entire project. Contains the game loop, and contains
    the event_loop which passes events to States as needed. Logic for flipping
    states is also found here."""
    def __init__(self, caption):
        self.screen = pg.display.get_surface()
        self.done = False
        self.clock = pg.time.Clock()
        self.caption = caption
        self.fps = 60
        self.show_fps = False
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()
        self.state_dict = {}
        self.state_name = None
        self.state = None
        self.count = 0
        self.fakeKey = None
        
        #thread = Thread(target = pressKeys, args = (self, ))
        #thread.start()
        #thread = Thread(target = waitForControlServer, args = ())
        #thread.start()
        #thread.start_new_thread(waitForControlServer, ())
        #thread.start_new_thread(waitForChatServer, ())
        #thread.join()
        #thread.start_new_thread(pressKeys, (self,))

        _thread.start_new_thread(startControl, ())
        
        
        globalControl.append(self)


    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def update(self):
        self.current_time = pg.time.get_ticks()
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, self.keys, self.current_time)

    def flip_state(self):
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)
        self.state.previous = previous

    def event_loop(self):
        global count
        self.count += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                lst = list(pg.key.get_pressed())
                #lst[275] = random.randint(0, 1)
                if self.fakeKey is not None:
                    lst[self.fakeKey] = 1
                ##for i, value in enumerate(self.keys):
                ##   if value != 0:
                ##        print i, value
                #self.keys = pg.key.get_pressed()
                self.keys = lst
                self.toggle_show_fps(event.key)
                #self.toggle_show_fps(275)
                ##print  "EVENT", event
                ##print "key down", self.count, "self.keys", self.keys
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
                ##print  "EVENT", event
                ##print "key up", self.count, "self.keys", self.keys
            self.state.get_event(event)


    def toggle_show_fps(self, key):
        if key == pg.K_F5:
            self.show_fps = not self.show_fps
            if not self.show_fps:
                pg.display.set_caption(self.caption)


    def main(self):
        """Main loop for entire program"""
        while not self.done:
            #self.fakeKey = random.choice((97, 275))
            #pg.event.post(pg.event.Event(pg.KEYDOWN, {'unicode':'a', 'key':97, 'mod':0}))
            self.event_loop()
            self.update()
            pg.display.update()
            self.clock.tick(self.fps)
            if self.show_fps:
                fps = self.clock.get_fps()
                with_fps = "{} - {:.2f} FPS".format(self.caption, fps)
                pg.display.set_caption(with_fps)


class _State(object):
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.persist = {}

    def get_event(self, event):
        pass

    def startup(self, current_time, persistant):
        self.persist = persistant
        self.start_time = current_time

    def cleanup(self):
        self.done = False
        return self.persist

    def update(self, surface, keys, current_time):
        pass



def load_all_gfx(directory, colorkey=(255,0,255), accept=('.png', 'jpg', 'bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name]=img
    return graphics


def load_all_music(directory, accept=('.wav', '.mp3', '.ogg', '.mdi')):
    songs = {}
    for song in os.listdir(directory):
        name,ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    return songs


def load_all_fonts(directory, accept=('.ttf')):
    return load_all_music(directory, accept)


def load_all_sfx(directory, accept=('.wav','.mpe','.ogg','.mdi')):
    effects = {}
    for fx in os.listdir(directory):
        name, ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pg.mixer.Sound(os.path.join(directory, fx))
    return effects











