import joblib
import numpy as np
import os,sys
sys.path.append(os.getcwd())
from utils import *

class PredictionService(object):
    def __init__(self,model_path,transformer_path,batch_data):
        self.model=joblib.load(open(model_path,'rb'))
        self.transformer=joblib.load(open(transformer_path,'rb'))
        self.batch_data=batch_data

    def inference(self):
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
    
if __name__ == '__main__':
    model_path =  f'{os.getcwd()}/artifacts/model/model.pkl'
    transformer_path = f'{os.getcwd()}/artifacts/features/transformer.pkl'
    batch_data = 'predict.tsv'
    prediction_service = PredictionService(model_path,transformer_path,batch_data)
    prediction_service.inference()