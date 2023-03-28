import os,sys
sys.path.append(os.getcwd())
import argparse
from tqdm import tqdm
import shutil
from utils import process_posts
from utils import *

STAGE="stage_02_prepare_data"


def preparedata(config_path,params_path):
        config=read_yaml(config_path)
        params=read_yaml(params_path)
        local_data_dir=config["source_download_dir"]["download_dir"]
        data_file_name=config["source_download_dir"]["data_file"]
        input_data=os.path.join("artifacts",local_data_dir,data_file_name)
        split_ratio=params["train_test"]["split"]
        seed=params["train_test"]["seed"]
        random.seed(seed)
        artifacts=config["artifacts"]
        prepared_data_dir=os.path.join(artifacts["ARTIFACTS_DIR"],artifacts["PREPARED_DATA"])
        os.makedirs(prepared_data_dir,exist_ok=True)
        train_data=os.path.join(prepared_data_dir,artifacts["TRAIN_DATA"])
        test_data=os.path.join(prepared_data_dir,artifacts["TEST_DATA"])
        with open(input_data,"r") as f_in:
            with open(train_data,"w") as train_f:
                with open(test_data,"w") as test_f:
                    process_posts(f_in.read(),"<python>",train_f,test_f ,split_ratio)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--config","-c",default="config.yaml",help="config file path")
    parser.add_argument("--params","-p",default="params.yaml",help="params file path")
    parsed_args=parser.parse_args()

    try:
        # prepare_data=PrepareData()
        preparedata(config_path=parsed_args.config,params_path=parsed_args.params)
    except Exception as e:
        raise e