import argparse
import os,sys
import joblib
import logging
sys.path.append(os.getcwd())
from utils import read_yaml, save_json
import numpy as np
import sklearn.metrics as metrics
import math


def evaluate(config_path):
    config=read_yaml(config_path)
    artifacts=config["artifacts"]
    featurized_data_dir_path = os.path.join(artifacts["ARTIFACTS_DIR"], artifacts["FEATURIZED_DATA"])
    featurized_test_data_path = os.path.join(featurized_data_dir_path, artifacts["FEATURIZED_TEST_DATA"])
    model_dir_path = os.path.join(artifacts["ARTIFACTS_DIR"], artifacts["MODEL_DIR"])
    model_path = os.path.join(model_dir_path, artifacts["MODEL_NAME"])
    model = joblib.load(model_path)
    matrix = joblib.load(featurized_test_data_path)
    labels = np.squeeze(matrix[:, 1].toarray())
    X = matrix[:, 2:]
    prediction_by_class=model.predict_proba(X)
    predictions=prediction_by_class[:,1]
    PREC_JSON_PATH=artifacts["plots"]["PRC"]
    ROC_JSON_PATH=artifacts["plots"]["ROC"]
    scores_json_file=artifacts["metrics"]["SCORES"]
    avg_prec=metrics.average_precision_score(labels,predictions)
    roc_auc=metrics.roc_auc_score(labels,predictions)

    scores={
        "roc_auc_score":roc_auc,
        "average_precision_score":avg_prec
    }
    save_json(scores,scores_json_file)
    precision,recall,thresholds=metrics.precision_recall_curve(labels,predictions)
    nth_pints=math.ceil(len(precision)/100)
    prc_points=list(zip(precision,recall,thresholds))[::nth_pints]
    prc_data=[{"precision":p,"recall":r,"threshold":t} for p,r,t in prc_points]
    save_json(prc_data,PREC_JSON_PATH)
    fpr, tpr, roc_threshold = metrics.roc_curve(labels, predictions)
    roc_data = {"roc": [{"fpr": fp, "tpr": tp, "threshold": t} for fp, tp, t in zip(fpr, tpr, roc_threshold)]} 
    save_json(roc_data, ROC_JSON_PATH)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config.yaml")
    parsed_args = args.parse_args()

    try:
        evaluate(config_path=parsed_args.config, )
    except Exception as e:
        raise e