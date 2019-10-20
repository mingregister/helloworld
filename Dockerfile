FROM registry.cn-shenzhen.aliyuncs.com/zmhuangpub/python:3.7.3-sqlite3-mysql

#####
COPY requirement.txt /requirement.txt
RUN pip install -r /requirement.txt
COPY helloworld /app

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# docker build -t registry.cn-shenzhen.aliyuncs.com/zmhuang/pythoncicd:v1.0 .
# docker run --rm --entrypoint /bin/bash -it  registry.cn-shenzhen.aliyuncs.com/zmhuang/pythoncicd:v1.0 
