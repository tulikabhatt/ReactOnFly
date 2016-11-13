# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 15:33:54 2016

@author: strider
"""

import pygame, pygame.camera, time
from werkzeug.utils import secure_filename
import os, flask, json
from flask import Flask, request, render_template, session, redirect 
from flask import send_from_directory, url_for, make_response

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
    #var = 0
    for i in range(0,5):
        filename="filename"+str(i)+".jpg"
        getEmotion(filename)
    return json.dumps({"value":True})
    

def getEmotion(filename):
    return json.dumps({"value":True})    



@application.route('/')
def main():
    #getImages()   
    return flask.jsonify(getImages())


    
if __name__ == "__main__":
  application.secret_key = os.urandom(24)
  application.run(threaded=True, ssl_context=('ssl.cert', 'ssl.key'))
