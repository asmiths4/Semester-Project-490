import pyrebase
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import json
import subprocess
import tensorflow as tf
import os


""" config = {
  "apiKey": "AIzaSyANEnG7bpr74E6UoLeJFSrs0IU0epZEqEg",
  "authDomain": "doodlepad-8ca23.firebaseapp.com",
  "databaseURL": "https://doodlepad-8ca23.firebaseio.com/",
  "storageBucket": "doodlepad-8ca23.appspot.com",
  "serviceAccount": "/home/kiran24/Downloads/doodlepad-8ca23-firebase-adminsdk-3hbyu-d457f2485e.json"
}
firebase_admin.initialize_app(config) """

cred = credentials.Certificate('/home/kiran24/Downloads/doodlepad-8ca23-firebase-adminsdk-3hbyu-d457f2485e.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://doodlepad-8ca23.firebaseio.com/'
})

#auth = firebase.auth()
output = db.reference("doodlepad-8ca23").get()
#output = json.loads(output)
s = output.get("jsonStr")
print(s)
subprocess.call("python3 /home/kiran24/Documents/CS490/Semester-Project-490/Semester-Project-490/train_model.py \ --classes_file=/home/kiran24/Documents/CS490/Semester-Project-490/tf_class_file/training.tfrecord.classes \
 --training_data=/home/kiran24/Documents/CS490/Semester-Project-490/tf_output_data/training.tfrecord-?????-of-????? \ --eval_data=/home/kiran24/Documents/CS490/Semester-Project-490/tf_output_data/eval.tfrecord-?????-of-????? \
 --predict_for_data="+s+" --predict_temp_file=/home/kiran24/Documents/CS490/Semester-Project-490/Semester-Project-490/predict_temp.tfrecord --cell_type=cudnn_lstm", shell=True)
