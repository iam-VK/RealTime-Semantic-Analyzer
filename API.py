from flask import Flask
from flask_cors import CORS
from model import emotion_classifier,sentence_classifier

app = Flask(__name__)
CORS(app)

@app.route("/classify-emotion/<user_input>")
def classify_emotion(user_input):
    emotionmodel=emotion_classifier()
    return emotionmodel.model_result(user_input)

@app.route("/classify-sentence/<user_input>")
def classify_sentence(user_input):
    sentencemodel=sentence_classifier()
    return sentencemodel.model_result(user_input)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)