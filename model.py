from transformers import AutoTokenizer, AutoModelForSequenceClassification,DistilBertForSequenceClassification, DistilBertTokenizer
from torch import nn
import json

model_name = "j-hartmann/emotion-english-distilroberta-base"#"SamLowe/roberta-base-go_emotions"#"cardiffnlp/twitter-roberta-base-sentiment"
ptmodel = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

class classifier:
    def runmodel(self,sentence):
        user_input = sentence
        print(user_input)
        ptbatch = tokenizer(user_input,padding=True,truncation=True,max_length=512,return_tensors="pt")
        ptoutputs = ptmodel(**ptbatch)
        ptprediction = nn.functional.softmax(ptoutputs.logits, dim=-1)
        return ptprediction
    
    def model_result(self,sentence):
        prediction=self.runmodel(sentence)
        result_dict={
            "Anger":prediction[0][0].item(),
            "Disgust":prediction[0][1].item(),
            "Fear":prediction[0][2].item(),
            "Joy":prediction[0][3].item(),
            "Neutral":prediction[0][4].item(),
            "Sadness":prediction[0][5].item(),
            "Surprise":prediction[0][6].item()
        }

        result_dict = sorted(result_dict.items(), key=lambda x:x[1],reverse=True)
        result_json=json.dumps(result_dict,indent=2)
        return result_json

