

## 1st session
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



## 2nd session

1.Create Ec2 machine <br>
2.connect to ec2 machine<br>
3.inside vm terminal ---> cmd---> `git clone https://github.com/rohanpatankar926/stackoverflow_query_prediction_dvc.git`<br>
4. cd stackoverflow_query_prediction_dvc<br>
5. change the port and hostname<br>
6. python3 api.py<br>
7. open the ec2 machine ipv4 url with port mapping to 8000<br>
8. make account on rapid api and follow the steps and depliy the hosted link <br>
9. fetch the data from src/stage_01_get_data.py file u can able to fetch all the data to the destination folder of artifacts this is data ingestion pipeline...

## 3rd Session

Git and github tutorial
git init
git add .
git commit -m "message"
git remote add origin git_url 
git checkout -b branch_name
git push origin branch_name

### component2 ml pipeline
1-->all ml stages from stage1 to stage5 in src directory deps are config.yml and params.yml and utils.yml
2-->make dvc.yaml and write 5 stage script
3-->install dvc `pip install dvc-s3`
4-->git init
4-->dvc init 
5-->dvc add main_data/data.xml
6-->git add .
7-->git commit -m "msg"
8-->dvc repro for 1 stage and again git add . and git commit -m "msg do for  5 times for 5 stages
9-->dvc plots show generates html template for showing the plot curve
10-->upload to github git push
11-->go to https://studio.iterative.ai and make account
12-->`add a project` and then add the main repository
13--> now u can able to track all the git commits wrt the data versions and also experiment and compare the models
14-->End 

