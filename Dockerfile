FROM python:3.7.3-alpine


WORKDIR /app
COPY requirement.txt requirement.txt 
RUN pip install -r requirement.txt
COPY helloworld /app

# # mysqlclient没有装
# docker build -t django-hello-world:v1.0 . 
