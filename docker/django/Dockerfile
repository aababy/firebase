FROM ubuntu:16.04

MAINTAINER Dockerfiles

# 环境变量
COPY pip.conf pip.conf
ENV PIP_CONFIG_FILE pip.conf
ENV MYSQL_DATABASE_NAME jigsaw
ENV EMAIL_HOST_USER my-email@email.com
ENV EMAIL_HOST_PASSWORD 123456

# 安装git、python、nginx、supervisor等，并清理缓存
RUN apt-get update \
        && apt-get upgrade -y \
        && apt-get install -y \
        git \
        nano \
        python \
        python-dev \
        python-setuptools \
        python-pip \
        nginx \
        supervisor \
        libssl-dev \
        && pip install -U pip \
        && hash -r pip \
        && pip install -U setuptools \
        && pip install uwsgi \
        && rm -rf /var/lib/apt/lists/*
        
# nginx、supervisor配置
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

# 安装项目所需python第三方库 ~/docker/code/jigsaw/ 这个是代码目录
COPY requirements.txt /home/code/jigsaw/
RUN pip install -r /home/code/jigsaw/requirements.txt

# uwsgi.ini 及 uwsgi_params
COPY . /home/code/

EXPOSE 981
CMD ["supervisord", "-n"]
