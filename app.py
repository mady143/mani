# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
# from __future__ import unicode_literals

# import argparse
# import warnings
# import time
import webbrowser

# import nltk
from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# import re

# from flask import Flask, render_template, request
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer

# from rasa_core import utils
# from rasa_core.agent import Agent
# from rasa_core.interpreter import RasaNLUInterpreter
# #from rasa_core.channels.console import ConsoleInputChannel


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

app = Flask(__name__)



english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)
# english_bot.train("./data")


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
    url_text = a.split()
 
    keywords = ['search', 'want', 'show', 'open','need','buy']
    stop_words = set(stopwords.words('english'))
    product_list = ['almonds', 'almond oil', 'face wash', 'honey', 'flax seed oil capsules',
                'hair oils','utensils','soaps','cow products', 'beauty care','perfumes','green tea','ginger tea','lemon tea','masala tea']
    # brands_list  = []
    data = pd.read_csv("AR_Parents.csv")
    cat = list(data['category_name'])
    sub_cat = list(data['parents_name'])
    # print(dd)
   

    if a in cat:
        for m,n in zip(cat, sub_cat):
            if a == m:
                b = ast.literal_eval(n)
                b = '&'.join(b)
                url = main_url.format(b)
                bot = b

    elif a in product_list:
        str1 = a.split()
        str1 = '+'.join(str1)
        url = main_url.format(str1)
        bot =url
        # webbrowser.open(url)
    elif any(i in keywords for i in url_text):
        stop_words.update(['search', 'open','show','want','need','some','buy'])
        filtered_sentence = [w for w in url_text if not w in stop_words] 
        str1 = '+'.join(filtered_sentence)
        url = main_url.format(str1)
        bot = url
       
    else:
        text =  str(english_bot.get_response(a))
        bot  = text
        b = {"converstaions":[[a,bot]]}
        with open("chat.yml","a") as outfile:
            yaml.dump(b["converstaions"],outfile,default_flow_style=False)
    return bot
  
            
@app.route("/get_speech")

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