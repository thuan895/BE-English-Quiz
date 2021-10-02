from django.shortcuts import render
from Quiz.firebasechild import datachild
from .models import *
from django.shortcuts import redirect
import pyrebase
from django.contrib import admin
from bson import json_util

# Create your views here.

config = {
    "apiKey": "AIzaSyAm7qlHSpKUKLRFH46Ia7sicGdBBRa8_7o",
    "authDomain": "englishquiz-b52bc.firebaseapp.com",
    "databaseURL": "https://englishquiz-b52bc-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "projectId": "englishquiz-b52bc",
    "storageBucket": "englishquiz-b52bc.appspot.com",
    "messagingSenderId": "511928079334",
    "appId": "1:511928079334:web:9272551d367e034da3fc27",
    "measurementId": "G-20EGKY2N75"
  }

firebase=pyrebase.initialize_app(config)
auth = firebase.auth()
database=firebase.database()
