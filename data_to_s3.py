from utils import *
import os
from s3_sync import S3Sync
from dotenv import load_dotenv
load_dotenv()

# class DataPipeline:
#     def __init__(self,file_path):
#         self.filepath=os.path.join(os.getcwd(),file_path)
    
#     def preprocess_xml_data(self, target_tag, output_file):
#         if not os.path.exists(self.filepath):
#             return FileNotFoundError
#         os.makedirs(os.path.dirname(output_file), exist_ok=True)
#         output_list = []
#         for filename in os.listdir(self.filepath):
#             if filename.endswith(".xml"):
#                 xml_path = os.path.join(self.filepath, filename)
#                 json_data = convert_xml_to_json(xml_path)
#                 for i in tqdm(json_data["data"]["row"]):
#                     new_dict = {}
#                     for k, v in i.items():
#                         if k == "@Body":
#                             new_dict["Body"] = re.sub(r"\s+", " ", v).strip()
#                         elif k == "@Title":
#                             new_dict["Title"] = re.sub(r"\s+", " ", v).strip()
#                         elif k == "@Tags":
#                             new_dict["Tags"] = 1 if target_tag in v else 0
#                         else:
#                             new_dict[k[1:]] = v

#                     output_list.append(new_dict)
#         for data in output_list:
#             print(data.keys())
#             if "Title" in data.keys() and "Body" in data.keys():
#                 combined_data = data["Title"] + " " + data["Body"]
#                 data["combined_data"] = combined_data
#             else:
#                 data["combined_data"] = ""
        
#             # combined_data=data["Title"]+" "+data["Body"]
#             # data["combined_data"]=combined_data
        
#         save_json(output_list, output_file)
#         return "Saved successfully"


class DataDumpS3:
    def __init__(self, file_path):
        self.bucket_name = os.getenv("AWS_S3_BUCKET")
        self.file_path= file_path
    
    def dump_data(self):
        for file in os.listdir(self.file_path):
            if file.endswith(".xml"):
                data_dir=os.path.join(os.getcwd(),self.file_path)
                print(data_dir)
                s3_uri=f"s3://{self.bucket_name}/stack_overflow_data"
                S3Sync.s3_json_folder_sync(data_dir,s3_uri)
            else:
                return "Data failed to store in s3 bucket"

if __name__=="__main__":
    print(DataDumpS3("main_data").dump_data())

    