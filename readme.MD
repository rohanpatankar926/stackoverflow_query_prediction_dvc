sudo docker build -t stack_overflow:v1 <br>
sudo docker tag stack_overflow:v1 rohan9887700/stack_overflow:v1<br>
before this signin to dockerhub<br>
sudo docker push rohan9887700/stack_overflow:v2<br>
goto ec2 and the install docker<br>
sudo apt update<br>
sudo apt install docker.io<br>
sudo docker pull rohan9887700/stack_overflow:v2<br>
sudo docker run -t -d -p 8000:8000 rohan9887700/stack_overflow:v2v