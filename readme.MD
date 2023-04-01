## component2
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