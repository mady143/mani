from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import warnings
import time
import webbrowser
import csv
import pandas as pd
import ast
import soundex
import nltk
import requests 
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
#import wordsegment
#from wordsegment import segment

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


import requests 
from autocorrect import spell
import spell_func
import fuzzy_example
import fuzzy_cat
#import app_tfidf
import warnings
import ruamel.yaml
import webbrowser
from nltk.corpus import stopwords
import speech_recognition as sr
from chatterbot import ChatBot
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import yaml
import urllib3
import json
import sys
import pandas as pd
import ast
import requests
from autocorrect import spell
from metaphone import doublemetaphone
app = Flask(__name__)



english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("./data")

df_cat = pd.read_csv('parent.csv')
documents = df_cat['category_name']
categories = df_cat['category_name'].tolist()
sub_cat = df_cat['subcat_name'].tolist()

product_csv = pd.read_csv('AR_Data_Product.csv')
pro = product_csv['pro_name'].tolist()
product_id = product_csv['product_id'].tolist()

url = "http://magento.arogyarahasya.com/restapi/rest_mage/getSession"
payload = {
    'api_user' : "launchship",
    'api_key' : "JVYR5UJASE0SHOGW"
    }
response_session = requests.post(url,data= payload)
ss = response_session.json()
session_id = ss["session_id"]
# print(session_id)


@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
#def get_bot_response():
    #userText = request.args.get('msg')
    #return str(english_bot.get_response(userText))
def get_bot_response():
    
    main_url = 'https://www.arogyarahasya.com/catalogsearch/result/?q={}'
    
    a = request.args.get('msg')
    # print("AAA",a)
    chat_input = a.split()
    # print("Chat-input", chat_input)
    if a in categories:
       bot = spell_func.spell_correct(a)
       # print("bot",bot)
    elif a not in categories:
       #bot = app_tfidf.tfidf(a)
       bot = fuzzy_cat.home(a)
       # print("a not in categories", bot)
       if len(bot)== 5:
          responses = str(english_bot.get_response(a))
          bot = responses
          b = {"converstaions":[[a,bot]]}
          with open("chat.yml","a") as outfile:
            yaml.dump(b["converstaions"],outfile,default_flow_style=False)
          
    else:
        text =  str(english_bot.get_response(a))
        bot  = text
        b = {"converstaions":[[a,bot]]}
        with open("chat.yml","a") as outfile:
            yaml.dump(b["converstaions"],outfile,default_flow_style=False)
    return bot



@app.route("/get_cart")
def add_to_cart():
   checkout_url = "https://magento.arogyarahasya.com/checkout/cart/?SID={}"
   a = request.args.get('msg')
   # print("cart_input",a)
   p_id = [j for i, j in zip(pro, product_id) if a in i]
   # print("i",p_id)
   id1 = p_id[0]
   # print(id1)
  
   cart_url = "http://magento.arogyarahasya.com/restapi/rest_cart/updateCart"
   param = {

        'product_id':id1,
        'qty'       :1,
        'SID':session_id

   }
   response_cart    = requests.post(cart_url,params = param)
   bot = checkout_url.format(session_id)
   return bot
@app.route("/get_speech")
# def cart():
    
def return_audio():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration =1)
            print("say something:")
            audio = r.listen(source) 
            message = r.recognize_google(audio)
            print("You Said:",message)
            return message
            # text =  str(english_bot.get_response(message))
            # bot  = text
            # webbrowser.open(bot)
            # return bot

if __name__ == "__main__":
    app.run()


# support@doselect.com
