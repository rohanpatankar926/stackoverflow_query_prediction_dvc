

### creation of virtualenv<br>
pip install virtualenv<br>
virtualenv env <br>
.\env\Scripts\activate --> windows<br>
source venv/bin/activate --> linux<br>
deactivate<br>

### installing all deps<br>
pip install -r requirements.txt<br>


pip install awscli<br>
aws configure in vs code terminal <br>
attach access and secret access key<br>
create AWS account<br>
---> create IAM role<br>
----> create s3 bucket<br>

s3_sync.py --> class for sending data to s3<br>
data_to_s3.py---> data sending to s3<br>
main_data/data.xml-->datafile<br>
requirements.txt---> pip install -r requirements.txt<br>
api.py---> interact with falsk and s3 and getting all the data to<br> webpage.  cmd--> python api.py<br>
