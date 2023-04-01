import argparse
import os,sys
sys.path.append(os.getcwd())
import logging
from utils import *
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
#pipelne
from sklearn.pipeline import Pipeline

STAGE = "Stage 03 featurization" 

def featurization(config_path, params_path):
    ## read config files
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts = config["artifacts"]
    prepared_data_dir_path = os.path.join(artifacts["ARTIFACTS_DIR"], artifacts["PREPARED_DATA"])
    train_data_path = os.path.join(prepared_data_dir_path, artifacts["TRAIN_DATA"])
    test_data_path = os.path.join(prepared_data_dir_path, artifacts["TEST_DATA"])

    featurized_data_dir_path = os.path.join(artifacts["ARTIFACTS_DIR"], artifacts["FEATURIZED_DATA"])
    os.makedirs(featurized_data_dir_path, exist_ok=True)

    featurized_train_data_path = os.path.join(featurized_data_dir_path, artifacts["FEATURIZED_TRAIN_DATA"])
    featurized_test_data_path = os.path.join(featurized_data_dir_path, artifacts["FEATURIZED_TEST_DATA"])

    df_train = get_df(train_data_path)
    train_words = np.array(df_train.text.str.lower().values.astype("U")) ## << U1000
    max_features = params["featurize"]["max_featurize"]
    ngrams = params["featurize"]["ngrams"]
    bag_of_words = CountVectorizer(
        stop_words="english", max_features=max_features, ngram_range=(1, ngrams)
    )
    tfidf = TfidfTransformer(smooth_idf=False)
    pipeline=Pipeline([('bag_of_words',bag_of_words),('tfidf',tfidf)])
    pipeline_save_path = os.path.join(featurized_data_dir_path, artifacts["TRANSFORMATION_SAVE"])
    pipeline.fit(train_words)
    joblib.dump(pipeline, pipeline_save_path)
    train_words_tfidf_matrix = pipeline.transform(train_words)
    save_matrix(df_train, train_words_tfidf_matrix, featurized_train_data_path)
    df_test = get_df(test_data_path)
    test_words = np.array(df_test.text.str.lower().values.astype("U")) ## << U1000
    test_words_tfidf_matrix = pipeline.transform(test_words)
    save_matrix(df_test, test_words_tfidf_matrix, featurized_test_data_path)
    
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        featurization(config_path=parsed_args.config, params_path=parsed_args.params)
    except Exception as e:
        raise e