

# from flask import Flask,jsonify,request
# app = Flask(__name__)

# @app.route("/")
# def hello():
# 	return jsonify({"about":"Hello World"})
# if __name__ == '__main__':
# 	app.run()

# from flask import Flask,jsonify
# import requests
# app = Flask(__name__)

from flask import Flask,jsonify
import requests
import json
import yaml
import urllib3
import sys
import pandas as pd
import ast
app = Flask(__name__)
@app.route("/")
def hello():
	r= requests.session()
	url = "http://magento.arogyarahasya.com/restapi/rest_mage/getSession"
	payload = {
	    'api_user' : "launchship",
	    'api_key' : "JVYR5UJASE0SHOGW"
	    }
	response_session = r.post(url,data= payload)
	ss = response_session.json()
	session_id = ss["session_id"]
	print(session_id)
	data_products_name = pd.read_csv("AR_All.csv")
	pro_id = list(data_products_name['product_id'])
	pro_name = list(data_products_name['pro_name'])
	cart_url = "http://magento.arogyarahasya.com/restapi/rest_cart/updateCart"

	param = {

		'product_id':1313,
		'qty'		:1,
		'SID':session_id
	}

	response_cart    = r.post(cart_url,data = param)
	return (response_cart.text)
if __name__ == '__main__':
	app.run()



# import requests
# import json
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

# cart_url = "http://magento.arogyarahasya.com/restapi/rest_cart/updateCart"

# param = {

# 	'product_id':1322,
# 	'qty'		:5,
# 	'SID':session_id
# }
# data_message ={'messages':'Added Sucessufully'}

# response_cart    = r.post(cart_url,data = param)
# print(response_cart.json())
# # ss = response.json()	
# # print(ss["session_id"])

# # print(response.json())