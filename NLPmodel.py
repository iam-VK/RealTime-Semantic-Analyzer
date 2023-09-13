from transformers import AutoTokenizer, AutoModelForSequenceClassification,DistilBertForSequenceClassification, DistilBertTokenizer
from torch import nn
from flask import Flask,request

app = Flask(__name__)
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
ptmodel = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
#input = tokenizer("Hi good to see ya")

# @app.route('/classify',methods=['POST'])
# def classify():
#     user_input = request.json#input("Sentence: ")#"hi bro watcha doing"
#     print(user_input)
#     ptbatch = tokenizer(user_input,padding=True,truncation=True,max_length=512,return_tensors="pt")
#     ptoutputs = ptmodel(**ptbatch)
#     ptprediction = nn.functional.softmax(ptoutputs.logits, dim=-1)
#     print("\n^^^^^^^^^^^^Result^^^^^^^^^^^^")
#     print("Raw ",ptprediction)
#     print("Score ",ptprediction[0][1].item())
#     print("Positive" if ptprediction[0][1].item()>0.5 else "Negative") 
#     return ["Positive" if ptprediction[0][1].item()>0.5 else "Negative",user_input] 

@app.route("/classify/<uinput>")
def classify(uinput):
    user_input = uinput#input("Sentence: ")#"hi bro watcha doing"
    print(user_input)
    ptbatch = tokenizer(user_input,padding=True,truncation=True,max_length=512,return_tensors="pt")
    ptoutputs = ptmodel(**ptbatch)
    ptprediction = nn.functional.softmax(ptoutputs.logits, dim=-1)
    print("\n^^^^^^^^^^^^Result^^^^^^^^^^^^")
    print("Raw ",ptprediction)
    print("Score ",ptprediction[0][1].item())
    print("Positive" if ptprediction[0][1].item()>0.5 else "Negative") 
    return ["Positive" if ptprediction[0][1].item()>0.5 else "Negative",user_input] 





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

#pip freeze >requirements.txt        source venv/bin/activate 
