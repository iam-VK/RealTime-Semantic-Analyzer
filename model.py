from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
from torch import nn
import json
import collections

emotion_model = "roberta-base-go_emotions"
emotion_ptmodel = AutoModelForSequenceClassification.from_pretrained(emotion_model)
emotion_tokenizer = AutoTokenizer.from_pretrained(emotion_model)
emotion_config = AutoConfig.from_pretrained(emotion_model)

classifier_model = "twitter-roberta-base-sentiment-latest"
classifier_ptmodel = AutoModelForSequenceClassification.from_pretrained(classifier_model)
classifier_tokenizer = AutoTokenizer.from_pretrained(classifier_model)
classifier_config = AutoConfig.from_pretrained(classifier_model)

class emotion_classifier:
    def runmodel(self,sentence):
        user_input = sentence
        ptbatch = emotion_tokenizer(user_input,padding=True,truncation=True,max_length=512,return_tensors="pt")
        ptoutputs = emotion_ptmodel(**ptbatch)
        ptprediction = nn.functional.softmax(ptoutputs.logits, dim=-1)
        return ptprediction
    
    def model_result(self,sentence):
        prediction=self.runmodel(sentence)

        id2label = emotion_config.id2label
        scores = prediction[0].tolist()
        labled_prediction = {label: round(score*100,1) for label, score in zip(id2label.values(), scores)}

        result_dict = sorted(labled_prediction.items(), key=lambda x:x[1],reverse=True)
        ordered_dict = collections.OrderedDict(result_dict)

        result_json=json.dumps(ordered_dict,indent=2)
 
        return result_json

class sentence_classifier:
    def runmodel(self,sentence):
        user_input = sentence
        ptbatch = classifier_tokenizer(user_input,padding=True,truncation=True,max_length=512,return_tensors="pt")
        ptoutputs = classifier_ptmodel(**ptbatch)
        ptprediction = nn.functional.softmax(ptoutputs.logits, dim=-1)
        return ptprediction
    
    def model_result(self,sentence):
        prediction=self.runmodel(sentence)

        id2label = classifier_config.id2label
        scores = prediction[0].tolist()
        labled_prediction = {label: round(score*100,1) for label, score in zip(id2label.values(), scores)}

        result_dict = sorted(labled_prediction.items(), key=lambda x:x[1],reverse=True)
        ordered_dict = collections.OrderedDict(result_dict)

        result_json=json.dumps(ordered_dict,indent=2)
 
        return result_json