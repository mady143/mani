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
from metaphone import doublemetaphone
app = Flask(__name__)



english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)
# english_bot.train("./data")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def hello():

def get_bot_response():

    main_url = 'https://www.arogyarahasya.com/catalogsearch/result/?q={}'
    a = request.args.get('msg')
    # print(type(a))
    # print("a",a)

    # a = doublemetaphone(a)
    url_text = a.split()
 
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
    # # brands_list  = []

    data_products_name = pd.read_csv("AR_All.csv")
    pro_id = list(data_products_name['product_id'])
    pro_name = list(data_products_name['pro_name'])
    # print(pro_name[10])

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
                    # print("c",c)
                    b = [ x.replace(" ", '+') for x in c]
                    # print("b",b)
                    d = [ main_url.format(i) for i in b]
                    # print("d",d)
                    if not d: 
                        d = a.split()
                        a = '+'.join(d)
                        bot = main_url.format(a)
                    else:
                        str2 = '&&'.join(d)
                        bot = str2
                else:
                    b = '&&'.join(b)
                    bot = b    
    elif a in product_list:
        str2 = a.split()
        str2 = '+'.join(str2)
        url = main_url.format(str2)
        bot =url
        webbrowser.open(url)
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
            
@app.route("/get_cart")

def add_to_cart():

    # r= requests.session()
    # url = "http://magento.arogyarahasya.com/restapi/rest_mage/getSession"
    # payload = {
    #     'api_user' : "launchship",
    #     'api_key' : "JVYR5UJASE0SHOGW"
    #     }
    # response_session = r.post(url,data= payload)
    # ss = response_session.json()
    # session_id = ss["session_id"]
    # print(session_id)
    # data_products_name = pd.read_csv("AR_All.csv")
    # pro_id = list(data_products_name['product_id'])
    # pro_name = list(data_products_name['pro_name'])
    # cart_url = "http://magento.arogyarahasya.com/restapi/rest_cart/updateCart"

    # param = {

    #     'product_id':4,
    #     'qty'       :1,
    #     'SID':session_id
    # }

    # response_cart    = r.post(cart_url,data = param)
    # return (response_cart.text)
    return("Message")


if __name__ == "__main__":
    app.run()


    # 19031218476080S3























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
from metaphone import doublemetaphone
app = Flask(__name__)



english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)
# english_bot.train("./data")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def hello():

    def get_bot_response():

        main_url = 'https://www.arogyarahasya.com/catalogsearch/result/?q={}'
        a = request.args.get('msg')
        # print(type(a))
        # print("a",a)

        # a = doublemetaphone(a)
        url_text = a.split()
     
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
        # # brands_list  = []

        data_products_name = pd.read_csv("AR_All.csv")
        pro_id = list(data_products_name['product_id'])
        pro_name = list(data_products_name['pro_name'])
        # print(pro_name[10])

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
                        # print("c",c)
                        b = [ x.replace(" ", '+') for x in c]
                        # print("b",b)
                        d = [ main_url.format(i) for i in b]
                        # print("d",d)
                        if not d: 
                            d = a.split()
                            a = '+'.join(d)
                            bot = main_url.format(a)
                        else:
                            str2 = '&&'.join(d)
                            bot = str2
                    else:
                        b = '&&'.join(b)
                        bot = b    
        elif a in product_list:
            str2 = a.split()
            str2 = '+'.join(str2)
            url = main_url.format(str2)
            bot =url
            webbrowser.open(url)
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

        def fjhfhjfhgf(x):
            return " sfgfd"

    x=get_bot_response()
    y=fjhfhjfhgf(x)
            
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
            
@app.route("/get_cart")

def add_to_cart():

    # r= requests.session()
    # url = "http://magento.arogyarahasya.com/restapi/rest_mage/getSession"
    # payload = {
    #     'api_user' : "launchship",
    #     'api_key' : "JVYR5UJASE0SHOGW"
    #     }
    # response_session = r.post(url,data= payload)
    # ss = response_session.json()
    # session_id = ss["session_id"]
    # print(session_id)
    # data_products_name = pd.read_csv("AR_All.csv")
    # pro_id = list(data_products_name['product_id'])
    # pro_name = list(data_products_name['pro_name'])
    # cart_url = "http://magento.arogyarahasya.com/restapi/rest_cart/updateCart"

    # param = {

    #     'product_id':4,
    #     'qty'       :1,
    #     'SID':session_id
    # }

    # response_cart    = r.post(cart_url,data = param)
    # return (response_cart.text)
    return("Message")


if __name__ == "__main__":
    app.run()


    # 19031218476080S3