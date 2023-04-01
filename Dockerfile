FROM python:3.8
RUN mkdir app/
COPY . /app/
WORKDIR /app
RUN apt-get update && apt-get install -y git
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
VOLUME [ "/artifacts" ]
RUN dvc init -f

CMD ["dvc", "repro","-v"]