from flask import Flask
from firebase import firebase
 
app = Flask(__name__)
FIREBASE_URL = 'https://nabsdemo.firebaseio.com/'
app.config['FIREBASE_URI'] = FIREBASE_URL
firebase = firebase.FirebaseApplication(FIREBASE_URL, None)
 
from markov_sim.user.views import nabs
app.register_blueprint(nabs)
 
# db.create_all()