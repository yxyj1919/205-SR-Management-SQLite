# https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/
FROM ubuntu:20.04
 
ARG IMAGE_CREATE_DATE
ARG IMAGE_VERSION
ARG IMAGE_SOURCE_REVISION
 
# Metadata as defined in OCI
# https://github.com/opencontainers/image-spec/blob/main/annotations.md?plain=1
LABEL maintainer="changw@vmware.com" \
      NAME="___name___" \
      Version="___version___" \
      org.opencontainers.image.title="My App Test Image" \
      org.opencontainers.image.description="For Test Only" \
      org.opencontainers.image.created=$IMAGE_CREATE_DATE \
      org.opencontainers.image.authors="Chang WANG" \
      org.opencontainers.image.version=$IMAGE_VERSION \
      org.opencontainers.image.url=" " \
      org.opencontainers.image.documentation=" " \
      org.opencontainers.image.vendor="Chang WANG" \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.source="http://192.168.10.31/root/my-app-k8s.git" \
      org.opencontainers.image.revision=$IMAGE_SOURCE_REVISION
 
# Update
RUN apt-get update -y 
 
# Set Timezone
ENV TIME_ZONE Asia/Shanghai
RUN ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime
 
# Create app directory
RUN mkdir -p /python-docker
WORKDIR /python-docker
 
# Install basic packages
RUN apt-get install -y python3-pip tzdata --no-install-recommends

# Install app dependenies
COPY requirements.txt /python-docker
RUN pip3 install --requirement  /python-docker/requirements.txt
 
# Bundle app source
COPY . .

# Set ENV
ENV DB_SERVER='my-flask-app-postgres-svc.ara-gss-chn-devops.svc.cluster.local' \
    DB_PORT='5432' \
    DB_NAME='sr_db' \
    DB_USERNAME='postgres' \
    DB_PASSWORD='password'

# COMMAND
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
