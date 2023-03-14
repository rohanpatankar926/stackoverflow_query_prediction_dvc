#convert the xml to json
#read_json file
import os 
import json
import xmltodict
import sys
sys.path.append(os.getcwd())
import random
import yaml
import re
import tqdm
from xml.etree import ElementTree as ET
import pandas as pd
import scipy.sparse as sparse
import joblib
import logging
import numpy as np

#convert the xml data to the json data
def convert_xml_to_json(file_path):
    try:
        with open(file_path,"r") as data:
            xml_data=xmltodict.parse(data.read())
        return xml_data
    except Exception as e:
        raise e

def save_json_xml(input_file, output_path):
    try:
        output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(output_dir, exist_ok=True)
        data = convert_xml_to_json(input_file)
        json_data = json.dumps(data)  # convert JSON data to a string
        with open(f"{output_dir}/{output_path}", "w") as f:
            f.write(json_data)  # write the string to file
    except Exception as e:
        raise e

def save_json(data,output_file_name):
    try:
        data_save=json.dump(data,open(output_file_name,"w"))
        return data_save
    except Exception as e:
        raise e

def read_json_data(file_path):
    try:
        with open(file_path,"r") as data:
            cvat_data=json.load(data)
        return cvat_data
    except Exception as e:
        raise e

def process_posts(f_in, target_tag, f_out_train, f_out_test, split):
    try:
        root = ET.fromstring(f_in)
        for child in root:
            pid = child.get('Id', "")
            label = 1 if target_tag in child.get('Tags', "") else 0
            title = re.sub(r"\s+", " ", child.get('Title', "")).strip()
            body = re.sub(r"\s+", " ", child.get('Body', "")).strip()
            text = title + " " + body
            f_out = f_out_train if random.random() > split else f_out_test
            f_out.write(f"{pid}\t{label}\t{text}\n")
    except Exception as e:
        msg = f"{e}\n"
        raise Exception(msg)

def read_yaml(config_path):
    try:
        with open(config_path,"r") as data:
            config_data=yaml.safe_load(data)
        return config_data
    except Exception as e:
        raise e
    


def get_df(path_to_data: str, sep: str="\t") -> pd.DataFrame:
    df = pd.read_csv(
        path_to_data, 
        encoding="utf-8",
        header=None,
        delimiter=sep,
        names=["id", "label", "text"]
    )
    return df

def save_matrix(df, matrix, out_path):
    id_matrix = sparse.csr_matrix(df.id.astype(np.int64)).T
    label_matrix = sparse.csr_matrix(df.label.astype(np.int64)).T

    result = sparse.hstack([id_matrix, label_matrix, matrix], format="csr")

    joblib.dump(result, out_path)
    msg = f"The output matrix saved at: {out_path} of the size: {result.shape} and data type: {result.dtype}"
    logging.info(msg)