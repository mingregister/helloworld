FROM centos:7.6.1810

RUN yum clean all && yum install -y epel-release && yum update -y && yum install -y vim bind-utils net-tools tcpdump git make zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc libffi-devel && yum clean all

# # install python3.7.3
# curl -O https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
ADD Python-3.7.3.tgz /root/

WORKDIR /root/Python-3.7.3

RUN ./configure && make && make install

RUN mv /usr/bin/python /usr/bin/python.bak && ln -s /usr/local/bin/python3 /usr/bin/python && ln -s /usr/local/bin/pip3 /usr/bin/pip

RUN sed -i 's|#! /usr/bin/python|#! /usr/bin/python2|' /usr/libexec/urlgrabber-ext-down && \
    sed -i 's|#!/usr/bin/python|#!/usr/bin/python2|' /usr/bin/yum

# # install sqlite3
# # The minimum supported version of SQLite is increased from 3.7.15 to 3.8.3.
# curl -O http://www.sqlite.org/2019/sqlite-autoconf-3280000.tar.gz
ADD sqlite-autoconf-3280000.tar.gz /root
WORKDIR /root/sqlite-autoconf-3280000
RUN ./configure && make && make install \
       && mv  /usr/bin/sqlite3 /usr/bin/sqlite3.7.17 \
       && cp  sqlite3 /usr/bin/sqlite3 \
       && touch /etc/ld.so.conf.d/sqlite3.conf \
       && echo "/usr/local/lib" >> /etc/ld.so.conf.d/sqlite3.conf \
       && ldconfig

# # install django==2.2.2
RUN pip install django==2.2.2
WORKDIR /root/

# make django can use mysql as backend
# # 注意：如果这里加上yum update -y的话，会把python3.7.3 给覆盖了。
RUN yum clean all && yum install mysql mariadb-devel.x86_64 -y  && yum clean all && pip install mysqlclient==1.4.4

# ######
COPY requirement.txt /requirement.txt

RUN pip install -r /requirement.txt

COPY helloworld /app

# docker build -t django:1.0 . 
