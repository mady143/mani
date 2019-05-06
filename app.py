import time
import webbrowser
import csv
from autocorrect import spell
import spell_func
import fuzzy_example
import fuzzy_cat
#import app_tfidf

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
# english_bot.train("./data")

df_cat = pd.read_csv('parent.csv')
documents = df_cat['category_name']
categories = df_cat['category_name'].tolist()
sub_cat = df_cat['subcat_name'].tolist()
main_url = 'https://www.arogyarahasya.com/catalogsearch/result/?q={}'
product_csv = pd.read_csv('AR_Data_Product.csv')
pro = product_csv['pro_name'].tolist()
product_id = product_csv['product_id'].tolist()
#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")
s = requests.session()  
Session_API = "http://magento.arogyarahasya.com/restapi/rest_mage/getSession"
payload = {
   'api_user' : 'launchship',
   'api_key' :'JVYR5UJASE0SHOGW'
   }
r = s.post(Session_API, params=payload)
#print(r.url)
r = r.json()

bot_dict = {}
@app.route("/")
def home():
    return render_template("index1.html")
@app.route("/get")
#def get_bot_response():
    #userText = request.args.get('msg')
    #return str(english_bot.get_response(userText))
def get_bot_response():

    
    main_url = 'https://www.arogyarahasya.com/catalogsearch/result/?q={}'
    while True:
         a = request.args.get('msg')
         print("AAA",a)
         spell_correct = a.split()
         spell_correct = [spell(i) for i in spell_correct]
         a = ' '.join(spell_correct)
         print('aa',a)
         if a in categories:
             bot = spell_func.spell_correct(a)
         elif a not in categories:
           bot_dict['categories'] = fuzzy_cat.home(a)
           bot_dict['products'] = fuzzy_example.home(a)
           print("bot",bot_dict)
           product_list = bot_dict['products'].split('&&')
           product_list = filter(None, product_list)
           #print("product_list", product_list)
           if product_list:
              product = [ product.replace(" ", '+') for product in product_list]
              product = [i.strip('"') for i in product]
              product_url = [ main_url.format(i) for i in product]
              str2 = '&&'.join(product_url)
              bot_dict['products'] = str2
           print("bot_values", bot_dict.values())
           cat = '&&'.join(str(values) for values in bot_dict.values() if values)
           bot = '&&'+cat
           print("catt",cat)
           if bot == '&&':
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
   a = request.args.get('msg')
   print("cart_input",a)

   qty = request.args.get('quantity')
   print("qty", qty)
   
   i = [j for i, j in zip(pro, product_id) if a in i]
   print('p_id', i)
   p_id = i[0]
   SID =  r['session_id']
   print('SID', SID)
   payload = {
   'product_id':  p_id,
   'qty': qty,
   'SID': SID
    }
   updatecart_api = "http://magento.arogyarahasya.com/restapi/rest_cart/updateCart/"
   cart = requests.post(updatecart_api, params = payload)
   cart_info = cart

   #get_cart = "http://magento.arogyarahasya.com/restapi/rest_cart/getCart"
   #get_cart = s.get(get_cart, params=SID)
   #print("get_cart",get_cart.url)
   #print("cart_response",cart.status_code)
   SID = {'SID': r['session_id']}
   checkout_api = "https://magento.arogyarahasya.com/checkout/cart/"
   check = requests.post(checkout_api, params = SID)
   
   #print(check.json())
   #https://magento.arogyarahasya.com/checkout/?SID=38bogjm191utc0vngggeon44to
   cart_response = check.url
   return cart_response

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


# support@doselect.com
