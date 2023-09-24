from flask import Flask
from flask_cors import CORS
from model import classifier

app = Flask(__name__)
CORS(app)

@app.route("/classify/<user_input>")
def classify(user_input):
    model=classifier()
    return model.model_result(user_input)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)