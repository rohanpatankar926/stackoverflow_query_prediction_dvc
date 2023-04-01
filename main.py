from src.stage_01_get_data import GetData
from src.stage_02_prepare import preparedata
from src.stage_03_featurization import featurization
from src.stage_04_train import train
from src.stage_05_model_evaluate import evaluate
from loguru import logger

def initiate_pipeline():
    try:
        get_data=GetData()
        logger.info("Stage 1 - Get Data")
        get_data.get_data(config_path="config.yaml")
        logger.info("stage 2 - Prepare Data")
        preparedata(config_path="config.yaml",params_path="params.yaml")
        logger.info("stage 3 - Featurization")
        featurization(config_path="config.yaml",params_path="params.yaml")
        logger.info("stage 4 - Training")
        train(config_path="config.yaml",params_path="params.yaml")
        logger.info("stage 5 - Model Evaluation")
        evaluate(config_path="config.yaml")
    except Exception as e:
        raise e
    
if __name__=="__main__":
    initiate_pipeline()