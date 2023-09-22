from transformers import AutoTokenizer, AutoModelForSequenceClassification,DistilBertForSequenceClassification, DistilBertTokenizer
from torch import nn

model_name = "cardiffnlp/twitter-roberta-base-sentiment"
ptmodel = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

class classifier:
    def model(self,uinput):
        user_input = uinput#input("Sentence: ")#"hi bro watcha doing"
        print(user_input)
        ptbatch = tokenizer(user_input,padding=True,truncation=True,max_length=512,return_tensors="pt")
        ptoutputs = ptmodel(**ptbatch)
        self.ptprediction = nn.functional.softmax(ptoutputs.logits, dim=-1)
        print("\n^^^^^^^^^^^^Result^^^^^^^^^^^^")
        print("Raw ",self.ptprediction)
        print("Score ",self.ptprediction[0][1].item())
        print("Positive" if self.ptprediction[0][1].item()>0.5 else "Negative") 
        #return ["Positive" if self.ptprediction[0][1].item()>0.5 else "Negative",user_input] 
    
    def model_result(self):
        self.classify("hi")
        return str(self.ptprediction)


