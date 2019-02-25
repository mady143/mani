from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import yaml

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)
# english_bot.train("./data")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
	
	userText = request.args.get('msg')
	# print(userText)
	text =  str(english_bot.get_response(userText))

	Chathistory = "chathistory"
	a = {"categories":[Chathistory]}
	b = {"converstaions":[[userText,text]]}
	
	


	with open("chat.yml","a") as outfile:
		
		yaml.dump(a,outfile,default_flow_style=False)
		yaml.dump(b,outfile,default_flow_style=False)
	
		

	return text
if __name__ == "__main__":
    app.run()