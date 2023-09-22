from flask import Flask,request
from model import classifier

app = Flask(__name__)

@app.route("/classify/<uinput>")
def classify(uinput):
    model=classifier()
    return model.model_result()





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

