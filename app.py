from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
from ecommercebot.retrieval_generation import generation
from ecommercebot.data_ingest import ingestData
import os

app = Flask(__name__)

load_dotenv()

vstore=ingestData("done")
chain=generation(vstore)

os.environ["TOKENIZERS_PARALLELISM"] = "false"

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    result=chain.invoke(input)
    print("Response : ", result)
    return str(result)

if __name__ == '__main__':
    app.run(debug= True)