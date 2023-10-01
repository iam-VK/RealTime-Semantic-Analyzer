from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
from torch import nn
import json
import collections

model_name = "roberta-base-go_emotions"
ptmodel = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
config = AutoConfig.from_pretrained(model_name)

class classifier:
    def runmodel(self,sentence):
        user_input = sentence
        ptbatch = tokenizer(user_input,padding=True,truncation=True,max_length=512,return_tensors="pt")
        ptoutputs = ptmodel(**ptbatch)
        ptprediction = nn.functional.softmax(ptoutputs.logits, dim=-1)
        return ptprediction
    
    def model_result(self,sentence):
        prediction=self.runmodel(sentence)

        id2label = config.id2label
        scores = prediction[0].tolist()
        labled_prediction = {label: round(score*100) for label, score in zip(id2label.values(), scores)}

        result_dict = sorted(labled_prediction.items(), key=lambda x:x[1],reverse=True)
        ordered_dict = collections.OrderedDict(result_dict)

        result_json=json.dumps(ordered_dict,indent=2)
 
        return result_json