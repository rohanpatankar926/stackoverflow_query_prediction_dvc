import joblib
import numpy as np
import os,sys
sys.path.append(os.getcwd())
from utils import *

class PredictionService(object):
    def __init__(self,model_path,transformer_path,batch_data=None):
        self.model=joblib.load(open(model_path,'rb'))
        self.transformer=joblib.load(open(transformer_path,'rb'))
        self.batch_data=batch_data

    def inference_batch(self):
        transformer=self.transformer
        model=self.model
        test_data=get_df_for_predict("predict.tsv")
        test_words = np.array(test_data.text.str.lower().values.astype("U")) ## << U1000
        test_transformer=transformer.transform(test_words)
        y_pred = model.predict(test_transformer)
        y_pred = np.array(y_pred)
        print(y_pred)
        test_data['predicted_tags'] = y_pred
        if os.path.exists('predict.csv'):
            os.remove('predict.csv')
        test_data["predicted_tags"]=test_data["predicted_tags"].replace({0.0:"not python query",1.0:"python related query"})
        test_data.to_csv('predict.csv', index=False)
        logging.info("Predictions saved to predict.tsv")
        return y_pred
    
    def inference_single(self,text):
        transformer=self.transformer
        model=self.model
        test_transformer=transformer.transform([text])
        y_pred = model.predict(test_transformer)
        y_pred = np.array(y_pred)
        if y_pred==[1.0]:
            return "python related query"
        else:
            return "not python query"

if __name__ == '__main__':
    model_path =  f'{os.getcwd()}/artifacts/model/model.pkl'
    transformer_path = f'{os.getcwd()}/artifacts/features/transformer.pkl'
    batch_data = 'predict.tsv'
    prediction_service = PredictionService(model_path,transformer_path,batch_data)
    print(prediction_service.inference_single('''Searching and capturing a character using regular expressions Python <p>While going through one of the problems in <a href="http://www.pythonchallenge.com/" rel="nofollow">Python Challenge</a>, I am trying to solve it as follows:</p> <p>Read the input in a text file with characters as follows:</p> <pre><code>DQheAbsaMLjTmAOKmNsLziVMenFxQdATQIjItwtyCHyeMwQTNxbbLXWZnGmDqHhXnLHfEyvzxMhSXzd BEBaxeaPgQPttvqRvxHPEOUtIsttPDeeuGFgmDkKQcEYjuSuiGROGfYpzkQgvcCDBKrcYwHFlvPzDMEk MyuPxvGtgSvWgrybKOnbEGhqHUXHhnyjFwSfTfaiWtAOMBZEScsOSumwPssjCPlLbLsPIGffDLpZzMKz jarrjufhgxdrzywWosrblPRasvRUpZLaUbtDHGZQtvZOvHeVSTBHpitDllUljVvWrwvhpnVzeWVYhMPs kMVcdeHzFZxTWocGvaKhhcnozRSbWsIEhpeNfJaRjLwWCvKfTLhuVsJczIYFPCyrOJxOPkXhVuCqCUgE luwLBCmqPwDvUPuBRrJZhfEXHXSBvljqJVVfEGRUWRSHPeKUJCpMpIsrV....... </code></pre> <p>What I need is to go through this text file and pick all lower case letters that are enclosed by only three upper-case letters on each side.</p> <p>The python script that I wrote to do the above is as follows:</p> <pre><code>import re pattern = re.compile("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]") f = open('/Users/Dev/Sometext.txt','r') for line in f: result = pattern.search(line) if result: print result.groups() f.close() </code></pre> <p>The above given script, instead of returning the capture(list of lower case characters), returns all the text blocks that meets the regular expression criteria, like</p> <pre><code>aXCSdFGHj vCDFeTYHa nHJUiKJHo ......... ......... </code></pre> <p>Can somebody tell me what exactly I am doing wrong here? And instead of looping through the entire file, is there an alternate way to run the regular expression search on the entire file?</p> <p>Thanks</p>'''))