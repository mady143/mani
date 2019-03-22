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
# english_bot.train("./data")

url = "http://magento.arogyarahasya.com/restapi/rest_mage/getSession"
payload = {
    'api_user' : "launchship",
    'api_key' : "JVYR5UJASE0SHOGW"
    }
response_session = requests.post(url,data= payload)
ss = response_session.json()
session_id = ss["session_id"]
print(session_id)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")

def get_bot_response():

    main_url = 'https://www.arogyarahasya.com/catalogsearch/result/?q={}'
    checkout_url = 'https://www.arogyarahasya.com/checkout/?SID={}'
    a = request.args.get('msg')
    # print("a",a)
    b = a.split()
    c = [spell(a) for a in b]
    d = " ".join(c)
    
    # a = doublemetaphone(a)
    url_text = d.split()
 
    keywords = ['search', 'want', 'show', 'open','need','buy']
    stop_words = set(stopwords.words('english'))

    data1 = pd.read_csv("AR_All.csv")
    cat_name = list(data1['category_name'])

    product_list = []

    for i in cat_name:
        rt=[w.lower() for w in i]
        str3 = ''.join(rt)
        # print(str3)
        if str3 not in product_list:
            product_list.append(str3)

    product_list = ['almonds', 'almond oil', 'face wash', 'honey', 'flax seed oil capsules',
                'hair oils','utensils','soaps','cow products', 'beauty care','perfumes','green tea','ginger tea','lemon tea','masala tea']



    data = pd.read_csv("AR_Parents.csv")
    cat = list(data['category_name'])
    sub_cat = list(data['parents_name'])
    # print(dd)
   

    if any(s.lower() == a.lower() for s in cat):
        for m,n in zip(cat, sub_cat):
            if a.casefold() == m.casefold():
                
                b = ast.literal_eval(n)
                
                data_products_name = pd.read_csv("AR_All.csv")
                pro_name = list(data_products_name['pro_name'])
                # print("products",pro_name)
                if not b:
                    c = [i for i in pro_name if a in i]
                   
                    b = [ x.replace(" ", '+') for x in c]
                    
                    d = [ main_url.format(i) for i in b]
                    
                    if not d: 
                        f = a.split()
                        a = '+'.join(f)
                        bot = main_url.format(a)
                    else:
                        str2 = '&&'.join(d)
                        bot = str2
                else:
                    b = '&&'.join(b)
                    bot = b    
    elif a in product_list:
        str2 = d.split()
        str2 = '+'.join(str2)
        url = main_url.format(str2)
        bot =url
        # return bot
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



@app.route("/get_cart")
def add_to_cart():

    # checkout_url = "https://magento.arogyarahasya.com/checkout/?SID={}"
    checkout_url = "https://magento.arogyarahasya.com/checkout/cart/?SID={}"
    a = request.args.get('msg')
    
    data_products_name = pd.read_csv("AR_All.csv")
    pro_id = list(data_products_name['product_id'])
    pro_name = list(data_products_name['pro_name'])
    
    list1 = []
    i= [col for row,col in zip(pro_name,pro_id) if a in row ]
    print("i",i)
    id1 = i[0]
    print(id1)
    
        
    # r= requests.session()
    
    cart_url = "http://magento.arogyarahasya.com/restapi/rest_cart/updateCart"
    # get_cart_url = "http://magento.arogyarahasya.com/restapi/rest_cart/getCart"
    param = {

        'product_id':id1,
        'qty'       :1,
        'SID':session_id
    }
    

    response_cart    = requests.post(cart_url,params = param)

    bot = checkout_url.format(session_id)
    print(bot)
    # print(bot)
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




    # UAN:101377191704
    # pwd:aSHwMm*%@442