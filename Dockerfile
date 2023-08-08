# https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/
FROM ubuntu:latest
LABEL authors="changw"

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


ENTRYPOINT ["top", "-b"]