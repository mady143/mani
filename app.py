# from flask import Flask, render_template
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

# app = Flask(__name__)

# english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

# english_bot.set_trainer(ListTrainer)
# english_bot.train("./data")


# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/get")
# def get_bot_response():
#     userText = request.args.get('msg')
#     return str(english_bot.get_response(userText))


		
# if __name__ == "__main__":
#     app.run()




# from flask import Flask, render_template, request
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer

# app = Flask(__name__)

# english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

# english_bot.set_trainer(ChatterBotCorpusTrainer)
# english_bot.train("./data")


# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/get")
# def get_bot_response():
#     userText = request.args.get('msg')
#     return str(english_bot.get_response(userText))


		
# if __name__ == "__main__":
#     app.run()

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("./data")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


		
if __name__ == "__main__":
    app.run()
