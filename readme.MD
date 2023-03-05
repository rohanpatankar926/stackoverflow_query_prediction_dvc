## pip install virtualenv
## virtualenv env  -->creating environment
## /env/Sripts/activate 
## pip install -r requirements.txt


data-->sending to s3-->
                     flask api<--->s3 bucket  ---> rapid api

                     
#### learnt this 28/feb/2023
s3_sync.py --> logic for s3 command
data_to_S3.py ---> main_data_folder sending to s3 bucket

api.py ---> two endpoint / and /xml_data
/---> it is json message 
/xml_data--> all the data from the s3 bucket   api<--->s3 bucket
 
