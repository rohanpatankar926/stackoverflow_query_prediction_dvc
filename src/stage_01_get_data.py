import os,sys
sys.path.append(os.getcwd())
from utils import *
from loguru import logger
import requests
from argparse import ArgumentParser

STAGE="stage_01_get_data"


class GetData:
    def get_data(self,config_path):
        config=read_yaml(config_path)
        download_dir=os.path.join(config["artifacts"]["ARTIFACTS_DIR"],config["source_download_dir"]["download_dir"])
        os.makedirs(download_dir,exist_ok=True)
        url = config["RapidApi"]["api_url"]
        headers = {
            "X-RapidAPI-Key": config["RapidApi"]["api_header_key"],
            "X-RapidAPI-Host": config["RapidApi"]["api_header_host"]
        }
        response = requests.request("GET", url, headers=headers)
        with open(os.path.join(download_dir,config["source_download_dir"]["data_file"]),"w") as xml_data:
            xml_data.write(response.text)
        logger.info(f"Data downloaded successfully at {download_dir}")


if __name__=="__main__":
    parser=ArgumentParser()
    parser.add_argument("--config","-c",help="config file path",default="config.yaml")
    parsed_args=parser.parse_args()
    try:
        get_data=GetData()
        get_data.get_data(parsed_args.config)
    except Exception as e:
        logger.exception(e)
        raise e