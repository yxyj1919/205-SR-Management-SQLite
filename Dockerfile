# https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/
FROM ubuntu:20.04
LABEL authors="changw"
#WORKDIR /python-docker
RUN apt-get update -y 
RUN apt-get install -y python3-pip tzdata --no-install-recommends
COPY requirements.txt /tmp/
RUN pip3 install --requirement  /tmp/requirements.txt

ENV DB_SERVER='postgres' DB_PORT='5432' DB_NAME='sr_db' DB_USERNAME='postgress' DB_PASSWORD='password'
#COPY . .

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


#ENTRYPOINT ["top", "-b"]
