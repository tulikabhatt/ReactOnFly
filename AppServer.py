# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 15:33:54 2016

@author: strider
"""

import pygame, pygame.camera, time
import os, flask, json, storefilesintoazure, emotioncog
from flask import Flask, request


application = Flask(__name__)

def getImages():
    pygame.camera.init()
    cam = pygame.camera.Camera("/dev/video0",(640,480))
    cam.start()
    for i in range(0,5):
        time.sleep(2)
        img = cam.get_image()
        filename="filename"+str(i)+".jpg"
        pygame.image.save(img,filename)
    cam.stop()
    storefilesintoazure.saveFile()
    #var = 0
    getEmotion()
    return json.dumps({"value":True})
    

def getEmotion():
    count = 0
    for i in range(0,5):
        link="https://reactonfly.blob.core.windows.net/images/myblockblob"+str(i)
        if(emotioncog.processLinkForEmotion(link)):
            count = count + 1
    if count>=3:
        return json.dumps({"value":True})
    else:
        return json.dumps({"value":True})



@application.route('/')
def main():
    #getImages()   
    return flask.jsonify(getImages())


    
if __name__ == "__main__":
  application.secret_key = os.urandom(24)
  application.run(threaded=True, ssl_context=('ssl.cert', 'ssl.key'))
