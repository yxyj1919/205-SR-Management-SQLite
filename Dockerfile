# https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/
FROM ubuntu:20.04
LABEL authors="changw"
#WORKDIR /python-docker
RUN apt-get update -y 
RUN apt-get install -y python3-pip tzdata --no-install-recommends
WORKDIR /python-docker

COPY requirements.txt /python-docker
RUN pip3 install --requirement  /python-docker/requirements.txt

COPY . .
#x@COPY *.py /python-docker
#COPY templates /python-docker/templates
#COPY requirements.txt /python-docker
#RUN pip3 install --requirement  /python-docker/requirements.txt
ENV DB_SERVER='postgres' DB_PORT='5432' DB_NAME='sr_db' DB_USERNAME='postgres' DB_PASSWORD='password'
#COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


#ENTRYPOINT ["top", "-b"]
