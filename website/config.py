import pyrebase
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import json
import subprocess
import tensorflow as tf
import os
import cherrypy

from selenium import webdriver
# import time
# import urllib
#import urllib2


class fbRetrieval:
    @cherrypy.expose
    def index(self):
        """ config = {
        "apiKey": "AIzaSyANEnG7bpr74E6UoLeJFSrs0IU0epZEqEg",
        "authDomain": "doodlepad-8ca23.firebaseapp.com",
        "databaseURL": "https://doodlepad-8ca23.firebaseio.com/",
        "storageBucket": "doodlepad-8ca23.appspot.com",
        "serviceAccount": "/home/kiran24/Downloads/doodlepad-8ca23-firebase-adminsdk-3hbyu-d457f2485e.json"
        }
        firebase_admin.initialize_app(config) """

        cred = credentials.Certificate(
            '/home/kiran24/Downloads/doodlepad-8ca23-firebase-adminsdk-3hbyu-d457f2485e.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://doodlepad-8ca23.firebaseio.com/'
        })

      #auth = firebase.auth()
        output = db.reference("doodlepad-8ca23").get()
      #output = json.loads(output)
        s = output.get("jsonStr")
        #print("Hello World")
        # print(s)
        #output = exec(open('/home/kiran24/Documents/CS490/Semester-Project-490/Semester-Project-490/website/test.py').read())
        return s
    @cherrypy.expose
    def loadPage(self):
      x=raw_input("http://127.0.0.1:8080/")
      driver = webdriver.Chrome()
      driver.get(x)


if __name__ == '__main__':
    cherrypy.quickstart(fbRetrieval())
